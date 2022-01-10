import cv2
import numpy as np
import matplotlib.pyplot as plt

drawing = False # True if mouse is pressed
ix,iy = -1,-1

def draw(event,x,y,flags,param):
    # 마우스 왼쪽 버튼 클릭하면 초록색 원을 그린다.
    # if event == cv2.EVENT_LBUTTONDOWN:
    #     cv2.circle(img,(x,y),100,(0,255,0),-1)

    global ix, iy, drawing, mode

    if event == cv2.EVENT_LBUTTONDOWN:
        # When you click DOWN with left mouse button drawing is set to True
        drawing = True
        # Then we take note of where that mouse was located
        ix, iy = x, y

    elif event == cv2.EVENT_MOUSEMOVE:
        # Now the mouse is moving
        if drawing == True:
            # If drawing is True, it means you've already clicked on the left mouse button
            # We draw a rectangle from the previous position to the x,y where the mouse is
            cv2.rectangle(img, (ix, iy), (x, y), (0, 255, 0), -1)


    elif event == cv2.EVENT_LBUTTONUP:
        # Once you lift the mouse button, drawing is False
        drawing = False
        # we complete the rectangle.
        cv2.rectangle(img, (ix, iy), (x, y), (0, 255, 0), -1)

# 검은색 이미지 생성
img = np.zeros((512,512,3), np.uint8)
# This names the window so we can reference it
cv2.namedWindow(winname='my_drawing')
# 마우스 버튼과 콜백함수를 연결한다.
cv2.setMouseCallback('my_drawing',draw)

while True:
    # Shows the image window
    cv2.imshow('my_drawing',img)

    # https://stackoverflow.com/questions/35372700/whats-0xff-for-in-cv2-waitkey1/39201163
    if cv2.waitKey(1) & 0xFF == 27:
        break

cv2.destroyAllWindows()