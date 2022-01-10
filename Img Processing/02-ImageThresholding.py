import cv2
import numpy as np
import matplotlib.pyplot as plt

# img = cv2.imread('../../DATA/rainbow.jpg')
#
# plt.imshow(img)
# plt.show()
#
# # 회색으로 불러오기
img = cv2.imread('../../DATA/rainbow.jpg',0)
plt.imshow(img,cmap='gray')
plt.show()
#
# # 127 이상의 채도는 흰색으로 나머지는 검은색으로 임계면 구분을 한다.
# ret,thresh1 = cv2.threshold(img,127,255,cv2.THRESH_BINARY)
#
# print(ret, thresh1)
#
# plt.imshow(thresh1,cmap='gray')
# plt.show()
#
# # INV -> 색반전
# ret,thresh2 = cv2.threshold(img,127,255,cv2.THRESH_BINARY_INV)
# plt.imshow(thresh2,cmap='gray')
# plt.show()

# threshold(이미지, threshold_value, value, flag)
# THRESH_BINARY -> threshold_value 보다 크면 value, 작으면 0
# THRESH_BINARY_INV -> threshold_value 보다 크면 threshold_value, 작으면 value (인버스)
# THRESH_TRUNC -> threshold_value 보다 크면 threshold_value 작으면 현재 값 적용
# THRESH_TOZERO -> threshold_value 보다 크면 현재 값 적용, 작으면 0
# THRESH_TOZERO_INV -> 인버스
ret,thresh3 = cv2.threshold(img,127,255,cv2.THRESH_TOZERO_INV)
plt.imshow(thresh3,cmap='gray')
plt.show()

