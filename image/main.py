import cv2
import numpy as np
import matplotlib.pyplot as plt


def main():
    img = cv2.imread('cat.jpg')
    #img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)  # グレースケール変換

    height = img.shape[0]
    width = img.shape[1]

    scale: float = 0.1
    scale2: float = 0.1
    img = cv2.resize(img, None, fx=scale, fy=scale2)
    img = cv2.resize(img, (width, height), interpolation=cv2.INTER_NEAREST)
    # img_list = np.array(img)

    cv2.imshow('image', img)
    cv2.waitKey(0)
    plt.imshow(img)
    plt.show()


if __name__ == '__main__':
    main()
