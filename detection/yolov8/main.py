from ultralytics import YOLO
import cv2


class yolov8_text_detection:
    def __init__(self, model_path, threshold):
        self.model_path = model_path
        self.model = self._load_model()
        self.threshold = threshold
    
    def _load_model(self):
        model = YOLO(self.model_path)
        return model
    
    def inference(self, image):
        '''
        image: Duong dan den anh test hoac anh test da duoc doc bang opencv
        '''
        raw_information_predict = self.model.predict(source=image, conf=self.threshold)
        boxes = [coordinate[0].cpu().numpy().astype(int) for coordinate in zip(raw_information_predict[0].boxes.xyxy)]
        return boxes
    



if __name__=="__main__":
    yolov8_instance = yolov8_text_detection(model_path="model_yolov8.pt", threshold=0.5)
    # boxes = yolov8_instance.inference_with_imgpath(img_path="test-case.jpg")
    # print(boxes)
    # img = cv2.imread('test-case.jpg')
    # boxes = yolov8_instance.inference_with_opencvimg(img)
    # print(boxes)