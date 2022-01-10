import cv2
import numpy as np
import matplotlib.pyplot as plt

img1 = cv2.imread('../../DATA/dog_backpack.png')
img2 = cv2.imread('../../DATA/watermark_no_copy.png')

# BGR -> RGB 변경
img1 = cv2.cvtColor(img1, cv2.COLOR_BGR2RGB)
img2 = cv2.cvtColor(img2, cv2.COLOR_BGR2RGB)

img1 =cv2.resize(img1,(1200,1200))
img2 =cv2.resize(img2,(1200,1200))

# 같은 사이즈 이미지 블렌드하기
blended = cv2.addWeighted(src1=img1,alpha=0.7,src2=img2,beta=0.3,gamma=0)
plt.imshow(blended)
plt.show()

print(img1.shape)
print(img2.shape)

# 다른 사이즈 이미지 오버레이하기
img1 = cv2.imread('../../DATA/dog_backpack.png')
img2 = cv2.imread('../../DATA/watermark_no_copy.png')

img2 =cv2.resize(img2,(600,600))

img1 = cv2.cvtColor(img1, cv2.COLOR_BGR2RGB)
img2 = cv2.cvtColor(img2, cv2.COLOR_BGR2RGB)

print(img1.shape)
print(img2.shape)

large_img = img1
small_img = img2

x_offset=0
y_offset=0

large_img[y_offset:y_offset+small_img.shape[0], x_offset:x_offset+small_img.shape[1]] = small_img
plt.imshow(large_img)
plt.show()

# 다른 사이즈 이미지 블렌드하기
img1 = cv2.imread('../../DATA/dog_backpack.png')
img2 = cv2.imread('../../DATA/watermark_no_copy.png')

img2 =cv2.resize(img2,(600,600))

img1 = cv2.cvtColor(img1, cv2.COLOR_BGR2RGB)
img2 = cv2.cvtColor(img2, cv2.COLOR_BGR2RGB)

x_offset=934-600
y_offset=1401-600

rows,cols,channels = img2.shape
roi = img1[y_offset:1401,x_offset:943] # BOTTOM RIGHT CORNER # roi = img1[0:rows, 0:cols ] # TOP LEFT CORNER
plt.imshow(roi)
plt.show()

# BGR -> GRAY 변환
img2gray = cv2.cvtColor(img2,cv2.COLOR_BGR2GRAY)

print(img2gray.shape)

plt.imshow(img2gray, cmap='gray')
plt.show()

# INV -> 색반전
mask_inv = cv2.bitwise_not(img2gray)
plt.imshow(mask_inv,cmap='gray')
plt.show()

# 하얀색 배경 만들기
white_background = np.full(img2.shape, 255, dtype=np.uint8)
bk = cv2.bitwise_or(white_background, white_background, mask=mask_inv)
plt.imshow(bk)
plt.show()

plt.imshow(mask_inv,cmap='gray')
plt.show()

fg = cv2.bitwise_or(img2, img2, mask=mask_inv)
plt.imshow(fg)
plt.show()

final_roi = cv2.bitwise_or(roi,fg)
plt.imshow(final_roi)
plt.show()

large_img = img1
small_img = final_roi

large_img[y_offset:y_offset+small_img.shape[0], x_offset:x_offset+small_img.shape[1]] = small_img

plt.imshow(large_img)
plt.show()