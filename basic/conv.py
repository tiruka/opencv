import cv2
import numpy as np

img = cv2.imread('img/dolphin.jpeg')

kernel = np.ones((3, 3)) / 9.
img_ke = cv2.filter2D(img, -1, kernel)
cv2.imshow('conv', img_ke)

# skernel (3, 3) and blut is the same
img_blur = cv2.blur(img, (3, 3))
cv2.imshow('blur', img_blur)

# gaussian filter
img_ga = cv2.GaussianBlur(img, (9, 9), 2)
cv2.imshow('gaussian', img_ga)

# median filter
img_me = cv2.medianBlur(img, 5)
cv2.imshow('median', img_me)

# bilateral filter
img_bi = cv2.bilateralFilter(img, 20, 30, 30)
cv2.imshow('bilateral', img_bi)

cv2.waitKey(0)
cv2.destroyAllWindows()