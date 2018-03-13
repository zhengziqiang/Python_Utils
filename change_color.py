from pylab import *
import glob
from PIL import Image
import numpy as np
import os
# dict = {}
for files in glob.glob("/home/vision/out/rename/*.png"):
    img_all = Image.open(files)
    # r=img.crop((640,0,1280,480))
    # l=img.crop((0,0,256,256))
    r = img_all.crop((256, 0, 512, 256))
    r_resize=r.resize((512,256),Image.ANTIALIAS)
    img = array(r_resize)
    for i in range(256):
        for j in range(512):
            if ((np.abs(img[i, j, 0] - 0) < 20) & (np.abs(img[i, j, 1] - 0) < 20) & (
            np.abs(img[i, j, 2]-0) < 20)):
                img[i,j,0]=0
                img[i, j, 1] = 0
                img[i, j, 2] = 0
            if ((np.abs(img[i, j, 0] - 147) < 20) & (np.abs(img[i, j, 1] - 161) < 20) & (
            np.abs(img[i, j, 2]-161) < 20)):
                img[i,j,0]=147
                img[i, j, 1] = 161
                img[i, j, 2] = 161
            if ((np.abs(img[i, j, 0] - 181) < 20) & (np.abs(img[i, j, 1] - 137) < 20) & (
            np.abs(img[i, j, 2]-0) < 20)):
                img[i,j,0]=181
                img[i, j, 1] = 137
                img[i, j, 2] = 0
            if ((np.abs(img[i, j, 0] - 203) < 20) & (np.abs(img[i, j, 1] - 75) < 20) & (
            np.abs(img[i, j, 2]-22) < 20)):
                img[i,j,0]=203
                img[i, j, 1] = 75
                img[i, j, 2] = 22
            if ((np.abs(img[i, j, 0] - 7) < 20) & (np.abs(img[i, j, 1] - 54) < 20) & (
            np.abs(img[i, j, 2]-66) < 20)):
                img[i,j,0]=7
                img[i, j, 1] = 54
                img[i, j, 2] = 66

    new_img=Image.fromarray(img,"RGB")
    p,n=os.path.split(files)
    new_img.save("/home/vision/out/reset_color512/"+n)

