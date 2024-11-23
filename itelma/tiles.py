import os

from numpy.ma.core import resize

os.environ["OPENCV_IO_MAX_IMAGE_PIXELS"] = str(pow(2, 40))
import cv2
import math


def split_image_to_tiles(input_image_path, output_dir, tile_size_x, tile_size_y):
    image = cv2.imread(input_image_path, cv2.IMREAD_UNCHANGED)
    height, width = image.shape[:2]

    x_tiles = math.ceil(width / tile_size_x)
    y_tiles = math.ceil(height / tile_size_y)

    os.makedirs(output_dir, exist_ok=True)

    for y in range(y_tiles):
        for x in range(x_tiles):
            x_start = x * tile_size_x
            y_start = y * tile_size_y
            x_end = min((x + 1) * tile_size_x, width)
            y_end = min((y + 1) * tile_size_y, height)

            # Crop the tile
            tile = image[y_start:y_end, x_start:x_end]

            # Save the tile
            tile_filename = os.path.join(output_dir, f"tile_{x}_{y}.png")
            cv2.imwrite(tile_filename, tile)

    del image


def downscale_image(input_image_path, size_x, size_y):
    image = cv2.imread(input_image_path, cv2.IMREAD_UNCHANGED)
    resized = cv2.resize(image, (size_x, size_y))

    del image
    return resized


cv2.imwrite("meow.png", downscale_image("image.png", 2000, 1000))
