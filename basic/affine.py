import cv2
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread('img/dolphin.jpeg', 0)
h, w = img.shape[:2]
dx, dy = 30, 30

afn_mat = np.float32([[1, 0, dx], [0, 1, dy]])
img_afn = cv2.warpAffine(img, afn_mat, (w, h))
cv2.imshow('transport', img_afn)

rot_mat = cv2.getRotationMatrix2D((w / 2, h / 2), 40, 1)
img_afn_2 = cv2.warpAffine(img, rot_mat, (w, h))
cv2.imshow('rotate', img_afn_2)

cv2.waitKey(0)
cv2.destroyAllWindows()