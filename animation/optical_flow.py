import cv2
import numpy as np

cap = cv2.VideoCapture('src/animation.mp4')
cv2.namedWindow('img', cv2.WINDOW_NORMAL)

count = 500
criteria = (cv2.TERM_CRITERIA_MAX_ITER | cv2.TERM_CRITERIA_EPS, 20, 0.05)
params = {'winSize': (10, 10), 'maxLevel': 4, 'criteria': criteria}
ret, frame = cap.read()
frame_pre = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
while True:
    ret, frame = cap.read()
    if not ret:
        break
    frame_cur = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    feature_pre = cv2.goodFeaturesToTrack(frame_pre, count, 0.001, 5)
    if feature_pre is None:
        continue
    feature_cur, status, err = cv2.calcOpticalFlowPyrLK(frame_pre, frame_cur, feature_pre, None, **params)
    for i in range(count):
        pre_x = feature_pre[i][0][0]
        pre_y = feature_pre[i][0][1]
        cur_x = feature_cur[i][0][0]
        cur_y = feature_cur[i][0][1]
        cv2.line(frame, (pre_x, pre_y), (cur_x, cur_y), (255, 0, 0), 3)
    cv2.imshow('img', frame)
    frame_pre = frame_cur.copy()
    if cv2.waitKey(10) == 27: # 27 is escape key
        break
cv2.destroyAllWindows()
cap.release()