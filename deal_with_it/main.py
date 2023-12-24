import cv2

cam = cv2.VideoCapture(0)
cv2.namedWindow("Camera", cv2.WND_PROP_FULLSCREEN)
cascade = cv2.CascadeClassifier("haarcascade_eye.xml")
glass = cv2.imread('deal_with_it.png', cv2.IMREAD_UNCHANGED)

while cam.isOpened():
    ret, frame = cam.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = cascade.detectMultiScale(gray)

    if len(faces) >= 2:  # Проверяем, что обнаружено хотя бы два глаза
        x1, y1, w1, h1 = faces[0]
        x2, y2, w2, h2 = faces[1]

        combined_width = w1 + (x2 - x1) + w2  # Вычисляем ширину для двух глаз и промежутка между ними

        glass_resized = cv2.resize(glass, (combined_width, max(h1, h2)))  # Масштабируем изображение под расстояние между глазами

        x_offset = x1  # Определяем смещение по горизонтали для первого глаза

        y_offset = min(y1, y2)  # Определяем смещение по вертикали для изображения

        frame[y_offset:y_offset + glass_resized.shape[0], x_offset:x_offset + glass_resized.shape[1]] = glass_resized  # Накладываем изображение на кадр

    cv2.imshow("Camera", frame)

    if cv2.waitKey(1) == ord('q'):
        break

cam.release()
cv2.destroyAllWindows()
