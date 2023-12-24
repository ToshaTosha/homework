import cv2
import numpy as np
from skimage.measure import label, regionprops


def find_shapes_count(image_path):
    frame = cv2.imread(image_path)

    hsv_image = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    lower_bound = np.array([0, 0, 0])
    upper_bound = np.array([225, 200, 170])

    mask = cv2.inRange(hsv_image, lower_bound, upper_bound)

    inverted_mask = cv2.bitwise_not(mask)

    cropped_mask = inverted_mask[25:875, 25:875]

    regions = regionprops(label(cropped_mask))
    count_rect = 0
    count_circle = 0

    for region in regions:
        if region.area > 100:
            centroid = [region.centroid[0], region.centroid[1]]
            if region.eccentricity > 0.4:
                bbox = region.bbox
                cv2.rectangle(frame, (bbox[1], bbox[0]), (bbox[3], bbox[2]), (124, 255, 124))
                count_rect += 1
            else:
                bbox = region.bbox
                cv2.circle(frame, (round(centroid[1]), round(centroid[0])), (bbox[2] - bbox[0]) // 2, (124, 255, 124), 2)
                count_circle += 1

    cv2.imshow("Processed Image", frame)
    cv2.imshow("Mask", mask)

    print(f"Квадратов: {count_rect} \nКругов: {count_circle} ")

    while True:
        if cv2.waitKey(1) & 0xFF == ord('q'):
            cv2.destroyAllWindows()
            break

    return count_rect, count_circle

find_shapes_count("D8becq6Ew3Y.jpg")
