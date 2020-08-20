import matplotlib.pyplot as plt
import cv2
import sys


def he(img):
    img_yuv = cv2.cvtColor(img, cv2.COLOR_RGB2YUV)
    img_yuv[:, :, 0] = cv2.equalizeHist(img_yuv[:, :, 0])
    out = cv2.cvtColor(img_yuv, cv2.COLOR_YUV2RGB)
    return out


def main():
    img_name = sys.argv[1]
    img = cv2.cvtColor(cv2.imread(img_name), cv2.COLOR_BGR2RGB)
    result = he(img)
    plt.imshow(result)
    plt.show()


if __name__ == '__main__':
    main()
