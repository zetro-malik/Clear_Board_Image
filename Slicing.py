from stitch import run
import glob
from split_image import split_image
import cv2
import numpy as np
import os


def Run(img):

    if os.path.exists("Sliced_imgs\img1.png"):
        img1 = cv2.imread("Sliced_imgs\img1.png")
    else:
        img1 = np.zeros((500, 500), dtype=np.uint8)

    if os.path.exists("Sliced_imgs\img2.png"):
        img2 = cv2.imread("Sliced_imgs\img2.png")
    else:
        img2 = np.zeros((500, 500), dtype=np.uint8)

    if os.path.exists("Sliced_imgs\img3.png"):
        img3 = cv2.imread("Sliced_imgs\img3.png")
    else:
        img3 = np.zeros((500, 500), dtype=np.uint8)

    height = img.shape[0]
    width = img.shape[1]
    gap = (width * 7) // 100
    color_radius = ((img.shape[0]*img.shape[1])*4)//100
    sought = [0, 255, 255]

    # Find all pixels where the 3 NoTE ** BGR not RGB  values match "sought", and count
    result = np.count_nonzero(np.all(img == sought, axis=2))
    print(result)

    img11 = img[0:height, 0: ((width // 3) + (gap))]
    result1 = np.count_nonzero(np.all(img11 == sought, axis=2))
    if result1 < color_radius:
        img1 = img11
    img22 = img[0:height, ((width // 3) - gap): (((width // 3) + gap) * 2)]
    result2 = np.count_nonzero(np.all(img22 == sought, axis=2))
    if result2 < color_radius:
        img2 = img22
    img33 = img[0:height, (((width // 3) - gap-(gap//2)) * 2): width]
    result3 = np.count_nonzero(np.all(img33 == sought, axis=2))
    if result3 < color_radius:
        img3 = img33
