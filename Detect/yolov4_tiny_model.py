import tensorflow as tf
import keras
from yolov3.utils import *
from yolov3.configs import *
import cv2

model_directory = 'yolov4-tiny.h5'
Yolo = keras.models.load_model(model_directory)


def load_yolov4_tiny_model(model_path=model_directory):
    model = keras.models.load_model(model_path)
    model.summary()
    return model


def detect_image(image_path, input_size=416, CLASSES=TRAIN_CLASSES, score_threshold=0.6, iou_threshold=0.3):
    original_image = cv2.imread(image_path)
    original_image = cv2.cvtColor(original_image, cv2.COLOR_BGR2RGB)
    original_image = cv2.cvtColor(original_image, cv2.COLOR_BGR2RGB)

    image_data = image_preprocess(np.copy(original_image), [input_size, input_size])
    image_data = image_data[np.newaxis, ...].astype(np.float32)

    pred_bbox = Yolo.predict(image_data)
    pred_bbox = [tf.reshape(x, (-1, tf.shape(x)[-1])) for x in pred_bbox]
    pred_bbox = tf.concat(pred_bbox, axis=0)

    bboxes = postprocess_boxes(pred_bbox, original_image, input_size, score_threshold)
    bboxes = nms(bboxes, iou_threshold, method='soft-nms')

    # get string characters
    NUM_CLASS = read_class_names(CLASSES)
    num_classes = len(NUM_CLASS)
    print(NUM_CLASS)
    print(num_classes)
    new_bboxes = [box for box in bboxes if box[4] >= score_threshold]
    new_bboxes.sort(key=lambda x: (x[0] + x[2])/2)
    str = ''
    for b in new_bboxes:
        str += "{}".format(NUM_CLASS[int(b[5])])
    return str


if __name__ == '__main__':
    image_dir = 'IMAGES/data1.png'
    image = cv2.imread(image_dir)
    result = detect_image(yolo, image_dir)
    cv2.imshow(f'{result}', image)
    print(result)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
