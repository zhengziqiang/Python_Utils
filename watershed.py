import numpy as np
import scipy.io
from PIL import Image
import glob
import os
# for files in glob.glob("/media/scs4450/52d95cdd-64a0-4c37-9480-dc43778ffc5f/next/gan/seg2color/cityscapes/val/*.jpg"):
#     semantic = scipy.misc.imread(files)
#     semantic=semantic[:,256:,:]
#     # print(semantic.shape)
#     tmp = np.zeros((semantic.shape[0], semantic.shape[1], 3), dtype=np.float32)
#     for k in range(3):
#         tmp[:, :, k] = np.float32((np.abs(semantic[:, :, 0] - 0) < 20) & (np.abs(semantic[:, :, 1] - 0) < 20) & (
#             semantic[:, :, 2] > 102
#         ))
#     one_tmp = np.ones((semantic.shape[0], semantic.shape[1], 3), dtype=np.float32)
#     one_tmp = 255.0
#     output_uint8 = np.uint8(tmp)
#     new_seg = np.multiply(tmp, one_tmp)
#     new_seg_uint = np.uint8(new_seg)
#     img_save = Image.fromarray(new_seg_uint, 'RGB')
#     p,n=os.path.split(files)
#     img_save.save("/media/scs4450/52d95cdd-64a0-4c37-9480-dc43778ffc5f/next/gan/seg2color/cityscapes/val-waterseg/"+n)

for files in glob.glob("/media/scs4450/52d95cdd-64a0-4c37-9480-dc43778ffc5f/next/gan/seg2color/cityscapes/train/*.jpg"):
    img=Image.open(files)
    # r=img.crop((256,0,512,256))
    target=Image.new("RGB",(768,256))
    target.paste(img,(0,0,512,256))
    # r_resize=img.resize((512,256),Image.ANTIALIAS)
    p,n=os.path.split(files)
    r=Image.open("/media/scs4450/52d95cdd-64a0-4c37-9480-dc43778ffc5f/next/gan/seg2color/cityscapes/new-seg/"+n)
    target.paste(r,(512,0,768,256))
    target.save("/media/scs4450/52d95cdd-64a0-4c37-9480-dc43778ffc5f/next/gan/seg2color/cityscapes/trainnored/"+n)
# import numpy as np
# import cv2
# from PIL import Image
# # import cv
# import glob
# import os
# # from matplotlib import pyplot as plt
# for files in glob.glob("/media/scs4450/52d95cdd-64a0-4c37-9480-dc43778ffc5f/next/gan/seg2color/cityscapes/new-seg/*.jpg"):
#     img = cv2.imread(files)
#     # gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
#     # ret, thresh = cv2.threshold(gray,0,255,cv2.THRESH_BINARY_INV+cv2.THRESH_OTSU)
#     thresh = cv2.imread(files)
#     thresh = cv2.cvtColor(thresh, cv2.COLOR_BGR2GRAY)
#     kernel = np.ones((3, 3), np.uint8)
#     opening = cv2.morphologyEx(thresh, cv2.MORPH_OPEN, kernel, iterations=2)
#
#     # sure background area
#     sure_bg = cv2.dilate(opening, kernel, iterations=3)
#
#     # Finding sure foreground area
#     dist_transform = cv2.distanceTransform(opening, cv2.DIST_L2, 5)
#     ret, sure_fg = cv2.threshold(dist_transform, 0.7 * dist_transform.max(), 255, 0)
#
#     # Finding unknown region
#     sure_fg = np.uint8(sure_fg)
#     unknown = cv2.subtract(sure_bg, sure_fg)
#     ret, markers = cv2.connectedComponents(sure_fg)
#
#     # Add one to all labels so that sure background is not 0, but 1
#     markers = markers + 1
#
#     # Now, mark the region of unknown with zero
#     markers[unknown == 255] = 0
#     markers = cv2.watershed(img, markers)
#     img[markers == -1] = [255, 0, 0]
#     img_save = Image.fromarray(img, 'RGB')
#     p,n=os.path.split(files)
#     img_save.save('/media/scs4450/52d95cdd-64a0-4c37-9480-dc43778ffc5f/next/gan/seg2color/cityscapes/water-seg/'+n)
