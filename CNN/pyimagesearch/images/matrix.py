import os
from imageGrayScale import imageConvert
import numpy as np

def testing():
    content_array = []
    with open('/Users/akirachang/Desktop/coding/Python/fashion-forecast/excl/matix.txt') as f:
            #Content_list is the list that contains the read lines.     
        for line in f:
            content_array.append(int(line.replace('\n','')))
        print(content_array)

    for filename in os.listdir('/Users/akirachang/Desktop/175990_396802_bundle_archive/images'):
        if filename.endswith(".jpg") or filename.endswith(".jpeg"): 
            # print(os.path.join(directory, filename))
            print(filename.replace('.jpg',''))
            try:
                if(content_array.index(int(filename.replace('.jpg',''))) != -1):
                    print("processing..")
                    arr = imageConvert('/Users/akirachang/Desktop/175990_396802_bundle_archive/images/'+filename)
                    arr = arr.reshape(1, 28, 28)

                    with open("/Users/akirachang/Desktop/testing/matrix/"+filename.replace('.jpg','')+'.txt', 'w') as f:
                        for item in arr:
                            f.write("%s\n" % item)  

                    print('write')
                    f.close()
            except:
                print('exception')
                continue
            else:
                print('here')
                continue

def getMatrix():
    content_array = []
    count = []
    with open('/Users/akirachang/Desktop/coding/Python/fashion-forecast/excl/matix.txt') as f:
            #Content_list is the list that contains the read lines.     
        for line in f:
            content_array.append(int(line.replace('\n','')))
        print(content_array)
    
    for i in range(len(content_array)):
        print(i)
        try:
            my_file = open('/Users/akirachang/Desktop/testing/matrix/'+str(content_array[i])+'.txt', "r")
        except:
            count.append(content_array[i])
        content = my_file.read()
        print(content)
    print(count)
    return '123'
# testing()
getMatrix()