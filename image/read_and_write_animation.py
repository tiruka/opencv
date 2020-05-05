import os
# read animation and write out the same.
import sys
import cv2

video = cv2.VideoCapture('img/animation.mp4')
if video.isOpened():
    ret, frame = video.read()
    h, w = frame.shape[:2]
    fourcc = cv2.VideoWriter_fourcc(*'XVID')
    dst = cv2.VideoWriter('img/output.mp4', fourcc, 30., (w, h))
    while True:
        ret, frame = video.read()
        if not ret:
            break
        cv2.imshow('img', frame)
        dst.write(frame)
        if cv2.waitKey(30) == 27: # 27 is escape key
            break
    cv2.destroyAllWindows()
    video.release()
else:
    sys.exit()