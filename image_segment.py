import cv2
import os
import matplotlib.pyplot as plt
import numpy as np

directory = '/home/void/Documents/Project/Newly_cropped/432_Cropped/'

imageName = []
imgListName = [i for i in os.listdir(directory)]

for file in os.listdir(directory):
    file_name, file_ext = os.path.splitext(file)
    print(file_name, '  ', file_ext)