import os

# gt_image_2
directory = "/home/megan/Documents/Thesis/semantic-segmentation-master/data/data_road/training/gt_image_2"

# image_2
directory_ = "/home/megan/Documents/Thesis/semantic-segmentation-master/data/data_road/training/image_2"
os.chdir(directory_)

for f in os.listdir():
    file_name, file_ext = os.path.splitext(f)

    # gt_image_2

    """
    print(file_name + '___' + file_ext)
    gr, road, year, month, day, num = file_name.split('_')
    new_name = '{}-{}-{}_{}_{}{}'.format(year, month, day, road, num, file_ext)
    os.rename(f, new_name)
    """
    # image_2

    year, month, day, num = file_name.split('_')
    new_name = '{}-{}-{}_{}{}'.format(year, month, day,num, file_ext)
    os.rename(f, new_name)
    print(new_name)