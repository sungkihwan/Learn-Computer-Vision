import cv2
import numpy as np
import matplotlib.pyplot as plt

def draw_circle(event,x,y,flags,param):
    # 마우스 왼쪽 버튼 클릭하면 동작
    if event == cv2.EVENT_LBUTTONDOWN:
        cv2.circle(img,(x,y),100,(0,255,0),-1)

# 검은색 이미지 생성
img = np.zeros((512,512,3), np.uint8)
# This names the window so we can reference it
cv2.namedWindow(winname='my_drawing')
# Connects the mouse button to our callback function
cv2.setMouseCallback('my_drawing',draw_circle)

while True:
    # Shows the image window
    cv2.imshow('my_drawing',img)

    # https://stackoverflow.com/questions/35372700/whats-0xff-for-in-cv2-waitkey1/39201163
    if cv2.waitKey(20) & 0xFF == 27:
        break

cv2.destroyAllWindows()