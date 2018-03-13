import numpy as np
from PIL import Image
from pylab import *
import os
root="E:\\p2c_project\\facial_key_point\\annotation\\annotation\\"
img_path="E:\\p2c_project\\facial_key_point\\all\\"
for i in range(1,2331):
    left=3000
    right=0
    up=3000
    down=0
    path=root+str(i)+".txt"
    name=open(path).readline()
    name=name.strip('\n')
    img_name=img_path+name+".jpg"
    if not os.path.exists(img_name):
        continue
    img=Image.open(img_name)
    img_data=array(img)
    img_h,img_w=np.shape(img_data)[0],np.shape(img_data)[1]
    data=np.genfromtxt(path,delimiter=',',skip_header=1,dtype=float)#skip the first line
    for j in range(len(data)):
        width=np.int(data[j][0])
        height = np.int(data[j][1])
        if not (height<img_h):
            continue
        if not (width<img_w):
            continue
        if width<left:
            left=width
        if width>right:
            right=width
        if height<up:
            up=height
        if height>down:
            down=height
        #1
        img_data[height,width,0]=255
        img_data[height, width, 1] =0
        img_data[height, width, 2] = 0
        #2
        if height>1:
            img_data[height-1,width,0]=255
            img_data[height-1, width, 1] =0
            img_data[height-1, width, 2] = 0
        #3
        if height < img_h-1:
            img_data[height+1,width,0]=255
            img_data[height+1, width, 1] =0
            img_data[height+1, width, 2] = 0
        #4
        if width>1:
            img_data[height,width-1,0]=255
            img_data[height, width-1, 1] =0
            img_data[height, width-1, 2] = 0
        #5
        if width < img_w - 1:
            img_data[height,width+1,0]=255
            img_data[height, width+1, 1] =0
            img_data[height, width+1, 2] = 0
        #6
        if height>1 and width>1:
            img_data[height-1,width-1,0]=255
            img_data[height-1, width-1, 1] =0
            img_data[height-1, width-1, 2] = 0
        #7
        if height > 1 and width < img_w-1:
            img_data[height-1,width+1,0]=255
            img_data[height-1, width+1, 1] =0
            img_data[height-1, width+1, 2] = 0
        #8
        if height < img_h-1 and width > 1:
            img_data[height+1,width-1,0]=255
            img_data[height+1, width-1, 1] =0
            img_data[height+1, width-1, 2] = 0
        #9
        if height < img_h-1 and width < img_w-1:
            img_data[height+1,width+1,0]=255
            img_data[height+1, width+1, 1] =0
            img_data[height+1, width+1, 2] = 0
    if left>10:
        left-=10
    else:
        left=0
    if right+10>img_w:
        right=img_w
    else:
        right+=10
    if up<10:
        up=0
    else:
        up-=10
    if down+10>img_h:
        down=img_h
    else:
        down+=10
    new_img=Image.fromarray(img_data,"RGB")
    crop_img=new_img.crop((left,up,right,down))
    p,n=os.path.split(img_name)
    crop_img.save("E:\\p2c_project\\facial_key_point\\crop\\"+n)


#[0,0,0],[203,75,22],[147,161,161],[181,137,0],[7,54,66]
