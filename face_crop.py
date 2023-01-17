import os

import cv2
import mediapipe as mp

mp_face_detection = mp.solutions.face_detection
mp_drawing = mp.solutions.drawing_utils

IMAGE_FILES = []


def face_crop(file_path):
    with mp_face_detection.FaceDetection(model_selection=1, min_detection_confidence=0.5) as face_detection:
        image = cv2.imread(file_path)

        results = face_detection.process(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))

        if not results.detections:
            print(f'{file_path} >> 얼굴을 찾지 못함')
            os.remove(file_path)
            return
        h, w, c = image.shape
        for detection in results.detections:
            bbox = detection.location_data.relative_bounding_box
            if bbox.xmin < 0:
                bbox.xmin = 0
            if bbox.ymin < 0:
                bbox.ymin = 0
            crop_img = image[int(bbox.ymin * h): int((bbox.ymin + bbox.height) * h),
                       int(bbox.xmin * w): int((bbox.xmin + bbox.width) * w)]
            print(bbox)
            return crop_img
