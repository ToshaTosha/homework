import os
import cv2
from skimage.measure import regionprops, label


def find_pencil(file):
    pencils = 0
    img = cv2.imread(f'images/{file}')
    gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    blur_img = cv2.GaussianBlur(gray_img, (5, 5), 0)
    _, threshold_img = cv2.threshold(blur_img, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
    binary_img = cv2.bitwise_not(threshold_img)
    labeled = label(binary_img)
    for region in regionprops(labeled):
        if region.perimeter > 2000 and 30 > (region.major_axis_length / region.minor_axis_length) > 15:
            pencils += 1

    return pencils


all_pencils = 0
files = os.listdir('images/')
for file in files:
    all_pencils += find_pencil(file)

print(all_pencils)
