# yolofive detector videoflow

This project is an addition to the videoflow contrib part of the videoflow open source library.

Videoflow repo: https://github.com/videoflow/videoflow
Videoflow contrib repo: https://github.com/videoflow/videoflow-contrib

In order to use this project, you would need to create a pipeline using the videoflow library and then use my YOLOv5 module as a part of that pipeline.

The VF library uses multiprocessing, increasing efficiency and restricting frame rate of input video to the limiting factor module rather than the runtime of all the modules put together. Another way to bottleneck is by using a GPU with too little memory, especially when running high intensity modules like video action recogntion modules.
