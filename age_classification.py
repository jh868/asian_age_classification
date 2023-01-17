import os
import glob
import cv2
from padding import padding

# aihub 데이터 나이대, 역할 별 split, padding & resize
path = './data/'
complete_path = './dataset/'

image_path_list = glob.glob(os.path.join(path, '*', '*', '*', '2.Individuals', '*.jpg'))
# print(image_path_list)

for idx, image_path in enumerate(image_path_list):
    age = int(image_path.split('_')[3])
    role = image_path.split('_')[2]

    if int(age) < 40:
        pass
    else:
        age_range = int(age/10)

        os.makedirs(complete_path + f'{role}/' + f'{age_range*10}', exist_ok=True)
        img = cv2.imread(image_path)
        img = padding(img, 600)
        cv2.imwrite(complete_path + f'{role}/' + f'{age_range*10}/' + f'{role}_{age_range*10}_{idx}.png', img)
