from fastapi import FastAPI, File, UploadFile
import requests
from sort_bb import sort_bounding_boxes

app = FastAPI()


# api cho yolo vaf parseq
@app.post("/ocr/yolo_parseq/")
async def ocr(image: UploadFile = File(...)):
    image_bytes = await image.read()

    # Gửi ảnh đến container detection
    detection_url = "http://0.0.0.0:4001/api/detection/yolov8/"
    detection_response = requests.post(detection_url, json={"image": image_bytes})

    # # Lấy tọa độ của văn bản từ detection
    # coordinates = detection_response.json()["coordinates"]
    # print(coordinates)
    return {'result': 1}

    # # Sort các bounding box
    # coordinates = sort_bounding_boxes(coordinates, threshold=20)

    # # Gửi ảnh và tọa độ đến container recognition
    # recognition_url = "http://0.0.0.0:4003/api/recognition/parseq/"
    # recognition_response = requests.post(recognition_url, files={"image": image_bytes}, data=coordinates)

    # # Trả về kết quả OCR là một string
    # return recognition_response.text


# # api cho yolo vaf vietocr
# @app.post("/ocr/yolo_vietocr/")
# async def ocr(image: UploadFile = File(...)):
#     image_bytes = await image.read()

#     # Gửi ảnh đến container detection
#     detection_url = "http://0.0.0.0:4001/api/detection/yolov8/"
#     detection_response = requests.post(detection_url, files={"image": image_bytes})

#     # Lấy tọa độ của văn bản từ detection
#     coordinates = detection_response.json()["coordinates"]

#     # Sort các bounding box
#     coordinates = sort_bounding_boxes(coordinates, threshold=20)

#     # Gửi ảnh và tọa độ đến container recognition
#     recognition_url = "http://0.0.0.0:4004/api/recognition/vietocr/"
#     recognition_response = requests.post(recognition_url, files={"image": image_bytes}, data=coordinates)

#     # Trả về kết quả OCR là một string
#     return recognition_response.text


# # api cho craft vaf parseq
# @app.post("/ocr/craft_parseq/")
# async def ocr(image: UploadFile = File(...)):
#     image_bytes = await image.read()

#     # Gửi ảnh đến container detection
#     detection_url = "http://0.0.0.0:4002/api/detection/craft/"
#     detection_response = requests.post(detection_url, files={"image": image_bytes})

#     # Lấy tọa độ của văn bản từ detection
#     coordinates = detection_response.json()["coordinates"]

#     # Sort các bounding box
#     coordinates = sort_bounding_boxes(coordinates, threshold=20)

#     # Gửi ảnh và tọa độ đến container recognition
#     recognition_url = "http://0.0.0.0:4003/api/recognition/parseq/"
#     recognition_response = requests.post(recognition_url, files={"image": image_bytes}, data=coordinates)

#     # Trả về kết quả OCR là một string
#     return recognition_response.text


# # api cho craft vaf vietocr
# @app.post("/ocr/yolo_vietocr/")
# async def ocr(image: UploadFile = File(...)):
#     image_bytes = await image.read()

#     # Gửi ảnh đến container detection
#     detection_url = "http://0.0.0.0:4002/api/detection/craft/"
#     detection_response = requests.post(detection_url, files={"image": image_bytes})

#     # Lấy tọa độ của văn bản từ detection
#     coordinates = detection_response.json()["coordinates"]

#     # Sort các bounding box
#     coordinates = sort_bounding_boxes(coordinates, threshold=20)
    
#     # Gửi ảnh và tọa độ đến container recognition
#     recognition_url = "http://0.0.0.0:4004/api/recognition/vietocr/"
#     recognition_response = requests.post(recognition_url, files={"image": image_bytes}, data=coordinates)

#     # Trả về kết quả OCR là một string
#     return recognition_response.text