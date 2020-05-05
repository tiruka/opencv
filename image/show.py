# show image and destroy it after entering any key.
import cv2

img = cv2.imread('src/dolphin.jpeg')


# resize
size = (200, 300)
img_area = cv2.resize(img, size, interpolation=cv2.INTER_AREA)
img_linear = cv2.resize(img, size, interpolation=cv2.INTER_LINEAR)

cv2.imshow('img', img)
cv2.imshow('img_area', img_area)
cv2.imshow('img_linear', img_linear)
cv2.waitKey(0)
cv2.destroyAllWindows()
