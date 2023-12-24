import cv2
import numpy as np


def match_template_in_video(template_image_path, video_path, match_threshold=0.7):
    count = 0
    all_images = 0
    video = cv2.VideoCapture(video_path)
    template_img = cv2.imread(template_image_path, cv2.IMREAD_GRAYSCALE)

    while True:
        _, frame = video.read()
        if frame is None:
            break
        frame_gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        match_result = cv2.matchTemplate(frame_gray, template_img, cv2.TM_CCOEFF_NORMED)
        loc = np.where(match_result >= match_threshold)
        if loc[0].size > 0:
            count += 1
            cv2.imshow('Matched Frame', frame)
            cv2.waitKey(0)
        all_images += 1

    video.release()
    print(f"Моё изображение в видео: {count}")


template_path = 'img.jpg'
video_path = 'output.avi'
match_template_in_video(template_path, video_path)
