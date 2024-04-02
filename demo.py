# encoding=utf-8
import os
import cv2
import numpy as np
im1_path = './TestData/NLPR/test_data/test_images/8_08-47-34.jpg'  # 原图
im2_path = './ATSA_pred/NLPR/8_08-47-34.png'  # alpha图

# im1_path = './TestData/RGBD135/test_data/test_images/RGBD_data_114.jpg'
# im2_path = './ATSA_pred/RGBD135/RGBD_data_114.png'

img1 = cv2.imread(im1_path)
img2 = cv2.imread(im2_path, cv2.IMREAD_GRAYSCALE)
h, w, c = img1.shape
img3 = np.zeros((h, w, 4))
img3[:, :, 0:3] = img1
img3[:, :, 3] = img2
cv2.imwrite('8_08-47-34.png', img3)

