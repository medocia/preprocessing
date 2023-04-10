!pip install patchify

from patchify import patchify
import cv2
import numpy as np
from matplotlib import pyplot as plt
from google.colab.patches import cv2_imshow

#Predict on large image
large_image = cv2.imread('/content/drive/MyDrive/slicing/220412d_51_resample_crop.tif')
#This will split the image into small images of shape [3,3]
#patches = patchify(large_image, (256, 256), step=256)  #Step=256 for 256 patches means no overlap
print("Large image shape is: ", large_image.shape)
#print("Patches array shape is: ", patches.shape)

#JUST CHECKING
plt.figure()
plt.imshow(large_image)

patches_img = patchify(large_image, (1024, 1024,3), step=1024)  #Step=256 for 256 patches means no overlap
img=""    
for i in range(patches_img.shape[0]):
    for j in range(patches_img.shape[1]):
            
        single_patch_img = patches_img[i,j,0,:,:,:]
        #cv2_imshow(single_patch_img)

        cv2.imwrite('/content/drive/MyDrive/slicing/colored/' + 'image_' + str(img) + '_' + str(i)+str(j)+ ".tif", single_patch_img)
