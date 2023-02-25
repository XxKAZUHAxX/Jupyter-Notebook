import cv2
import numpy as np

def draw_circle(event, x, y, flags, param):
    if event == cv2.EVENT_LBUTTONDOWN:
        cv2.circle(img=img, center=(x, y), radius=25, color=(0, 255, 0), thickness=-1)

cv2.namedWindow('image')
cv2.setMouseCallback('image', draw_circle)

img = np.zeros((1000, 1000, 3), np.uint8)

while True:
    cv2.imshow('image', img)
    if cv2.waitKey(1) & 0xFF == 27:
        break
cv2.destroyAllWindows()