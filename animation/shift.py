import cv2
import numpy as np

cap = cv2.VideoCapture('src/tennis.mov')
# ret, frame = cap.read()
# h, w, ch = frame.shape

cv2.namedWindow('img', cv2.WINDOW_NORMAL)
# cv2.resize('img', 1200, 800)
rct = (990, 600, 100, 100)
cri = (cv2.TERM_CRITERIA_COUNT | cv2.TERM_CRITERIA_EPS, 10, 1)

while True:
    threshold = 100
    ret, frame = cap.read()
    if not ret:
        break
    img_gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    _, img_bin = cv2.threshold(img_gray, threshold, 255, cv2.THRESH_BINARY)
    # _, rct = cv2.meanShift(img_bin, rct, cri)
    _, rct = cv2.CamShift(img_bin, rct, cri)
    x, y, w, h = rct
    frame = cv2.rectangle(frame, (x, y), (w + x, h + y), (255, 0, 0), 3)
    cv2.imshow('img', frame)
    if cv2.waitKey(10) == 27: # 27 is escape key
        break
cv2.destroyAllWindows()
cap.release()