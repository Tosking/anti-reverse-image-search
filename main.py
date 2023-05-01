#!/usr/bin/env python3

from PIL import Image
import sys
import random

NOISE_D = 50

def image_handler(path):
    image = Image.open(path)
    return image

def create_noise(image):
    width, height = image.size
    for x in range(width):
        for y in range(height):
            cur_color = image.getpixel((x, y))
            noise = random.randint(-NOISE_D, NOISE_D) + 50
            new_color = (cur_color[0] + noise, cur_color[1] + noise, cur_color[2] + noise)
            image.putpixel((x, y), new_color)
    return image

def resize_image(image):
    return image.resize((round(image.size[0] * 0.5), round(image.size[1] * 0.5)), Image.LANCZOS)

def save_image(image, path):
    sliced = path.split(".")
    sliced[-1] = "_redacted." + sliced[-1]
    path = ''.join(sliced)
    image.save(path, quality=35)



if __name__ == "__main__":
    image = image_handler(sys.argv[1])
    if len(sys.argv) >= 3:
        NOISE_D = int(sys.argv[2])
    image = create_noise(image)
    image = resize_image(image)
    save_image(image, sys.argv[1])
