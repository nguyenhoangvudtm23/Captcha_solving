import xml.etree.ElementTree as ET
import numpy as np
import cv2
import os
from yolov3.utils import *
from yolov3.configs import *


def detection_to_xml(boxes, image_file, score_threshold=0.6):
    img = cv2.imread(image_file)
    height, width, channel = img.shape
    image_name = os.path.splitext(image_file)[0]
    xml_file = image_name + '.xml'
    root = ET.Element('annotation')

    # path, filename, folder
    file_split = image_file.split('/')
    folder = ET.SubElement(root, 'folder')
    folder.text = str(file_split[len(file_split) - 2])
    filename = ET.SubElement(root, 'filename')
    filename.text = str(file_split[-1])
    path = ET.SubElement(root, 'path')
    path.text = image_file
    # source node
    m1 = ET.Element('source')
    m11 = ET.SubElement(m1, 'database')
    m11.text = 'Unknown'
    root.append(m1)
    # size node
    m2 = ET.Element('size')
    m21 = ET.SubElement(m2, 'width')
    m21.text = str(width)
    m22 = ET.SubElement(m2, 'height')
    m22.text = str(height)
    m23 = ET.SubElement(m2, 'depth')
    m23.text = str(channel)
    root.append(m2)
    # segmented node
    m3 = ET.Element('segmented')
    m3.text = '0'
    root.append(m3)
    # object root
    for box in boxes:
        if box[4] < score_threshold:
            continue
        coor = np.array(box[:4], dtype=np.int32)
        (x1, y1), (x2, y2) = (coor[0], coor[1]), (coor[2], coor[3])
        m = ET.Element('object')
        m1 = ET.SubElement(m, 'name')
        m1.text = 'hand'
        m2 = ET.SubElement(m, 'pose')
        m2.text = 'Unspecified'
        m3 = ET.SubElement(m, 'truncated')
        m3.text = '0'
        m4 = ET.SubElement(m, 'difficult')
        m4.text = '0'
        # bndbox
        m5 = ET.SubElement(m, 'bndbox')
        # x, y min
        m51 = ET.SubElement(m5, 'xmin')
        m51.text = str(x1)
        m52 = ET.SubElement(m5, 'ymin')
        m52.text = str(y1)
        # x, y max
        m53 = ET.SubElement(m5, 'xmax')
        m53.text = str(x2)
        m54 = ET.SubElement(m5, 'ymax')
        m54.text = str(y2)
        # append to root
        root.append(m)

    tree = ET.ElementTree(root)
    with open(xml_file, 'wb') as file:
        tree.write(file)


if __name__ == '__main__':
    os.environ['CUDA_VISIBLE_DEVICES'] = '0'
    yolo = Load_Yolo_model()
    image_path = 'D:/Study/PythonPrj/pythonProject/TensorFlow-2.x-YOLOv3/IMAGES/test_hand1.jpg'
    boxes = detect_bboxes(yolo, image_path, YOLO_INPUT_SIZE)
    detection_to_xml(boxes, image_path)



