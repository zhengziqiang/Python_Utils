import glob
from PIL import Image
from pylab import *

dict = {}
for files in glob.glob("/home/vision/PycharmProjects/seg/nyu2/train/*.jpg"):
    img = Image.open(files)
    # r=img.crop((640,0,1280,480))
    # l=img.crop((0,0,256,256))
    r = img.crop((256, 0, 512, 256))
    right = array(r)
    for i in range(256):
        for j in range(256):
            tmp = int(right[i, j, 0]) + int(right[i, j, 1]) + int(right[i, j, 2])
            if dict.has_key(tmp):
                continue
            else:

                tmP_list = []
                tmP_list.append(right[i, j, 0])
                tmP_list.append(right[i, j, 1])
                tmP_list.append(right[i, j, 2])
                dict[tmp] = tmP_list