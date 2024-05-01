import os
import cv2
import numpy as np
import time  # 导入时间模块

# 定义原始图片文件夹路径和处理后保存的文件夹路径
input_folder = './TestData/RGBD135/test_data/test_images/'
output_folder = './Processed_Images/RGBD135-1/'
# truth_folder = './Processed_Images/RGBD135/'  # 存放真实抠图结果的文件夹路径

start_time = time.time()

# 获取原始图片文件夹中所有图片文件的路径
image_files = os.listdir(input_folder)

# 遍历每张图片进行处理
for image_file in image_files:
    if image_file.endswith('.jpg') or image_file.endswith('.png'):
        # 拼接原始图片文件的完整路径
        im1_path = os.path.join(input_folder, image_file)
        # print(im1_path)
        
        # 生成alpha图的文件名
        alpha_file = os.path.splitext(image_file)[0] + '.png'
        im2_path = os.path.join('./sal_map_1/RGBD135/', alpha_file)
        # print(im2_path)
        
        # 读取原始图片和alpha图
        img1 = cv2.imread(im1_path)
        img2 = cv2.imread(im2_path, cv2.IMREAD_GRAYSCALE)
        
        # 创建处理后图片的数组，并进行处理
        h, w, c = img1.shape
        img3 = np.zeros((h, w, 4))
        # img3[:, :, 3] = img2[:, :, np.newaxis]
        img3[:, :, 0:3] = img1
        img3[:, :, 3] = img2
        
        # 生成处理后图片的保存路径
        output_path = os.path.join(output_folder, alpha_file)
        # print(output_path)
        
        # 保存处理后的图片
        cv2.imwrite(output_path, img3)
        
#         # 读取真实抠图结果
#         truth_path = os.path.join(truth_folder, alpha_file)
#         truth_img = cv2.imread(truth_path, cv2.IMREAD_GRAYSCALE)
        
#         # 计算准确率
#         accuracy = np.sum(img3 == truth_img) / (h * w)  # 像素相同的数量除以总像素数
#         print(f'Accuracy for {image_file}: {accuracy:.4f}')

# 计算运行时间
end_time = time.time()
execution_time = end_time - start_time
print(f'Execution Time: {execution_time:.4f} seconds')

