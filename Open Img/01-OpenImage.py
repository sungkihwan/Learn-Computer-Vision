import numpy as np
import cv2
import matplotlib.pyplot as plt

# imread
img_bgr = cv2.imread('../../DATA/00-puppy.jpg')

plt.imshow(img_bgr)
plt.show()

# -> 3차원 이미지가 들어있으나 순서가 BGR로 들어있다.
# -> plt는 RGB로 읽는게 디폴트라서 변환해주면 된다.
print(img_bgr.shape)

# BGR -> RGB 변환
img_rgb = cv2.cvtColor(img_bgr, cv2.COLOR_BGR2RGB)

plt.imshow(img_rgb)
plt.show()

# jpg 이미지에서 녹색 컬러만 추출
img_gray = cv2.imread('../../DATA/00-puppy.jpg', cv2.IMREAD_GRAYSCALE)
plt.imshow(img_gray)
plt.show()

# -> 녹색만 뽑아내는거라서 img_gray는 2차원이다.
print(img_gray.shape)

# 컬러맵을 회색으로 지정
plt.imshow(img_gray,cmap='gray')
plt.show()

# x축으로 이미지 반전
x_flip_img = cv2.flip(img_rgb,0)
plt.imshow(x_flip_img)
plt.show()

# y축으로 이미지 반전
y_flip_img = cv2.flip(img_rgb,1)
plt.imshow(y_flip_img)
plt.show()

# 이미지 리사이즈 하기
w_ratio = 0.7
h_ratio = 0.3
img =cv2.resize(img_rgb,(700,275))
new_img =cv2.resize(img_rgb,(0,0),img,w_ratio,h_ratio)
plt.imshow(new_img)
plt.show()

pic_red = img_rgb.copy()
pic_green = img_rgb.copy()
pic_blue = img_rgb.copy()

pic_red[:, :, 1] = 0    # 초록색 제거
pic_red[:, :, 2] = 0    # 파란색 제거

pic_green[:, :, 0] = 0 # 빨간색 제거
pic_green[:, :, 2] = 0

pic_blue[:, :, 0] = 0
pic_blue[:, :, 1] = 0

plt.imshow(pic_red)
plt.show()
plt.imshow(pic_green)
plt.show()
plt.imshow(pic_blue)
plt.show()

# jpg 이미지로 만들기
cv2.imwrite('y_flip_img.jpg',y_flip_img)

