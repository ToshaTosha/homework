import random

import cv2

capture = cv2.VideoCapture(0)
capture.set(cv2.CAP_PROP_AUTO_EXPOSURE, -2)
capture.set(cv2.CAP_PROP_EXPOSURE, 1)

cv2.namedWindow('Camera')

yellow_color = [(26, 100, 100), (46, 255, 255)]
blue_color = [(87, 100, 100), (107, 255, 255)]
green_color = [(64, 100, 100), (84, 255, 255)]

colors = [yellow_color, blue_color, green_color]
random.shuffle(colors)
print("Я загадал", colors)

prev_frame = [0, 0]
end_frame_time = 0

balls = []


def find_ball(frame, color):
    mask = cv2.inRange(hsv, color[0], color[1])
    mask = cv2.dilate(mask, None, iterations=2)
    cnts = cv2.findContours(mask.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)[-2]

    if len(cnts) > 0:
        # start_frame_time = time.perf_counter()
        c = max(cnts, key=cv2.contourArea)
        (x, y), radius = cv2.minEnclosingCircle(c)
        M = cv2.moments(c)
        center = (int(M["m10"] / M["m00"]), int(M["m01"] / M["m00"]))
        if radius > 10:
            cv2.circle(frame, (int(x), int(y)), int(radius), (0, 0, 0), 2)
            cv2.circle(frame, center, 5, (0, 0, 0), -1)

            return center
    return None


while capture.isOpened():
    ret, frame = capture.read()
    frame = cv2.GaussianBlur(frame, (11, 11), 0)
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    prev_frame_time = 0
    timee = 0
    balls = []
    for color in colors:
        ball = find_ball(frame, color)
        if ball is not None:
            balls.append((ball, color))

    if len(balls) == len(colors):
        prev_frame = [0, 0]
        sorted_arr = sorted(balls, key=lambda x: x[0])

        sorted_values = [item[1] for item in sorted_arr]

        # Затем используем zip() для проверки соответствия массивов
        match = all(arr1 == arr2 for arr1, arr2 in zip(sorted_values, colors))

        if match:
            print("Цвета в массиве colors соответствуют порядку в отсортированном массиве.")


    cv2.imshow("Camera", frame)
    key = cv2.waitKey(1)
    if key == ord("q"):
        break

capture.release()
cv2.destroyAllWindows()