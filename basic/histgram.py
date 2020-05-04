# histgram
import cv2
import matplotlib.pyplot as plt

img = cv2.imread('img/dolphin.jpeg')

color = ['blue', 'green', 'red']

for i in range(len(color)):
    hist = cv2.calcHist([img], [i], None, [256], [0, 256])
    plt.plot(hist, color=color[i])
plt.show()

# gray scale
img_gray = cv2.imread('img/dolphin.jpeg', 0)
hist_gray = cv2.calcHist([img_gray], [0], None, [256], [0, 256])
plt.plot(hist_gray)
plt.show()

# normalized gray scale
img_eq = cv2.equalizeHist(cv2.imread('img/dolphin.jpeg', 0))
hist_eq = cv2.calcHist([img_eq], [0], None, [256], [0, 256])
plt.plot(hist_eq)
plt.show()
