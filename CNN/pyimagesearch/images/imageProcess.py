# example of converting an image with the Keras API
from keras.preprocessing.image import load_img
from keras.preprocessing.image import img_to_array
from keras.preprocessing.image import array_to_img
from resizeimage import resizeimage
from pyimagesearch.images.imageGrayScale import *
import numpy as np
from tensorflow.keras import backend as K
from dataset.upload import *
import oss2
import os
import cv2

endpoint = 'http://oss-cn-beijing.aliyuncs.com'
auth = oss2.Auth('LTAI4GJq5fpr5LfUggyDLFDc', 'bTCHF7tSboJUfcZsXxWeHkP3sz64yS')
bucket = oss2.Bucket(auth, endpoint, 'picture-fashion')
style = ''

# load the image
def imageTests():
    num = 10000
    count = 1
    arr = imageConvert('pyimagesearch/images/clothes/trousers.jpg')
    arr = arr.reshape(1,28,28)
    dim = 100
    print("hii "+str(arr.shape))
    for ii in range(dim):
        num = num + 1
        print(num)
        key = str(num)+'.jpg'
        new_pic = '/Users/akirachang/Desktop/testing/images' + key
        # print('here')
        try:
            bucket.get_object_to_file(key, new_pic)
            count += 1
        except:
            # print(index)
            continue
        img = imageConvert(new_pic)
        img = img.reshape(1,28,28)
        arr = np.append(img,arr)
        print("Orignal:" ,type(img))
        print(type(img))
        # print(img)
        # convert to numpy array
        # x = img
        # np.savetxt('file.txt', x)
        # print(type(img))
        # print("type:",img.dtype)
        # print("shape:",img.shape)
        # new_data = np.loadtxt('file.txt')
        # new_data = new_data.reshape(1,28,28,1)
    print(arr.shape)
    if K.image_data_format() == "channels_first":
        arr = arr.reshape(count,1,28,28)
    else: 
        arr = arr.reshape(count,28,28,1)
    return arr

# imageTests()
# convert back to image

