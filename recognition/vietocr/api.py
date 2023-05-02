from fastapi import FastAPI, File, UploadFile
from PIL import Image
from io import BytesIO
from src import parseq_text_recognition



app = FastAPI()

vietocr_instance = parseq_text_recognition()


@app.post("/api/recognition/vietocr/")
async def create_upload_file(file: UploadFile = File(...), 
                             coordinates: list = []):
    contents = await file.read()
    coordinates = [int(x) for x in coordinates]

    image = Image.open(BytesIO(contents)).convert('RGB') # convert to grayscale 
    sub_img = image.crop((coordinates[0], coordinates[1], coordinates[2], coordinates[3]))
    text = vietocr_instance.inference(sub_img)

    return {"text": text}