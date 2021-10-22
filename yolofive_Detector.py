import numpy as np
import pandas as pd
import torch

from torch._C import device

from videoflow.core.node import ProcessorNode
from videoflow.core.constants import CPU, GPU #You can set CPU instead of GPU at the end of init function to utilise CPU instead. Recommended to use GPU.
from videoflow.processors.vision.detectors import ProcessorNode
from videoflow.utils.downloader import get_file

class YOLOv5Detector(ProcessorNode):

    def __init__(self, classes_to_detect = None, min_score_threshold = 0.5, model_type = 'YOLOv5s', nms_iou_threshold=0.5, custom_inference_size=None):
        
        '''
        Arguments
        classes_to_detect:
        Can pass a list of classes to detect. Optional.
        e.g. ['person', 'car'] --> Use labels from COCO dataset

        min_score_threshold:
        Set threshold above which detected boxes are shown. Default is set to 0.5. Highly dependent on use case.

        model_type:
        Models are from torch hub ultralytics.yolov5
        Model Types = ['YOLOv5s','YOLOv5m','YOLOv5l','YOLOv5x','YOLOv5s6','YOLOv5m6','YOLOv5l6','YOLOv5x6'] #All Working
        
        nms_iou_threshold:
        Non-Maximum Suppression Intersection Over Union Threshold.
        Default is 0.5. Can change based on circumstances. Generally leave unchanged.

        custom_inference_size:
        Default is None.
        Uses inference size based on model selected.
        Setting a custom inference size can have a significant negative impact on model accuracy. Only modify when required.
        '''

        self._custom_inference_size = custom_inference_size
        self._classes_to_detect = classes_to_detect
        self._model_type = model_type 
        self._min_score_threshold = min_score_threshold
        self._nms_iou_threshold = nms_iou_threshold
        self._YOLOv5_model = None
        super(YOLOv5Detector, self).__init__(nb_tasks = 1, device_type = GPU) #YOLOv5 can run on CPU but in the case of videoflow it is recommended it runs on the GPU
    
    def open(self):
        '''
        Creates YOLOv5 Model
        '''
        self._YOLOv5_model = torch.hub.load('ultralytics/yolov5', self._model_type.lower()) #Load model from torch hub
        
        self._YOLOv5_model.iou = self._nms_iou_threshold #Set Non Maximum Suppression Intersection Over Union Threshold. Generally should be left alone and the default value of 0.5 is used.
        
        '''
        If classes to detect is not passed, will return all detected bounding boxes above specified minimum score threshold irrespective of class label.
        Along with bounding box, class label is also returned so further sorting or class specific tasks can be performed based on class label.
        '''
        if self._classes_to_detect != None: 
            self._YOLOv5_model.classes = self._classes_to_detect #Sets sorting by classes. More efficienct than implementing by myself.
        #self._YOLOv5_model.conf = self._min_score_threshold #Method one to set minimum score threshold. See _detect function for method two.

    ''' Called at end when video pipeline is closed. '''
    def close(self):
        pass

    ''' Called after initialisation each time this part of the pipeline is reached. '''
    def _detect(self, im : np.array) -> np.array:
        '''
        - Arguments:
            - im (np.array): (h, w, 3)
        
        - Returns:
            - dets: np.array of shape (nb_boxes, 6) \
                Specifically (nb_boxes, [ymin, xmin, ymax, xmax, class_index, score])
        '''

        if self._custom_inference_size == None:
            results = self._YOLOv5_model(im)
        else:
            results = self._YOLOv5_model(im, size=self._custom_inference_size)
        res = results.pandas().xyxy[0] #Take pandas formatted output
        
        '''
        Extracting values to be sorted and returned.
        confidence represents confidence scores.
        class represents the class label the prediction belongs to.
        '''
        xmin = res['xmin'].to_numpy()
        ymin = res['ymin'].to_numpy()
        xmax = res['xmax'].to_numpy()
        ymax = res['ymax'].to_numpy()
        classes = res['class'].to_numpy()
        scores = res['confidence'].to_numpy()

        indices = np.where(scores > self._min_score_threshold)[0] #Method two to set minimum score threshold
        boxes, scores, classes = [ymin[indices], xmin[indices], ymax[indices], xmax[indices]], scores[indices], classes[indices]
        
        '''
        In order to concatenate all the different values together, we would need to modify the dimensions of the different sets of data.
        Potential Improvement #1
        '''
        scores, classes = np.expand_dims(scores, axis = 1), np.expand_dims(classes, axis = 1)
        boxes = np.transpose(boxes, axes=None)
        return np.concatenate((boxes, classes, scores), axis = 1)