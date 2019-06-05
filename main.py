# -*- coding: UTF-8 -*-
import cv2
import os
bmppath = '/home/mzx/郑州局6号文件2测线图片/'
outpath = '/home/mzx/转化jpg/'
for imagename in os.listdir(bmppath):
    image = cv2.imread(bmppath + imagename)
    imagename = imagename.strip('.bmp')
    cv2.imwrite(outpath+imagename + '.jpg', image)