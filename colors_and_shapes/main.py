import matplotlib.pyplot as plt
import cv2
import numpy as np
from skimage.measure import label, regionprops

image = plt.imread("balls_and_rects.png")
hsv = cv2.cvtColor(image, cv2.COLOR_RGB2HSV)
image_mean = np.mean(image, axis=2)
binary = image_mean > 0


def clustering(colors):
    clusters = []
    while colors:
        item = colors.pop(0)
        cluster = [item]
        similar_colors = [color for color in colors if abs(item - color) < 5]
        for color in similar_colors:
            cluster.append(color)
            colors.remove(color)
        clusters.append(cluster)
    return clusters


labeled = label(binary)
regions = regionprops(labeled)

all_count = np.max(labeled)
print(f"Всего: {all_count}")

rect = []
circle = []
h = hsv[:, :, 0]

for region in regions:
    r = h[region.bbox[0]:region.bbox[2], region.bbox[1]:region.bbox[3]]
    if len(np.unique(r)) == 1:
        rect.extend(np.unique(r))
    else:
        circle.extend(np.unique(r)[1:2])

rect_count = len(rect)
circle_count = len(circle)

print(f"Всего квадратов: {rect_count}, всего кругов: {circle_count}")

rect_cluster = clustering(rect)
circle_cluster = clustering(circle)

for i in range(len(rect_cluster)):
    idx = [[j for k in circle_cluster[j] if int(k) == int(rect_cluster[i][0])] for j in range(len(circle_cluster))]
    idx = [i[0] for i in idx if i][0]
    print(f"Оттенок: {int(rect_cluster[i][0])}, Прямоугольников: {len(rect_cluster[i])}, Кругов: {len(circle_cluster[idx])}")

