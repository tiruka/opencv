# Dervative leads to inspect edge
# incline = adjacant value　- the value
import cv2
import numpy as np

img = cv2.imread('img/dolphin.jpeg')
# sobel filter
img_sobel_x = cv2.Sobel(img, cv2.CV_32F, 1, 0, ksize=3)
img_sobel_x = cv2.convertScaleAbs(img_sobel_x)

img_sobel_y = cv2.Sobel(img, cv2.CV_32F, 0, 1, ksize=3)
img_sobel_y = cv2.convertScaleAbs(img_sobel_y)

cv2.imshow('x', img_sobel_x)
cv2.imshow('y', img_sobel_y)

# Laplacian filter
img_lap = cv2.Laplacian(img, cv2.CV_32F)
img_lap = cv2.convertScaleAbs(img_lap)
cv2.imshow('laplacian', img_lap)


# Laplacian and gaussian filter
img_ga = cv2.GaussianBlur(img, (3, 3), 2)
img_lap_ga = cv2.Laplacian(img_ga, cv2.CV_32F)
img_lap_ga = cv2.convertScaleAbs(img_lap_ga) * 2
cv2.imshow('laplacian_gaussian', img_lap_ga)


# Canny filter
img_ca = cv2.Canny(img, 100, 200)
cv2.imshow('canny', img_ca)

cv2.waitKey(0)
cv2.destroyAllWindows()