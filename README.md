# Intelligent-Image-Matting-System
##  1、系统功能：
本项目使用显著性目标检测技术实现了一个智能抠图系统。其中显著性目标检测技术是自己设计的基于金字塔视觉Transformer（ Pyramid Vision Transforme）的非对称RGBD显著性目标检测网络（PVTANet）。后面会简单介绍一下这个网络。
## 2、系统流程：
实现抠图功能的代码放在demo.py文件中。 

这段代码使用Python和OpenCV库实现图片合成代码。代码中的功能是将两张图片进行合成，其中一张图片是原始的RGB图像，另一张图片是表示透明度的alpha图像。
我们挑选了几张代表不同场景下的图片。原始的RGB图像放在 /[original_images](https://github.com/STRUGGLE1999/Intelligent-Image-Matting-System/tree/main/original_images) 文件夹中，alpha图像是使用我们提出的显著性检测网络(PVTANet)检测得到的显著性预测图像，放在 /[alpha_images](https://github.com/STRUGGLE1999/Intelligent-Image-Matting-System/tree/main/alpha_images) 文件夹中。
在Alpha图像中，每个像素都有一个额外的通道，通常用于表示该像素的透明度级别。这个额外的通道通常被称为Alpha通道。Alpha通道的取值范围通常是0到255之间，其中0表示完全透明，255表示完全不透明。对于介于0和255之间的值，表示了介于完全透明和完全不透明之间的透明度级别。
**实现抠图的主要流程为**：

1. 首先使用cv2.imread()函数读取原始RGB图像，以灰度图的方式读取alpha图像
2. 获取原始RGB图像的尺寸（高度、宽度、通道数），并创建一个全零数组img3来存储合成后的图片，大小与原始RGB图像相同，但通道数为4。
3. 将原始RGB图像的像素值复制到img3的前三个通道中（RGB通道）
4. 将alpha图像的像素值复制到img3的第四个通道中，这样img3就成为了一个带有透明度信息的RGBA图像。
5. 使用cv2.imwrite()函数将合成后的图片保存到指定路径中。
## 3、PVTANet简单介绍
PVTANet是我们提出的一种基于金字塔视觉Transformer（PVT）的非对称显著性目标检测网络。具体来说，我们认识到当前主流对称网络结构在处理 RGB 和深度特征时忽略数据固有差异、导致难以充分融合进而导致了信息丢失和性能下降等问题。
为了更好提取不同模态数据中的有效特征，我们使用不同的编码器进行特征提取，通过利用 PVT 从 RGB 图像中提取特征，并设计了一个轻量级深度模块用于深度特征提取。该模块通过特征交互和空间自注意力机制加强对深度特征的理解和利用。
为了更好地融合 RGB 和深度特征，我们提出了流梯度融合模块，以渐进的方式融合不同级别的特征并保留细节信息。同时引入深度注意力模块确保深度特征有效引导 RGB 特征，从而充分利用深度特征中的几何特征。
PVTANet的网络结构图如下图所示：

![图4-1.png](https://cdn.nlark.com/yuque/0/2024/png/22838017/1712049683748-06fc3884-fee6-4f71-97bf-3c00da6502cf.png#averageHue=%23e6e9d4&clientId=u6d5286e6-1f92-4&from=paste&height=751&id=u39c97063&originHeight=1502&originWidth=2162&originalType=binary&ratio=2&rotation=0&showTitle=false&size=265731&status=done&style=none&taskId=u59b0f8ad-a7ff-42b7-96cf-c40be1eec9d&title=&width=1081)

在网络训练过程中，我们使用PVT v2-b2作为骨干网络，以及使用它的预训练参数初始化，动量、权重衰减、批量大小和学习率分别设定为 0.9、0.0005、6 和 1e-10 本文的网络在 PyTorch 深度学习框架上实现，并在一块 NVIDIA GeForce RTX 3080 GPU 上加速。
最终在六个数据集上测试的定量P-R曲线如下：
![P-R.png](https://cdn.nlark.com/yuque/0/2024/png/22838017/1712049869447-249ce275-520f-4e41-8f87-7870aed3ad92.png#averageHue=%23f2f1f1&clientId=u6d5286e6-1f92-4&from=paste&height=577&id=u442cbb5a&originHeight=1154&originWidth=2079&originalType=binary&ratio=2&rotation=0&showTitle=false&size=752651&status=done&style=none&taskId=u14daaf0c-9c63-44f4-a27b-75244d86ece&title=&width=1039.5)
定性评估如下：
![图4-6.png](https://cdn.nlark.com/yuque/0/2024/png/22838017/1712049902573-06ae1d39-d6b4-4cdc-8763-4ea3c5270429.png#averageHue=%23454544&clientId=u6d5286e6-1f92-4&from=paste&height=709&id=ue265b034&originHeight=1417&originWidth=2082&originalType=binary&ratio=2&rotation=0&showTitle=false&size=1347263&status=done&style=none&taskId=ufa74ddf3-ecf8-4d53-aea2-4fc55b8e574&title=&width=1041)



