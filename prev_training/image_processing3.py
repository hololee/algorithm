import cv2 as cv
import numpy as np



img = cv.imread('D:/paprika_disease/label_coarse/graymold_0047.png')
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
ret, thresh = cv.threshold(gray, 0, 255, cv.THRESH_BINARY + cv.THRESH_OTSU)


# 이진화된 결과를 dist_transform 함수의 입력으로 사용합니다.

dist_transform = cv.distanceTransform(thresh, cv.DIST_L2, 5)
# dist_transform  함수를 사용하면 실수 타입(float32)의 이미지가 생성됩니다. 화면에 보여주려면 normalize 함수를 사용해야 합니다.
result = cv.normalize(dist_transform, None, 255, 0, cv.NORM_MINMAX, cv.CV_8UC1)

cv.imshow("dist_transform", result)
cv.imshow("src", img)

cv.waitKey(0)