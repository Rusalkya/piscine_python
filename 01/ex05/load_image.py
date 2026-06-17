"""Image loader module."""

from pathlib import Path

import numpy as np
from PIL import Image


def ft_load(path: str):
    """Load an image and print its shape and content."""
    if not isinstance(path, str):
        raise TypeError("path must be a string")

    if not path.endswith((".jpg", ".jpeg")):
        raise TypeError("image format must be jpg or jpeg")

    image_path = Path(path)
    if not image_path.is_absolute() and not image_path.exists():
        image_path = Path(__file__).with_name(path)

    img = Image.open(image_path)
    array = np.array(img)

    print(f"The shape of image is: {array.shape}")
    print(array)

    return array
