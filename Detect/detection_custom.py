#================================================================
#
#   File name   : detection_custom.py
#   Author      : PyLessons
#   Created date: 2020-09-17
#   Website     : https://pylessons.com/
#   GitHub      : https://github.com/pythonlessons/TensorFlow-2.x-YOLOv3
#   Description : object detection image and video example
#
#================================================================
import os
import cv2
import numpy as np
import tensorflow as tf
from glob import glob
from yolov3.utils import detect_image, detect_realtime, detect_video, Load_Yolo_model, detect_video_realtime_mp, crop_image1
from yolov3.configs import *
from PIL import Image

os.environ['CUDA_VISIBLE_DEVICES'] = '0'
image_path = "Detect/IMAGES/data301.png"
video_path = "Detect/IMAGES/data1_detect.png"

Dataset_name = ['u', 'U', 'D', '2', 'X', '1', 'W', 'q', 'V', '7', 'J', 'k', 'I', 'm', 'N', 'C', '6', 'x', '8', 'F', 'O',
                'v', 'L', 'a', 'p', 'A', 'B', 'Q', 's', '5', 'R', '3', 'l', 'K', 'e', '9', 'n', 'j', 'T', 'f', 'c', 'r',
                'H', 'G', '4', 'P', 'o', 'Z', 'y', 'M', '', 'E', 'Y', 'w', 'z', 'S', 'b', '0', 'g', 'd', 'i', 't', 'J\\']


yolo = Load_Yolo_model()
# image = crop_image1(yolo, image_path, "D:/detect_hand.jpg", input_size=YOLO_INPUT_SIZE,
# show=False, CLASSES=TRAIN_CLASSES, resize=True, do_return=True)
# detect_image(yolo, image_path, "Detect/IMAGES/data1_detect.png", input_size=YOLO_INPUT_SIZE, show=False,
#              CLASSES=TRAIN_CLASSES, rectangle_colors=(255, 0, 0))
# crop_image1(yolo, image_path, "D:/test_detect.png", input_size=YOLO_INPUT_SIZE, show=False,
# CLASSES=TRAIN_CLASSES, resize=True)

# detect_video(yolo, video_path, './IMAGES/detected.mp4', input_size=YOLO_INPUT_SIZE, show=False,
# CLASSES=TRAIN_CLASSES, rectangle_colors=(255,0,0))

# detect_realtime(yolo, '', input_size=YOLO_INPUT_SIZE, show=True, CLASSES=TRAIN_CLASSES, rectangle_colors=(255, 0, 0))
# detect_video_realtime_mp(video_path, "Output.mp4", input_size=YOLO_INPUT_SIZE, show=True,
# CLASSES=TRAIN_CLASSES, rectangle_colors=(255,0,0), realtime=False)
# yolo.summary()

yolo.save('yolov4-tiny.h5')
# list_images = glob('IMAGES/Test_tiny1/*.png')
# print(list_images)
# for image_dir in list_images:
#     image_name = os.path.basename(image_dir)
#     image_path = image_dir
#
#     image, string_char = detect_image(yolo, image_path, '', input_size=YOLO_INPUT_SIZE, show=False,
#                  CLASSES=TRAIN_CLASSES, rectangle_colors=(255, 0, 0))
#     out_path = f"IMAGES/Test_tiny1/again{string_char}_{image_name}"
#     cv2.imwrite(out_path, image)
#     print(image_path)
