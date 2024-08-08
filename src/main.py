import os
import sys

import cv2
from PIL import Image


def image_to_ascii(image: Image, size: list[int] = (0, 0)) -> str:
    pixels = image.load()

    DENSITY = "$@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/\\|()1{}[]?-_+~<>i!lI;:,\"^`'. "
    DENSITY = DENSITY[::-1]

    if size[0] and size[1]:
        SIZE = size
    else:
        SIZE = [240, 80]

    WIDTH = image.width // SIZE[0] + 1
    HEIGHT = image.height // SIZE[1] + 1

    averages = [
        [0 for i in range(SIZE[0])] for j in range(SIZE[1])
    ]

    index_y = 0
    for y in range(image.height):
        index_x = 0
        for x in range(image.width):
            try:
                r, g, b, a = pixels[x, y]
            except ValueError:
                r, g, b = pixels[x, y]
            avg = (r + g + b) // 3

            averages[index_y][index_x] += avg

            if (x+1) % WIDTH == 0 and index_x < SIZE[0]-1:
                index_x += 1
        if (y+1) % HEIGHT == 0 and index_y < SIZE[1]-1:
            index_y += 1

    for y in range(len(averages)):
        for x in range(len(averages[y])):
            averages[y][x] /= WIDTH * HEIGHT

    string = ""
    for y in range(len(averages)):
        for x in range(len(averages[y])):
            index = int(averages[y][x]*70/255)
            while True:
                try:
                    string += DENSITY[index]
                    break
                except IndexError:
                    index -= 1
        string += "\n"

    return string


cam = cv2.VideoCapture("Rotating Donut.mp4")


while (True):
    ret, frame = cam.read()

    if ret:
        image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        image = Image.fromarray(image)
        string = image_to_ascii(image, [180, 40])
        os.system('cls')
        sys.stdout.write(string)
    else:
        break

cam.release()
cv2.destroyAllWindows()
