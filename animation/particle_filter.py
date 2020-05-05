from random import choices
import cv2
import numpy as np

def likelihood(img, px, py, obj_value, NP, sigma2=0.01):
    likelihood_arr = []
    for i in range(NP):
        b = (img[py[i],px[i]][0] - obj_value[0]) / 255.
        g = (img[py[i],px[i]][1] - obj_value[1]) / 255.
        r = (img[py[i],px[i]][2] - obj_value[2]) / 255.
        likelihood = np.exp(-(r ** 2 + g ** 2 + b ** 2 ) / (2 * sigma2))
        likelihood_arr.append(likelihood)
    return likelihood_arr

cap = cv2.VideoCapture('src/animation.mp4')
cv2.namedWindow('img', cv2.WINDOW_NORMAL)

ret, frame = cap.read()
h, w = frame.shape[:2]
np.random.seed(0)
NP = 500 # number of particles
px = np.zeros((NP), dtype=np.int64)
py = np.zeros((NP), dtype=np.int64)
lp = np.zeros((NP), dtype=np.int64)

for i in range(NP):
    # scatter particles randomly
    px[i] = int(np.random.uniform(0, w))
    py[i] = int(np.random.uniform(0, h))

target = [0, 100, 200] # target RGB
while True:
    ret, frame = cap.read()
    if not ret:
        break
    lp = likelihood(frame, px, py, target, NP, sigma2=0.001)
    # random walk
    next_px = np.array(choices(population=px, weights=lp, k=NP)) + np.random.randint(-15, 15, NP)
    next_py = np.array(choices(population=py, weights=lp, k=NP)) + np.random.randint(-15, 15, NP)
    # inside frame
    px = np.where(next_px > w - 1, w - 1, next_px)
    py = np.where(next_py > h - 1, h - 1, next_py)
    px = np.where(px < 0, 0, px)
    py = np.where(py < 0, 0, py)
    for i in range(NP):
        cv2.circle(frame, (px[i], py[i]), 1, (255, 0, 0), 30)
    cv2.imshow('img', frame)
    if cv2.waitKey(10) == 27: # 27 is escape key
        break
cv2.destroyAllWindows()
cap.release()