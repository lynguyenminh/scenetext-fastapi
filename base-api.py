# from fastapi import FastAPI
# import uvicorn
# from load_model import load_model_yolov8


# # khoi tao api
# app = FastAPI()


# # load model
# model = load_model_yolov8()



# @app.get("/api/v1/yolov8")  # Define the endpoint and specify the image_name as a path parameter
# async def get_image_values(image_path: str, threshold: float):    
#     raw_information_predict = model.predict(source=image_path, conf=threshold)
#     boxes = [coordinate[0].cpu().numpy().astype(int) for coordinate in zip(raw_information_predict[0].boxes.xyxy)]
#     boxes = [x.tolist() for x in boxes]
#     boxes = [[[box[0], box[1]], [box[2], box[1]], [box[2], box[3]], [box[0], box[3]]] for box in boxes]
#     return {"bounding_box": boxes} 


# if __name__ == "__main__":
#     uvicorn.run(app, host="0.0.0.0", port=4001)

# # CMD ["python3", "app.py"]
# # http://0.0.0.0:4001/api/v1/yolov8?image_path=test_img.jpg&threshold=0.5