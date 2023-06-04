import torch
from PIL import Image

from vietocr.tool.config import Cfg
from vietocr.tool.predictor import Predictor



class parseq_text_recognition: 
    def __init__(self):
        self.base_config = 'vgg_transformer'
        self.device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
        self.vocab = 'aAàÀảẢãÃáÁạẠăĂằẰẳẲẵẴắẮặẶâÂầẦẩẨẫẪấẤậẬbBcCdDđĐeEèÈẻẺẽẼéÉẹẸêÊềỀểỂễỄếẾệỆfFgGhHiIìÌỉỈĩĨíÍịỊjJkKlLmMnNoOòÒỏỎõÕóÓọỌôÔồỒổỔỗỖốỐộỘơƠờỜởỞỡỠớỚợỢpPqQrRsStTuUùÙủỦũŨúÚụỤưƯừỪửỬữỮứỨựỰvVwWxXyYỳỲỷỶỹỸýÝỵỴzZ0123456789!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~° ' + '̉'+ '̀' + '̃'+ '́'+ '̣'
        self.trained_model = 'VietOCR-best.pth'
        self.detector = self._load_model()


    def _load_model(self):
        config = Cfg.load_config_from_name(self.base_config)
        config['device'] = self.device
        config['vocab'] = self.vocab
        config['weights'] = self.trained_model
        detector = Predictor(config)
        return detector

    def inference(self, image) -> tuple:
        # image = Image.open(image).convert('RGB')
        pred, prob = self.detector.predict(image , return_prob = True)
        return pred
    
if __name__=="__main__":
    parseq_instance = parseq_text_recognition()
    print(parseq_instance.inference("test-case.png"))