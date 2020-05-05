import cv2

haar_file = 'etc/haarcascade_frontalface_default.xml'
cascade = cv2.CascadeClassifier(haar_file)

img = cv2.imread('img/gather.jpg')
img_gray = cv2.imread('img/gather.jpg', 0)


face = cascade.detectMultiScale(img_gray)

for x, y, w, h in face:
    cv2.rectangle(img, (x, y), (x + w, y + h), (0, 0, 255), 1)

cv2.imshow('o', img_gray)
cv2.imshow('face', img)
cv2.waitKey(0)
cv2.destroyAllWindows()