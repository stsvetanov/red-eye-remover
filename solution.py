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
from utils.eye_pattern import EYE_PATTERN_1


# Might increase the performance if used
# from bitmap import BitMap
# pattern_1 = [
#     BitMap.fromstring("11111"),
#     BitMap.fromstring("10001"),
#     BitMap.fromstring("11111"),
#     BitMap.fromstring("10001"),
#     BitMap.fromstring("11111")
# ]

def find_and_apply_pattern(pixels_in_channel, position, pattern, image_width):

    row_pointer, cow_pointer = position
    pattern_width = len(pattern)
    pattern_height = len(pattern[0])

    for pattern_x in range(row_pointer, row_pointer + pattern_width):
        for pattern_y in range(cow_pointer, cow_pointer + pattern_height):
            if EYE_PATTERN_1[pattern_x - row_pointer][pattern_y - cow_pointer] == " ":
                continue
            else:
                if pixels_in_channel[image_width * row_pointer + cow_pointer] < 200:
                    return False
                else:
                    pixels_in_channel[image_width * row_pointer + cow_pointer] -= 150

    return pixels_in_channel


def compute_solution(images: List[Union[PackedImage, StrideImage]]):
    ft = FunctionTracer("compute_solution", "seconds")

    # TODO fill solution

    for index, image in enumerate(images):
        image_height = image.resolution.height
        image_width = image.resolution.width
        pixels_red = image.pixels_red
        pattern_width = len(EYE_PATTERN_1)
        pattern_height = len(EYE_PATTERN_1[0])

        print(f"Processing image: {index}")

        for row_pointer in range(0, image_height - pattern_height):
            for cow_pointer in range(0, image_width - pattern_width):

                updated_pixels = find_and_apply_pattern(pixels_in_channel=pixels_red,
                                                        position=(row_pointer, cow_pointer),
                                                        pattern=EYE_PATTERN_1,
                                                        image_width=image_width)

                if updated_pixels:
                    print(f"Patterns found in image: {index}")
                    images[index].pixels_red = updated_pixels

    del ft
