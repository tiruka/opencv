import cv2
import numpy as np

cap = cv2.VideoCapture('src/animation.mp4')
while True:
    cv2.namedWindow('img', cv2.WINDOW_NORMAL)
    # cv2.resize('img', 640, 480)
    ret, frame = cap.read()
    if not ret:
        break
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    lower = np.array([20, 50, 50])
    upper = np.array([25, 255, 255])
    frame_mask = cv2.inRange(hsv, lower, upper)
    dst = cv2.bitwise_and(frame, frame, mask=frame_mask)
    cv2.imshow('img', dst)
    if cv2.waitKey(30) == 27: # 27 is escape key
        break
cv2.destroyAllWindows()
cap.release()