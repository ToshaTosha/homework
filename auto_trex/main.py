import pyautogui
import mss
import numpy as np
import time
import cv2
import pyautogui as pg

image_location = pyautogui.locateOnScreen('dino2.png')
left, top, width, height = image_location

distanceThreshold = 180


def process_image(original_image):
    processed_image = cv2.cvtColor(original_image, cv2.COLOR_BGR2GRAY)
    processed_image = cv2.Canny(processed_image, threshold1=200, threshold2=300)
    return processed_image

start_time = time.time()

def calculatedistanceThreshold():
    current_time = time.time()
    score = (current_time - start_time) * 10
    return score / 15000
 

def screen_record():
    sct = mss.mss()
    global distanceThreshold

    while True:
        distanceThreshold = distanceThreshold + calculatedistanceThreshold()
        BOX_COORD = {'top': top - 5, 'left': int(distanceThreshold), 'width': int(width / 2), 'height': height}

        img = sct.grab(BOX_COORD)
        img = np.array(img)
        processed_image = process_image(img)

        mean = np.mean(processed_image)

        if mean != float(0):
            pg.press('space')
            time.sleep(0.05)
            pg.press('down')


pg.press('space')
screen_record()
