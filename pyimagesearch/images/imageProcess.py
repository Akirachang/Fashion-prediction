# example of converting an image with the Keras API
from keras.preprocessing.image import load_img
from keras.preprocessing.image import img_to_array
from keras.preprocessing.image import array_to_img
from resizeimage import resizeimage
from pyimagesearch.images.imageGrayScale import *

import cv2

# load the image
def imageTests():
    img = imageConvert('pyimagesearch/images/clothes/trousers.jpg')
    print("Orignal:" ,type(img))
    print(type(img))
    print(img.shape)
    # convert to numpy array
    img = img.reshape((1, 28, 28, 1))
    print(type(img))
    print("type:",img.dtype)
    print("shape:",img.shape)
    return img
# convert back to image

