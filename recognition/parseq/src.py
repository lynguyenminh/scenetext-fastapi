import torch
import statistics
from PIL import Image

from strhub.data.module import SceneTextDataModule
from strhub.models.utils import load_from_checkpoint



class parseq_text_recognition: 
    def __init__(self):
        self.device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
        self.trained_model = 'parseq_model.ckpt'
        self.parseq, self.img_transform = self._load_model()
        self.threshold = 0.7
        
    def _load_model(self):
        parseq = load_from_checkpoint(self.trained_model).eval().to(self.device)
        img_transform = SceneTextDataModule.get_transform(parseq.hparams.img_size)
        return parseq, img_transform
    
    def predict(self, image):
        # image = Image.open(image).convert('RGB')
        image = self.img_transform(image).unsqueeze(0).to(self.device)

        p = self.parseq(image).softmax(-1)
        pred, p = self.parseq.tokenizer.decode(p)

        return pred[0]
    
    
if __name__=="__main__":
    parseq_instance = parseq_text_recognition()
    print(parseq_instance.predict('test-case.png'))