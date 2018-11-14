import cv2
import os

directory = "/home/void/Desktop/Images/Band_5_4_3_Edit/Image_Manipulate_432/Segment_432/Current"

imageName = []
imgListName = [i for i in os.listdir(directory)]

for i in range(len(imgListName)) and os.listdir(directory):
    file_name, file_ext = os.path.splitext(i)
    year, month, day = file_name.split('_')
    new_name = '{}-{}-{}'.format(year, month, day)
    # os.rename(f, new_name)
    img = cv2.imread('Current/'+i)
    cv2.imshow(new_name, img)
    for ii in range(11):
        img_new_name = new_name + '_road_' + str(ii) + file_ext
        print(img_new_name)
        cv2.imwrite('New/'+img_new_name, img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()