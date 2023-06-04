import cv2
import torch
import torch.backends.cudnn as cudnn
from torch.autograd import Variable

from craft import CRAFT
from refinenet import RefineNet
from collections import OrderedDict
import craft_utils, imgproc





text_threshold = 0.7
low_text = 0.4
link_threshold = 0.4 
canvas_size = 1280
mag_ratio = 1.5
poly = False


class craft_text_detection:
    def __init__(self):
        self.device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
        self.refine = False
        self.trained_model = 'craft_mlt_25k.pth'
        self.refiner_model = 'craft_refiner_CTW1500.pth'
        self.net, self.refine_net = self._load_model()
        self.threshold = 0.7

    def _load_model(self):
        net = CRAFT()

        # choose cuda or cpu
        if self.device == 'cuda':
            net.load_state_dict(self.copyStateDict(torch.load(self.trained_model)))
        else:
            net.load_state_dict(self.copyStateDict(torch.load(self.trained_model, map_location='cpu')))

        if self.device == 'cuda':
            net = net.cuda()
            net = torch.nn.DataParallel(net)
            cudnn.benchmark = False

        net.eval()

        # LinkRefiner
        refine_net = None
        if self.refine:
            refine_net = RefineNet()
            if self.device == 'cuda':
                refine_net.load_state_dict(self.copyStateDict(torch.load(self.refiner_model)))
                refine_net = refine_net.cuda()
                refine_net = torch.nn.DataParallel(refine_net)
            else:
                refine_net.load_state_dict(self.copyStateDict(torch.load(self.refiner_model, map_location='cpu')))

            refine_net.eval()

        return net, refine_net

    def copyStateDict(self, state_dict):
        if list(state_dict.keys())[0].startswith("module"):
            start_idx = 1
        else:
            start_idx = 0
        new_state_dict = OrderedDict()
        for k, v in state_dict.items():
            name = ".".join(k.split(".")[start_idx:])
            new_state_dict[name] = v
        return new_state_dict

    def feed_forward(self, image, threshold):
        # resize
        img_resized, target_ratio, _ = imgproc.resize_aspect_ratio(image, canvas_size, interpolation=cv2.INTER_LINEAR, mag_ratio=mag_ratio)
        ratio_h = ratio_w = 1 / target_ratio

        # preprocessing
        x = imgproc.normalizeMeanVariance(img_resized)
        x = torch.from_numpy(x).permute(2, 0, 1)    # [h, w, c] to [c, h, w]
        x = Variable(x.unsqueeze(0))                # [c, h, w] to [b, c, h, w]
        if self.device == 'cuda':
            x = x.cuda()

        # forward pass
        with torch.no_grad():
            y, feature = self.net(x)

        # make score and link map
        score_text = y[0,:,:,0].cpu().data.numpy()
        score_link = y[0,:,:,1].cpu().data.numpy()

        # refine link
        if self.refine_net is not None:
            with torch.no_grad():
                y_refiner = self.refine_net(y, feature)
            score_link = y_refiner[0,:,:,0].cpu().data.numpy()

        # Post-processing
        boxes, polys = craft_utils.getDetBoxes(score_text, score_link, threshold, link_threshold, low_text, poly)

        # coordinate adjustment
        boxes = craft_utils.adjustResultCoordinates(boxes, ratio_w, ratio_h)
        polys = craft_utils.adjustResultCoordinates(polys, ratio_w, ratio_h)
        for k in range(len(polys)):
            if polys[k] is None: polys[k] = boxes[k]

        return polys

    def inference(self, image_path, threshold=0.7):
        image_path = imgproc.loadImage(image_path)
        polys = self.feed_forward(image_path, threshold=threshold)
        polys = [i.tolist() for i in polys]
        polys = [[[int(num) for num in sublist] for sublist in inner_list] for inner_list in polys]

        boxes = []
        for box in polys: 
            x_coordinates, y_coordinates = zip(*box)
            top = min(y_coordinates)
            left = min(x_coordinates)
            bot = max(y_coordinates)
            right = max(x_coordinates)

            boxes.append([left, top, right, bot])

        return boxes


if __name__=="__main__":
    craft_instance = craft_text_detection()
    print(craft_instance.inference('test-case.jpg'))