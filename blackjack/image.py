import cv2
import os
import shutil
import numpy as np
import requests
import matplotlib.pyplot as plt

SAVE_IMG_PATH: str = 'image/'
DOWN_IMG_PATH: str = 'download/'
DOWN_URL: str = 'http://3156.bz/techgym/cards.jpg'
IMG_NAME: str = 'cards.jpg'
images: list = []


def download_image():
    res = requests.get(DOWN_URL)
    img = res.content
    with open(DOWN_IMG_PATH + IMG_NAME, 'wb') as f:
        f.write(img)


def split_image():
    rows: int = 4
    cols: int = 13
    img = cv2.imread(DOWN_IMG_PATH + IMG_NAME)
    
    images.clear()
    
    for row_img in np.array_split(img, rows, axis=0):
        for image in np.array_split(row_img, cols, axis=1):
            images.append(image)
    
    print(len(images))


def save_image():
    shutil.rmtree(SAVE_IMG_PATH)  # フォルダ全体を削除
    os.mkdir(SAVE_IMG_PATH)  # 新たなフォルダ作成
    for index, image in enumerate(images):
        image_name: str = SAVE_IMG_PATH + f'{index}.jpg'
        cv2.imwrite(image_name, image)

    
def load_image(num):
    img = cv2.imread(SAVE_IMG_PATH + f'{num}.jpg')
    return img 


def hunite_image(images: list):
    img = cv2.hconcat(images)
    return img
    

def vunite_image(images: list):
    img = cv2.vconcat(images)
    return img


def show_image(image):
    img = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    plt.figure(figsize=(6.0, 9.0), dpi=30)  # dpi * figsizeのピクセル数で表示される
    plt.axis('off')
    plt.imshow(img)
    plt.show(block=False)


def close_image():
    input('画像を閉じるにはEnterを押してください')
    plt.close()


def main():
    images = []
    images2 = []
    images3 = []
    img = None
    for index in range(3):
        img = load_image(index)
        images.append(img)
    for index in range(3):
        img = load_image(index)
        images2.append(img)
        
    img1 = hunite_image(images)
    img2 = hunite_image(images2)
    images3 = [img1, img2]
    img = vunite_image(images3)
    show_image(img)
    input('enter')
    close_image()
    

if __name__ == '__main__':
    main()