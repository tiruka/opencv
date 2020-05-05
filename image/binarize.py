# binarization of black and white
import cv2
import matplotlib.pyplot as plt

img = cv2.imread('src/dolphin.jpeg', 0)

threshold = 100
ret, img_th = cv2.threshold(img, threshold, 255, cv2.THRESH_BINARY)
cv2.imshow('th', img_th)

# auto by otsu
ret, img_o = cv2.threshold(img, 0, 255, cv2.THRESH_OTSU)
cv2.imshow('otsu', img_o)

# adaptive threshold
img_ad = cv2.adaptiveThreshold(img, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 3, 1)
cv2.imshow('adaptive', img_ad)
cv2.waitKey(0)
cv2.destroyAllWindows()