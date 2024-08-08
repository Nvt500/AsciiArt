from PIL import Image

DENSITY = "$@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/\\|()1{}[]?-_+~<>i!lI;:,\"^`'. "
DENSITY = DENSITY[::-1]


def image_to_ascii(image: Image) -> str:

    pixels = image.load()
    string = ""
    for y in range(image.height):
        for x in range(image.width):
            r, g, b, a = pixels[x, y]
            avg = (r + g + b) // 3
            string += DENSITY[int(avg * 70 / 255)]
        string += "\n"

    return string
