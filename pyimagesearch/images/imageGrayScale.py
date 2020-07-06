import numpy as np
from PIL import Image
import cv2

def imageConvert(str):
    im = np.array(Image.open(str).convert('L')) #you can pass multiple arguments in single line
    print(type(im))
    str = str.replace('.jpeg','')
    str = str.replace('.png','')
    gr_im= Image.fromarray(im).save('1.png')

    img = cv2.imread('1.png', cv2.IMREAD_UNCHANGED)
    
    print('Original Dimensions : ',img.shape)
    
    scale_percent = 60 # percent of original size
    width = 28
    height = 28
    dim = (width, height)
    # resize image
    resized = cv2.resize(img, dim, interpolation = cv2.INTER_AREA)

    print('Resized Dimensions : ',resized.shape)
    
    # cv2.imshow("Resized image", resized)
    # cv2.waitKey(0)
    # cv2.destroyAllWindows()

    return resized