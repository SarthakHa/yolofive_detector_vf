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
[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/drive/1kQkmGxvOz4QbjsPtZeJLDS9A_z6lb6KL]
