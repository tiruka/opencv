# In this order of Corner > Edge > Flat, it includes more image features.
from copy import deepcopy
import cv2
import numpy as np


img = cv2.imread('img/dolphin.jpeg')
img_gray = cv2.imread('img/dolphin.jpeg', 0)

# Harris
img_harris = deepcopy(img)
img_dst = cv2.cornerHarris(img_gray, 2, 3, 0.04)
img_harris[img_dst > 0.02 * img_dst.max()] = [0, 0, 255]
cv2.imshow('harris', img_harris)


# kaze
img_kaze = deepcopy(img)
kaze = cv2.KAZE_create()
kp1 = kaze.detect(img, None)
img_kaze = cv2.drawKeypoints(img_kaze, kp1, None)
cv2.imshow('kaze', img_kaze)


# A-kaze
img_akaze = deepcopy(img)
akaze = cv2.AKAZE_create()
kp2 = kaze.detect(img, None)
img_akaze = cv2.drawKeypoints(img_akaze, kp2, None)


# Orb
img_orb = deepcopy(img)
orb = cv2.ORB_create()
t = orb.detect(img, None)
img_orb = cv2.drawKeypoints(img_orb, t, None)
cv2.imshow('orb', img_orb)

cv2.waitKey(0)
cv2.destroyAllWindows()