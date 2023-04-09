from Stitching import Stitching
import cv2
import numpy as np
import os

img1 = np.zeros((500, 500), dtype=np.uint8)
img2 = np.zeros((500, 500), dtype=np.uint8)
img3 = np.zeros((500, 500), dtype=np.uint8)


# Get a list of all the files in the folder
count = 0
# Loop through each file
for i in range(500, 35500, 500):
    if i > 34000:
        break

    if not os.path.exists(f'ds\_frame_{i}.jpg'):
        continue

    print(f'ds\_frame_{i}.jpg')
    img = cv2.imread(f'ds\_frame_{i}.jpg')

    height = img.shape[0]
    width = img.shape[1]
    count += 1
    gap = (width * 7) // 100
    color_radius = ((img.shape[0]*img.shape[1])*4)//100
    sought = [0, 255, 255]

    # Find all pixels where the 3 NoTE ** BGR not RGB  values match "sought", and count
    result = np.count_nonzero(np.all(img == sought, axis=2))

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

    cv2.imwrite('Sliced_imgs\img1.png', img1)
    cv2.imwrite('Sliced_imgs\img2.png', img2)
    cv2.imwrite('Sliced_imgs\img3.png', img3)


# Now, stitching the most updated slices together
Stitching()
