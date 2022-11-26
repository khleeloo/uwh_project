"""
num_channels.py
Find number of channels in your image.
Author: liuhh02 https://machinelearningtutorials.weebly.com/
"""

from PIL import Image
import numpy as np
from os import listdir


# # name of your image file
# filename = '/home/rita/uwh_project/justin/datasets/SQUID_original/image_set_01/LFT_3875resizedUndistort.tif'

# # open image using PIL
# img = Image.open(filename)

# # convert to numpy array
# img = np.array(img)

# # find number of channels
# if img.ndim == 2:
#     channels = 1
#     print("image has 1 channel")
# else:
#     channels = img.shape[-1]
#     print("image has", channels, "channels")


"""
pix2pix_combine
Combine 2 images from different domains for pix2pix. Make sure images in folderA and folderB have the same name.
Folder Structure:
folderA
    |--> train
    |--> valid (if any)
    |--> test (if any)
folderB
    |--> train
    |--> valid (if any)
    |--> test (if any)
dest_path
    |--> train
    |--> valid (if any)
    |--> test (if any_
Adapted from https://github.com/junyanz/pytorch-CycleGAN-and-pix2pix
"""

import os
import numpy as np
from PIL import Image
import cv2
import sys

class Preprocess():
    

    def tile(self,*images, vertical=False):
        width, height = images[0].width, images[0].height
        tiled_size = (
            (width, height * len(images))
            if vertical
            else (width * len(images), height)
        )
        tiled_img = Image.new(images[0].mode, tiled_size)
        row, col = 0, 0
        for image in images:
            tiled_img.paste(image, (row, col))
            if vertical:
                col += height
            else:
                row += width

        return tiled_img




    def allign_stereo(self,folderA,folderB,dest_path):
        splitsA = os.listdir(folderA)
        splitsB = os.listdir(folderB)

        for spa, spb in zip(splitsA,splitsB):
            img_fold_A = os.path.join(folderA, spa)
            img_fold_B = os.path.join(folderB, spb)
            img_list_A = os.listdir(folderA)
            img_list_B = os.listdir(folderB)
            num_imgs = len(img_list_A)
        
            # img_fold_AB = os.path.join(dest_path, sp)
            if not os.path.isdir(dest_path):
                os.makedirs('output')
            print('splitA = %s, number of images = %d' % (spa, num_imgs))

            name_A = spa.split('.tif')[0] 
            name_B=spb.split('.tif')[0] 
            name_AB = name_A +'_'+ name_B + '.jpeg' 
            path_AB = os.path.join(dest_path, name_AB)
            im_A1 = Image.open(img_fold_A)
            im_B1 = Image.open(img_fold_B)
            im_AB=self.get_concat_h(im_A1,im_B1)
            im_AB.save(path_AB,'JPEG',optimize=True )


    def get_concat_h(self,im1, im2):
        dst = Image.new('RGB', (im1.width + im2.width, im1.height))
        dst.paste(im1, (0, 0))
        dst.paste(im2, (im1.width, 0))
        return dst

    def normalize(self, arr):
        '''Function to scale an input array to [-1, 1]'''
        arr_min = arr.min()
        arr_max = arr.max()
        # Check the original min and max values
        print('Min: %.3f, Max: %.3f' % (arr_min, arr_max))
        arr_range = arr_max - arr_min
        scaled = np.array((arr-arr_min) / float(arr_range), dtype='f')
        arr_new = -1 + (scaled * 2)
        # Make sure min value is -1 and max value is 1
        print('Min: %.3f, Max: %.3f' % (arr_new.min(), arr_new.max()))
        return arr_new

    def scale(self,img_path):
        for filename in listdir(img_path):
            # load image
            image = Image.open(img_path+'/'+ filename)
            # convert to numpy array
            image = np.array(image)
            # scale to [-1,1]
            image = self.normalize(image)
            image.save(img_path+'/'+ filename)

    def change_format(self,img_path):
        for filename in listdir(img_path):
            # load image
            image = Image.open(img_path+'/'+ filename)
            new_file=filename.split('.')[0]

            image.save(img_path+'/'+ new_file+'.png')


    def resize(self,path):
     
        for item in  listdir( path ):
            if os.path.isfile(path+item):
                img = Image.open(path+item)
                f, e = os.path.splitext(path+item)
                img = img.resize((256,256), Image.ANTIALIAS)
                img.save(f + '.jpeg') 
    





        

"""
scale_images.py
Function to scale any image to the pixel values of [-1, 1] for GAN input.
Author: liuhh02 https://machinelearningtutorials.weebly.com/
"""

#

def main():
    '''specify input paths for stereo and output paths'''
    # folderA = 'FolderA'
    folderA = sys.argv[0]
    # folderA='Output_from_Seathru'
    # folderB = sys.argv[1]
    # dest_path = sys.argv[2]
    pr=Preprocess()
    # if len(sys.argv)>2:
    #     pr.allign_stereo(folderA,folderB,dest_path)
    # else:
    #     pr.change_format(folderA)
    pr.resize( folderA )
    


    
    
    # define paths for translation from domain A (images in folderA) -> domain B (images in folderB)
    # loop through all files in the directory





if __name__=='__main__':
    main()

