#导入cv模块
import cv2 as cv
import random
import numpy as np
# # =================================存取图像=====================================
# 60号宋体字母占用字符比较
xiangsi={
    "I":198,"V":229,"L":230,"U":235,"C":236,"Y":236,"T":245,"J":248,"A":262,"X":265,"Z":270,"N":276,"G":281,"F":284,"P":303,"O":306,"E":322,"K":339,"D":357,"W":373,"R":380,"H":384,"Q":391,"B":391,"S":292,"M":432
}

I_value=180   # I映射为不同的值表示亮度，
M_value=50   # M映射为50
x=(M_value-I_value)/(xiangsi['M']-xiangsi['I'])
b=I_value-xiangsi['I']*x
#归一化，后数组递减排列
for zimu in xiangsi:
    xiangsi[zimu]=int(x*xiangsi[zimu]+b)   # 将字母表示为对应的黑度值。

print(xiangsi)

# # 直接读取单通道灰度图
gray_img = cv.imread('hui.jpg', cv.IMREAD_GRAYSCALE)
gray_img = cv.resize(gray_img,(int(gray_img.shape[1]),int(gray_img.shape[0]/1.7)),interpolation=cv.INTER_CUBIC)
# cv.imshow('iker', gray_img)
# cv.waitKey(0)
print(gray_img.shape)   # 先是高度， 再是宽度
file = open('img.txt',mode='w')



for row in range(gray_img.shape[0]):
    for col in range(gray_img.shape[1]):
        pzimu=" "
        cansee=False
        for zimu in xiangsi:
            if (gray_img[row][col] > xiangsi[zimu]):
                file.write(pzimu)
                cansee=True
                break
            else:
                pzimu=zimu
        if(not cansee):file.write(pzimu)
    file.write('\n')
file.close() 