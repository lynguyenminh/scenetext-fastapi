from fastapi import FastAPI, File, UploadFile
from PIL import Image
from io import BytesIO
from typing import List


from src import yolov8_text_detection

app = FastAPI()

yolov8_instance = yolov8_text_detection(model_path="model_yolov8.pt", threshold=0.5)



@app.post("/api/detection/yolov8/")
async def create_upload_file(file: UploadFile = File(...)):
    contents = await file.read()
    image = Image.open(BytesIO(contents)).convert('L') # convert to grayscale 
    boxes = yolov8_instance.inference(image=image)
    return {"boxes": boxes}