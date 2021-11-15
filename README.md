# yolofive detector videoflow

This project is an addition to the videoflow contrib part of the videoflow open source library.

Videoflow repo: https://github.com/videoflow/videoflow

Videoflow contrib repo: https://github.com/videoflow/videoflow-contrib

# Quick Start

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/drive/1kQkmGxvOz4QbjsPtZeJLDS9A_z6lb6KL)

__Run this colab and then download the 'output.avi' file in under the videos folder in the colab environment.__

# Demo

### YOLOv5 --> Bounding Box Annotator --> BRG to RGB Color Fix

![YOLOv5 VF Module Output](https://www.dropbox.com/s/kkvztrlmo92mbio/yolofivemoduleoutput.gif)

# Why create a module for Videoflow?
The VF library uses multiprocessing, increasing efficiency and restricting frame rate of input video to the limiting factor module rather than the runtime of all the modules put together. This allows for better use of computer resources. 

Furthmore, the VF library uses a modularised design where modules can be used in a plug n play style manner. For example, different Object Detector modules can be switched out for each other without much hassle, allowing prototyping to take place quickly.

Although modularity is central to the VF library, there isn't a module for every single different possible attachment to the pipeline, hence I decided to create my own module for an advanced object detection model. A different module exists for the older yolov3, however, none for the YOLOv4 or YOLOv5. Considering that YOLOv5 is more standard nowadays, I decided to implement one for YOLOv5.

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
