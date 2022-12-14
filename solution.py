#!/usr/bin/env python3

from typing import (
    List,
    Tuple,
    Union
)

from utils.image import (
    ImageType,
    PackedImage,
    StrideImage,
)

from utils.function_tracer import FunctionTracer
from utils.eye_pattern import EYE_PATTERN_1, EYE_PATTERN_2, EYE_PATTERN_3, EYE_PATTERN_4


def print_image(image):
    image_height = image.resolution.height
    image_width = image.resolution.width
    pixels_red = image.pixels_red
    for img_row in range(0, image_height):
        buffer = []
        for img_col in range(0, image_width):
            if pixels_red[image_width * img_row + img_col] >= 200:
                buffer.append("#")
            else:
                buffer.append("-")

        print(buffer)


def find_and_apply_pattern(pixels_in_channel, position, pattern, image_width):
    img_row, img_col = position
    pattern_width = len(pattern)
    pattern_height = len(pattern[0])

    found_pattern = True
    for pattern_x in range(0, pattern_width):
        for pattern_y in range(0, pattern_height):
            if pattern[pattern_x][pattern_y] == " ":
                continue
            if pixels_in_channel[image_width * (img_row + pattern_x) + img_col + pattern_y] < 200:
                found_pattern = False
                break
        if not found_pattern:
            break

    if found_pattern:
        # print(f"Found in position: {img_row, img_col}, pattern: {pattern[2][2]}")
        for pattern_x in range(0, pattern_width):
            for pattern_y in range(0, pattern_height):
                if pattern[pattern_x][pattern_y] == " ":
                    continue
                pixels_in_channel[image_width * (img_row + pattern_x) + img_col + pattern_y] -= 150


def compute_solution(images: List[Union[PackedImage, StrideImage]]):
    ft = FunctionTracer("compute_solution", "seconds")

    # images = [images[1]]

    for index, image in enumerate(images):
        image_height = image.resolution.height
        image_width = image.resolution.width
        pixels_red = image.pixels_red
        patterns = [EYE_PATTERN_3, EYE_PATTERN_1, EYE_PATTERN_2, EYE_PATTERN_4]
        # patterns = [EYE_PATTERN_1, EYE_PATTERN_2, EYE_PATTERN_3, EYE_PATTERN_4]

        print(f"Processing image: {index}")
        # print_image(image)

        for pattern in patterns:
            for img_row in range(0, image_height - len(pattern) + 1):
                for img_col in range(0, image_width - len(pattern[0]) + 1):
                    find_and_apply_pattern(pixels_in_channel=pixels_red,
                                           position=(img_row, img_col),
                                           pattern=pattern,
                                           image_width=image_width)

        # print_image(image)

    del ft
