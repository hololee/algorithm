from imageio import imread, imwrite
import os
import numpy as np
import cv2
import matplotlib.pyplot as plt

path = "C:/Users/default.DESKTOP-DBP44Q5/Desktop/paprika_disease/label_fine"

for item in os.listdir(path):
    print(item)

    img = imread(os.path.join(path, item), pilmode="L")

    img[np.where(img < 255)] = 0

    imwrite(os.path.join(path, item), img)
