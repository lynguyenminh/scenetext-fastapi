# scenetext-api

## 1. Introduction
In this code, I have built an API for text detection and text recognition tasks using the following technologies:
- FastAPI
- Docker

Having participated in various OCR competitions and gained significant experience, I am confident in providing self-fine-tuned weights for the models.

This repository is a support for https://github.com/lynguyenminh/vietnamese-scenetext-detection-recognition.

## 2. Installation

I provide 4 APIs: yolov8, craft, vietocr, parseq. For each model, the installation process is the same. Follow the instructions below:

### 1. Download weights
After cloning the source code, navigate to the source code directory, then run:
```
sh download_models.sh
```

### 2. Build Docker images
To build the image for yolo, follow these steps:
```
cd detection/yolov8
sh run.sh
```

### 3. Run container and test the API
After successfully building the images, run the container as follows:
```
docker run -it --name test_yolov8_dockerimage2 -p 4001:4001 -v ./:/yolov8 yolov8_scenetext_orai:v1
```

Then, test the API using the command:
```
python request_api.py
```
