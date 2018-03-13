import os
import glob
from PIL import Image
import shutil
# cnt=0
# root="/home/vision/out/rename/"
# for files in glob.glob("/home/vision/out/merge/*.png"):
#     shutil.copy(files,root+str(cnt)+'.png')
#     cnt+=1

# for files in glob.glob("/media/vision/HD12T/zzq/research/PycharmProjects/pix2pix-tensorflow-master/nyu2-795/label/*.png"):
#     img=Image.open(files)
#     target=Image.new('RGB',(512,256))
#     p,n=os.path.split(files)
#     target.paste(img,(0,0,256,256))
#     right=Image.open('/media/vision/HD12T/zzq/research/PycharmProjects/pix2pix-tensorflow-master/nyu2-795/images/'+n)
#     target.paste(right,(256,0,512,256))
#     target.save("/media/vision/HD12T/zzq/research/PycharmProjects/pix2pix-tensorflow-master/nyu2-795/train/"+n)
# root="/home/vision/out/training"
# dirs=os.listdir(root)
# dest="/home/vision/out/merge/"
# for i in range(len(dirs)):
#     sub_dir= root+'/'+dirs[i]+'/'
#     for files in glob.glob(sub_dir+"*_colors.png"):
#         left=Image.open(files)
#         lr=left.resize((256,256),Image.ANTIALIAS)
#         p,n=os.path.split(files)
#         nn=n.split('.')
#         name=nn[0]
#         ths=name.split('_')
#         th=ths[0]
#         right_name=sub_dir+th+"_ground_truth.png"
#         right=Image.open(right_name)
#         rr=right.resize((256,256),Image.ANTIALIAS)
#         target=Image.new("RGB",(512,256))
#         target.paste(lr,(0,0,256,256))
#         target.paste(rr,(256,0,512,256))
#         target.save(dest+n)


from PIL import Image
import glob
import os
# for files in glob.glob("/media/vision/HD12T/zzq/research/PycharmProjects/pix2pix-tensorflow-master/cityscapesnoise/train/*.jpg"):
#     img=Image.open(files)
#     l=img.crop((0,0,256,256))
#     r=img.crop((256,0,512,256))
#     p,n=os.path.split(files)
#     l.save("/media/vision/HD12T/zzq/research/PycharmProjects/pix2pix-tensorflow-master/cityscapesnoise/traincolor/"+n)
#     r.save("/media/vision/HD12T/zzq/research/PycharmProjects/pix2pix-tensorflow-master/cityscapesnoise/trainseg/"+n)
for files in glob.glob("/media/vision/43c620be-e7c3-4af9-9cf6-c791ef2ed83e/zzq/mask-scale/data/nyu2-795/images/*.jpg"):
    target=Image.new("RGB",(512,256))
    l=Image.open(files)
    p,n=os.path.split(files)
    r=Image.open("/media/vision/43c620be-e7c3-4af9-9cf6-c791ef2ed83e/zzq/mask-scale/data/nyu2-795/label/"+n)
    target.paste(l,(0,0,256,256))
    target.paste(r,(256,0,512,256))
    target.save("/"+n)

# for files in glob.glob("/media/vision/HD12T/zzq/research/PycharmProjects/pix2pix-tensorflow-master/cityscapes/train/*.jpg"):
#     target=Image.new("RGB",(768,256))
#     l=Image.open(files)
#     p,n=os.path.split(files)
#     target.paste(l,(0,0,512,256))
#     r=Image.open("/media/vision/HD12T/zzq/research/PycharmProjects/pix2pix-tensorflow-master/cityscapes/water-seg/"+n)
#     target.paste(r,(512,0,768,256))
#     target.save("/media/vision/HD12T/zzq/research/PycharmProjects/pix2pix-tensorflow-master/cityscapes/trainwater/"+n)


# for files in glob.glob("/media/vision/HD12T/zzq/research/PycharmProjects/pix2pix-tensorflow-master/cityscapes/val/*.jpg"):
#     l=Image.open(files)
#     target=Image.new("RGB",(768,256))
#     target.paste(l,(0,0,512,256))
#     p,n=os.path.split(files)
#     r=Image.open("/media/vision/HD12T/zzq/research/PycharmProjects/pix2pix-tensorflow-master/cityscapes/val-waterseg/"+n)
#     target.paste(r,(512,0,768,256))
#     target.save("/media/vision/HD12T/zzq/research/PycharmProjects/pix2pix-tensorflow-master/cityscapes/valwater/"+n)