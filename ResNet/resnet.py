# -*- coding: utf-8 -*-
import os, torch, glob
import numpy as np
from torch.autograd import Variable
from PIL import Image  
from torchvision import models, transforms
import torch.nn as nn
# import shutil
data_dir = '/Users/akirachang/Desktop/coding/Python/fashion-forecast/ResNet/pictures'
features_dir = '/Users/akirachang/Desktop/coding/Python/fashion-forecast/ResNet/resnet50'
# shutil.copytree(data_dir, os.path.join(features_dir, data_dir[2:]))
 
 
def extractor(img_path, saved_path, net, use_gpu):
    transform = transforms.Compose([
            transforms.Resize(256),
            transforms.CenterCrop(224),
            transforms.ToTensor()    ]
    )
    try:
        img = Image.open(img_path)
        img = img.convert("RGB")
        # print(img.size)
        img = transform(img)
        # print(img.shape)
    except Exception as e:
        f = open('error.txt', 'a')
        f.write(img_path+'\n')
        f.close()
        print(img_path)
        return
    
    x = Variable(torch.unsqueeze(img, dim=0).float(), requires_grad=False)
    if use_gpu:
        x = x.cuda()
        net = net.cuda()
    y = net(x).cpu()
    y = y.data.numpy()
    y = np.squeeze(y)
    np.savetxt(saved_path, y, delimiter=',')
    
if __name__ == '__main__':
    extensions = ['jpg', 'jpeg', 'JPG', 'JPEG']
        
    files_list = []
    sub_dirs = [x[0] for x in os.walk(data_dir) ]
    sub_dirs = sub_dirs[1:]
    for sub_dir in sub_dirs:
        for extention in extensions:
            file_glob = os.path.join(sub_dir, '*.' + extention)
            files_list.extend(glob.glob(file_glob))
        
    resnet = models.resnet50(pretrained = True)
    # print(resnet)
    # resnet.fc = nn.Linear(2048, 2048)
    # torch.nn.init.eye(resnet.fc.weight)
    # resnet = models.resnet152(pretrained=True)
    modules = list(resnet.children())[:-1]      # delete the last fc layer.
    convnet = nn.Sequential(*modules)
    # print(convnet)
    
    for param in convnet.parameters():
        param.requires_grad = False   
        
    use_gpu = torch.cuda.is_available()
    i = 0
    print(len(files_list))
    for x_path in files_list:
        i += 1
        # print(x_path)
        fx_path = os.path.join(features_dir, x_path[2:].split('/')[-1] + '.txt')
        if os.path.exists(fx_path):
            continue
        # print(fx_path)
        if i % 100 == 0:
            print(i)
        extractor(x_path, fx_path, convnet, use_gpu)
        # break