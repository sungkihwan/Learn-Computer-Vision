import cv2
import numpy as np
import matplotlib.pyplot as plt

# img = cv2.imread('../DATA/00-puppy.jpg')
#
# while True:
#     cv2.imshow('Puppy',img)
#     # esc 키를 누르면 while을 탈출할 수 있도록 한다.
#     if cv2.waitKey(1) & 0xFF == 27:
#         break
#
# cv2.destroyAllWindows()

blank_img = np.zeros(shape=(512,512,3),dtype=np.int16)
print(blank_img.shape)
plt.imshow(blank_img)
plt.show()

# 이미지에 정사각형 그리기
cv2.rectangle(blank_img,pt1=(384,10),pt2=(500,128),color=(0,255,0),thickness=5)
plt.imshow(blank_img)
plt.show()

# cv2.rectangle(blank_img,pt1=(200,200),pt2=(300,300),color=(0,0,255),thickness=5)
# plt.imshow(blank_img)
# plt.show()
#
# cv2.circle(img=blank_img, center=(100,100), radius=50, color=(255,0,0), thickness=5)
# plt.imshow(blank_img)
# plt.show()
#
# cv2.circle(img=blank_img, center=(400,400), radius=50, color=(255,0,0), thickness=-1)
# plt.imshow(blank_img)
# plt.show()
#
# cv2.line(blank_img,pt1=(0,0),pt2=(511,511),color=(102, 255, 255),thickness=5)
# plt.imshow(blank_img)
# plt.show()
#
# font = cv2.FONT_HERSHEY_SIMPLEX
# cv2.putText(blank_img,text='Hello',org=(10,500), fontFace=font,fontScale= 4,color=(255,255,255),thickness=2,lineType=cv2.LINE_AA)
# plt.imshow(blank_img)
# plt.show()
#
# blank_img = np.zeros(shape=(512,512,3),dtype=np.int32)
# vertices = np.array([[100,300],[200,200],[400,300],[200,400]],np.int32)
# pts = vertices.reshape((-1,1,2))
# cv2.polylines(blank_img,[pts],isClosed=True,color=(255,0,0),thickness=5)
# plt.imshow(blank_img)
# plt.show()