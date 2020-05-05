import cv2
import numpy as np

cap = cv2.VideoCapture('src/tennis.mov')
cv2.namedWindow('img', cv2.WINDOW_NORMAL)
ret, frame = cap.read()
h, w, ch = frame.shape
frame_back = np.zeros((h, w, ch), dtype=np.float32)
while True:
    ret, frame = cap.read()
    if not ret:
        break
    frame_diff = cv2.absdiff(frame.astype(np.float32), frame_back)
    cv2.accumulateWeighted(frame, frame_back, 0.03)
    cv2.imshow('img', frame_diff.astype(np.uint8))
    if cv2.waitKey(10) == 27: # 27 is escape key
        break
cv2.destroyAllWindows()
cap.release()