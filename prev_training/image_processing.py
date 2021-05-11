from imageio import imread, imwrite
import os
import numpy as np
import cv2
import matplotlib.pyplot as plt

path = "C:/Users/default.DESKTOP-DBP44Q5/Desktop/filtered/label_coarse"

for item in os.listdir(path):
    print(item)

    img = imread(os.path.join(path, item), pilmode="L")
    H, W = img.shape

    gap = (np.max((H, W)) - np.min((H, W))) // 2

    img = img[gap:gap + np.min((H, W)), gap:gap + np.min((H, W))]
    img = cv2.resize(img, (512, 512))

    imwrite(os.path.join(path, item), img)
