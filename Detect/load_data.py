import os
import numpy as np
import cv2
import random
from sklearn.utils import shuffle
from yolov3.utils import image_preprocess1, crop_image1
import pickle
from sklearn.model_selection import train_test_split

source_dir = '/home/linhdt/Downloads/team_detection_data/Full_data/'
out_dir = '/home/linhdt/Downloads/team_detection_data/Full_data_crop(5_3_2021)/'
if not os.path.exists(out_dir):
    os.mkdir(out_dir)


classes = {'01': 0, '02': 1, '03': 2, '04': 3, '05': 4, '06': 5, '07': 6, '08': 7, '09': 8, '10': 9, '11': 10, '12': 11,
           '13': 12, '14': 13, '15': 14, '16': 15, '17': 16, '18': 17, '19': 18, '20': 19, '21': 20, '22': 21,
           '23': 22, '24': 23, '25': 24, '26': 25, '27': 26, '28': 27, '29': 28, '30': 29, '31': 30, '32': 31}

t = 1
for person in os.listdir(source_dir):
    person_out_file = out_dir + person + '/'
    person_path = source_dir + person + '/'
    if not os.path.exists(person_out_file):
        os.mkdir(person_out_file)
    for gesture in os.listdir(person_path):
        ges_path = person_path + gesture
        ges_out_path = person_out_file + gesture + '/'
        if not os.path.exists(ges_out_path):
            os.mkdir(ges_out_path)
        for subject in os.listdir(ges_path):
            sub_path = ges_path + subject + '/'
            for image in os.listdir(sub_path):
                temp = os.path.splitext(image)
                image_path = sub_path + image + '/'
                try:
                    cv2.imread(image)
                    num = str(random.randint(0, 100))
                    out_img_dir = out_dir + temp[0] + num + temp[1]
                    print(out_img_dir)
                    crop_image1(yolo, img_path, out_img_dir, input_size=YOLO_INPUT_SIZE, show=False,
                                CLASSES=TRAIN_CLASSES)
                    print(t)
                    t += 1
                except PIL.Uni
                except:
                    print("error")
                    pass






