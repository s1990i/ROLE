"""
from __future__ import absolute_import

import os
from raindrop.dropgenerator import generateDrops
from raindrop.config import cfg

from PIL import Image
import numpy as np
import cv2

from raindrop.dropgenerator import generateDrops

import numpy as np
# import HyperProTool as hyper
import scipy.io as sio # 3.9 vs 2.7
#from LRSR_1 import LRSR

from scipy import ndimage, misc
import cv2

from PIL import Image, ImageColor, ImageOps

import random
from matplotlib import cm

# it will return image in pillow format
# if using cfg["return_label"] = False


data = sio.loadmat("Sandiego_after_insert_petrol_tnt.mat")
data3d_brut = np.array(data["Sandiego_after_insert_petrol_tnt"], dtype=float)


#arr = np.ones(200,200)
#print(arr)
arr = np.eye(400, 400, 3)  #data3d_brut[:,:,0:4]

im = Image.fromarray(np.uint8(cm.gist_earth(  arr )*255)) # ==> comment transformer un tableau 3d (3 couches d'une matrice Hyperspectral) en type Image ?


#image_path = "Switzerland-Alps.jpg"
#image_data = Image.open(image_path)

output_image = generateDrops(data3d_brut[:,:,0:4], cfg)
#output_image[0].show()



##################

from PIL import Image
import numpy
im = Image.open("Switzerland-Alps.jpg")
np_im = numpy.array(im)
# print np_im.shape

np_im = np_im - 18
new_im = Image.fromarray(np_im)
new_im.save("Switzerland-Alps.jpg")

"""


# Python program to convert
# numpy array to image
  
# import required libraries
import numpy as np
from PIL import Image
from raindrop.dropgenerator import generateDrops
from raindrop.config import cfg
import cv2  
# define a main function
def main():
  
    # create a numpy array from scratch
    # using arange function.
    # 1024x720 = 737280 is the amount 
    # of pixels.
    # np.uint8 is a data type containing
    # numbers ranging from 0 to 255 
    # and no non-negative integers
    #amount = 400*400*3
    #array = np.arange(0, amount, 1, np.uint8)
      
    # check type of array
    #print(type(array)) TODO
      
    # our array will be of width 
    # 737280 pixels That means it 
    # will be a long dark line
    #print(array.shape) TODO
      
    # Reshape the array into a 
    # familiar resoluition
    
    #array = np.reshape(array, (400, 400,3))
    
    # show the shape of the array
    #print(array.shape) TODO
  
    # show the array
    #print(array) TODO
      
    # creating image object of
    # above array

    # rescale *1000
    # ==> traitement d'image
    # rescale /1000

    #data = Image.fromarray(array)
    #data.show()
    
    #output_image = generateDrops(array, cfg)
    #output_image[0].show()

    # saving the final output 
    # as a PNG file
    #output_image[0].save('emos_gfg_dummy_pic.png') #TODO
    image_path = "Switzerland-Alps.jpg"

    synth_img = Image.new('RGB', (1200, 720), color = (73, 109, 137))
    synth_img.save("synthetic.png")
    n_synth_img   = np.asarray(synth_img)
    print("synthetic image shape",n_synth_img.shape)
    
    """
    switzerland_img = Image.open(image_path)
    n_switzerland_img   = np.asarray(switzerland_img)
    print("switzerland shape" ,n_switzerland_img.shape)
    """
    output_image = generateDrops(image_path, cfg)
    #print(output_image[0].size)   
    output_image.show()
# driver code
if __name__ == "__main__":
    
  # function call
  main()


