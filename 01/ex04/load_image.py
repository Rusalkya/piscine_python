"""Image loader module."""

import numpy as np
from PIL import Image


def ft_load(path: str):
    """Load image, extract the square crop, and print it."""
    if not isinstance(path, str):
        raise TypeError("path must be a string")

    if not path.endswith((".jpg", ".jpeg")):
        raise TypeError("image format must be jpg or jpeg")

    img = Image.open(path)
    array = np.array(img)

    if array.ndim == 3:
        cropped = array[100:500, 450:850, 0:1]
    else:
        cropped = array[100:500, 450:850]

    print(f"The shape of image is: {cropped.shape}")
    print(cropped)

    return cropped
