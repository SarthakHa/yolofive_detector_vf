# YOLOv5 Detector Module Videoflow (VF) Addition

This project is an addition to the videoflow contrib part of the videoflow open source library.

Videoflow repo: https://github.com/videoflow/videoflow

Videoflow contrib repo: https://github.com/videoflow/videoflow-contrib

# Quick Start

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/drive/1kQkmGxvOz4QbjsPtZeJLDS9A_z6lb6KL)

__Run this colab and then download the 'output.avi' file that can be found in `Files > Content > Videos` in the colab environment.__

If you have not used Colab before, run by going to the Runtime tab in the top toolbar and clicking Run all, `Runtime > Run all`

Note: Ensure that the runtime is of GPU type. This setting can be found under the Runtime tab in the top toolbar, `Runtime > Change runtime type > Hardware accelerator > GPU`


# Demo

### YOLOv5 --> Bounding Box Annotator --> BRG to RGB Color Fix

| Plain Video | After going through VF with our YOLOv5 Module |
|------------------------------------------------------------------------|-------------------------------------------------------------------------|
|![Plain Video](https://i.postimg.cc/VNpwg1DN/plain-Video.gif) | ![YOLOv5 VF Module Output](https://i.postimg.cc/bvStvy50/secondgif.gif) |

### YOLOv5 --> Bounding Box Tracker --> Obfuscator --> BRG to RGB Color Fix

| Plain Video | After going through VF with our YOLOv5 Module and then an Obfuscator |
|------------------------------------------------------------------------|-------------------------------------------------------------------------|
|![Plain Video](https://i.postimg.cc/h4y9D5y0/plain-Video2.gif) | ![YOLOv5 VF Module Output](https://i.postimg.cc/BndpqVvz/Obfuscator-Output.gif) |

# Why create a module for Videoflow?
The VF library uses multiprocessing, increasing efficiency and restricting frame rate of input video to the limiting factor module rather than the runtime of all the modules put together. This allows for better use of computer resources. 

Furthmore, the VF library uses a modularised design where modules can be used in a plug n play style manner. For example, different Object Detector modules can be switched out for each other without much hassle, allowing prototyping to take place quickly.

Although modularity is central to the VF library, there isn't a module for every single different possible attachment to the pipeline, hence I decided to create my own module for an advanced object detection model. A different module exists for the older yolov3, however, none for the YOLOv4 or YOLOv5. Considering that YOLOv5 is more standard nowadays, I decided to implement one for YOLOv5.

# Ways to use this project

## Way 1: Self-implementation
Create a pipeline using the videoflow library and then use my YOLOv5 module as a part of that pipeline.

## Way 2: Run Google Colab(s)

Once you run the colab, the output video that is annotated with bounding boxes taken from YOLOv5 can be found in the Videos folder (in the colab environment files) under the name "output.avi"

There are different Colabs available

Click the respective Google Colab button below to go to the Colab.

| YOLOv5 Bounding Box Overlay | YOLOv5 Obfuscate non-detected areas |
|--|--|
| [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/drive/1kQkmGxvOz4QbjsPtZeJLDS9A_z6lb6KL) | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/drive/1LeIbwzym1RgrCkxbVQtAUu5Q3px7AUti?usp=sharing) | 

### Modifying the Google Colab
You can modify the google colab code to perform different functions, i.e. add more modules and change the fundamental functionality with YOLOv5 just being one in a series of modules.

The easiest modification is to replace the youtube video being analysed.

Locate the code block in colab that deals with the YouTube video (it should contain `from pytube import YouTube` at the top of the block).

Next, change the link variable to the URL of whichever YouTube video you want to run the program on.

This should do it in most cases. In extremely rare cases, however, you will need to run the next code block `yt.streams.filter(file_extension='mp4')`, read its output, choose any ID tag number which is written as `itag` (primary difference is in video quality) and then change the ID tag number in the next block accordingly. The next block would look something like this:

```
stream = yt.streams.get_by_itag(YOUR CHOSEN TAG NUMBER HERE)
stream.download(filename="savedVid.mp4")
```
