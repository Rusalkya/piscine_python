"""Image loader module."""

import numpy as np
from PIL import Image


def ft_load(path: str):
    """Load image and return numpy array."""
    try:
        if not isinstance(path, str):
            raise TypeError("path must be a string")

        if not path.endswith((".jpg", ".jpeg")):
            raise TypeError("image format must be jpg or jpeg")

        img = Image.open(path)
        array = np.array(img)

        print("The shape of image is: ", array.shape)
        print(array)

        return array

    finally:
        pass
