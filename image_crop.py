'''
    Date: 22 January 2019
    Author: Anis Sarker
    Cropping satellite images in 1024x1024 for Kutupalong area
'''

import cv2
import os
import matplotlib.pyplot as plt
import numpy as np

directory = '/home/void/Documents/Project/Newly_cropped/432/'

imageName = []
imgListName = [i for i in os.listdir(directory)]

x, y = 5150, 700

for file in os.listdir(directory):
    file_name, file_ext = os.path.splitext(file)
    print(file_name, '-', file_ext)
    n_img = cv2.imread(os.path.join(directory, file))
    # n_img = np.asarray(n_img)
    # cv2.rectangle(n_img, (x, y), (x+1024, y+1024), (255, 0, 0), 5)
    crop_img = n_img[x:x+1024, y:y+1024]
    # n_img = cv2.resize(n_img, dsize=(512, 512), interpolation=cv2.INTER_CUBIC)
    cv2.imwrite('New/' + file_name + file_ext, crop_img)
    # cv2.imshow(file_name, crop_img)
    # cv2.waitKey(0)
    # cv2.destroyAllWindows()