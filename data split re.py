import os
import glob
from sklearn.model_selection import train_test_split
import cv2
import numpy as np


def save_img(data, gender, age, mode):
    for path in data:
        image_name = os.path.basename(path)
        image_name = image_name.replace(".jpg", "")

        folder_path = f"./dataset/{mode}/{gender}+{age}"
        os.makedirs(folder_path, exist_ok=True)

        img = make_square_image(path)

        cv2.imwrite(os.path.join(folder_path, image_name + ".png"), img)


def make_square_image(image_path):
    origin_image = cv2.imread(image_path)

    try:
        height, width, channels = origin_image.shape
    except:
        print(image_path, '#' * 10)
        return

    x = height if height > width else width
    y = height if height > width else width

    if 224 > x and 224 > y:
        x, y = 224, 224

    squre_image = np.zeros((x, y, channels), np.uint8)
    squre_image[int((y - height) / 2):int(y - (y - height) / 2),
    int((x - width) / 2):int(x - (x - width) / 2)] = origin_image

    return squre_image


path = "./AFAD-Full"

all_labels = os.listdir(path)

for i in range(2, 8):
    globals()["all_M_image_" + str(i) + "0_" + str(i) + "9_path"] = []
    globals()["all_F_image_" + str(i) + "0_" + str(i) + "9_path"] = []

for i in range(20, 76):
    image_path = "./AFAD-Full/" + str(i)
    M_image_list = glob.glob(os.path.join(image_path, "111", "*.jpg"))
    F_image_list = glob.glob(os.path.join(image_path, "112", "*.jpg"))

    age = str(i)[0]
    globals()["all_M_image_" + str(age) + "0_" + str(age) + "9_path"].extend(M_image_list)
    globals()["all_F_image_" + str(age) + "0_" + str(age) + "9_path"].extend(F_image_list)

# all_M_image_20_29_path...


# 2. train, val, test 나누기
''' 이런 방법도 있습니다.
import splitfolders
splitfolders.ratio("path","저장경로",ratio=(.8,.1,.1),seed=7777)
'''
for i in range(2, 8):
    globals()[str(i) + "0_" + str(i) + "9_M_train_list"], globals()[
        str(i) + "0_" + str(i) + "9_M_val_list"] = train_test_split(
        globals()["all_M_image_" + str(i) + "0_" + str(i) + "9_path"], test_size=0.2, random_state=7)
    globals()[str(i) + "0_" + str(i) + "9_F_train_list"], globals()[
        str(i) + "0_" + str(i) + "9_F_val_list"] = train_test_split(
        globals()["all_F_image_" + str(i) + "0_" + str(i) + "9_path"], test_size=0.2, random_state=7)

for i in range(2, 8):
    # save_img(data,gender,age,mode)
    save_img(globals()[str(i) + "0_" + str(i) + "9_M_train_list"], "M", str(i) + "0_" + str(i) + "9", "train")
    save_img(globals()[str(i) + "0_" + str(i) + "9_M_val_list"], "M", str(i) + "0_" + str(i) + "9", "val")
    save_img(globals()[str(i) + "0_" + str(i) + "9_F_train_list"], "F", str(i) + "0_" + str(i) + "9", "train")
    save_img(globals()[str(i) + "0_" + str(i) + "9_F_val_list"], "F", str(i) + "0_" + str(i) + "9", "val")
