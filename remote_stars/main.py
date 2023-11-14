import socket
import matplotlib.pyplot as plt
import numpy as np
from skimage.measure import label, regionprops
import math


def recvall(sock, n):
    data = bytearray()
    while len(data) < n:
        packet = sock.recv(n - len(data))
        if not packet:
            return None
        data.extend(packet)
    return data


host = "84.237.21.36"
port = 5152

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
    beat = b'nope'
    sock.connect((host, port))
    while beat != b'yep':
        sock.send(b"get")

        bts = recvall(sock, 40002)

        im = np.frombuffer(bts[2:], dtype="uint8").reshape(bts[0], bts[1])

        im[im > 1] = 1
        regions = regionprops(label(im))
        x_one, y_one = regions[0].centroid
        x_two, y_two = regions[1].centroid

        distance = round(math.sqrt((x_two - x_one) ** 2 + (y_two - y_one) ** 2), ndigits=1)
        print(distance)

        sock.send(f"{distance}".encode())
        print(sock.recv(4).decode())

        plt.clf()
        plt.title(str({x_one, y_one}) + str({x_two, y_two}))
        plt.imshow(im)
        plt.pause(1)

        sock.send(b'beat')
        beat = sock.recv(20)



