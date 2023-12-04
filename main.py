import numpy as np
import matplotlib.pyplot as plt
from skimage.measure import label, regionprops

balls_trajectories = {
    'obj0': {'x': [], 'y': []},
    'obj1': {'x': [], 'y': []},
    'obj2': {'x': [], 'y': []}
}


def find_obj(path: str):
    image = np.load(path)
    labeled = label(image)
    regions = regionprops(labeled)
    regions_list = list(regions)
    n = len(regions_list)

    for i in range(n):
        for j in range(0, n - i - 1):
            if regions_list[j].area > regions_list[j + 1].area:
                regions_list[j], regions_list[j + 1] = regions_list[j + 1], regions_list[j]

    sorted_regions = regions_list

    for idx, obj in enumerate(balls_trajectories.keys()):
        origins = sorted_regions[idx].centroid
        balls_trajectories[obj]['x'].append(origins[0])
        balls_trajectories[obj]['y'].append(origins[1])


for i in range(100):
    find_obj(f'out/h_{i}.npy')


for ball_name, trajectory in balls_trajectories.items():
    plt.plot(trajectory['x'], trajectory['y'], label=ball_name)
plt.legend()
plt.show()
