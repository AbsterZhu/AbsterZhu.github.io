import cv2
import numpy as np

image_path = '/Users/abster/workspace/AbsterZhu.github.io/images/medlego.png'
# load alpha channel
img = cv2.imread(image_path)


h,w = img.shape[:2]

ration = 1000 / 600
if w/h > ration:
    new_w = w
    new_h = int(w/ration)
    
    new_img = np.ones((new_h, new_w, 3), np.uint8) * 255
    # center fill
    start = (new_h - h) // 2
    new_img[start:start+h, :] = img
else:
    new_h = h
    new_w = int(h * ration)
    
    new_img = np.ones((new_h, new_w, 3), np.uint8) * 255
    # center fill
    start = (new_w - w) // 2
    new_img[:, start:start+w] = img


new_img = cv2.resize(new_img, (1000, 600), interpolation=cv2.INTER_CUBIC)
cv2.imwrite(image_path.replace(".png", "_new.png"), new_img)

