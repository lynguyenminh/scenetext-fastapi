from fastapi import FastAPI, File, UploadFile
from PIL import Image
from io import BytesIO
from typing import List


from src import craft_text_detection

app = FastAPI()

craft_instance = craft_text_detection()



@app.post("/api/detection/craft/")
async def create_upload_file(file: UploadFile = File(...)):
    contents = await file.read()
    image = Image.open(BytesIO(contents)).convert('L') # convert to grayscale 
    boxes = craft_instance.inference(image_path=image)
    return {"boxes": boxes}