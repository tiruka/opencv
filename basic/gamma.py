# gamma convert to change brightness
import cv2
import numpy as np

gamma = 0.4 # over 1 -> more bright, under 1 darker
img = cv2.imread('img/dolphin.jpeg')
gammva_cvt = np.zeros((256, 1), dtype=np.uint8)
for i in range(256):
    gammva_cvt[i][0] = 255 * (float(i) / 255) ** (1.0 / gamma)

img_gamma = cv2.LUT(img, gammva_cvt)
cv2.imshow('original', img)
cv2.imshow('gamma', img_gamma)
cv2.waitKey(0)
cv2.destroyAllWindows()