# yolofive detector videoflow

This project is an addition to the videoflow contrib part of the videoflow open source library.

Videoflow repo: https://github.com/videoflow/videoflow

Videoflow contrib repo: https://github.com/videoflow/videoflow-contrib

# Why Videoflow?
The VF library uses multiprocessing, increasing efficiency and restricting frame rate of input video to the limiting factor module rather than the runtime of all the modules put together. Another way to bottleneck is by using a GPU with too little memory, especially when running high intensity modules like video action recogntion modules.

# Ways to use this project

## Way 1: Self-implementation
Create a pipeline using the videoflow library and then use my YOLOv5 module as a part of that pipeline.

## Way 2: Run Google Colab example

Once you run the colab, the output video that is annotated with bounding boxes taken from YOLOv5 can be found in the Videos folder (in the colab environment files) under the name "output.avi"

Click the Google Colab button below to go to the Colab.

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/drive/1kQkmGxvOz4QbjsPtZeJLDS9A_z6lb6KL)

### Modifying the Google Colab
You can modify the google colab code to perform different functions, i.e. add more modules and change the fundamental functionality with YOLOv5 just being one in a series of modules.

The easiest modification is to replace the youtube video being analysed. Simply change the youtube video url passed in code block 8, line 6. Be sure to run the output of code snippet `yt.streams.filter(file_extension='mp4')` first and select an appropriate ID tag (tag of any stream with mp4 format should work) and then change the tag ID value in `stream = yt.streams.get_by_itag(22)` where 22 is the ID tag
