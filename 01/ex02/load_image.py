import numpy as np
from PIL import Image


def ft_load(path: str):

    if not path.endswith((".jpg", ".jpeg")):
        raise TypeError("Image's format must be a .jpg or .jpeg.")

    try:
        img = Image.open(path)
    except Exception:
        raise FileNotFoundError("Image doesn't exist.")

    array = np.array(img)

    print(f"The shape of image is: {array.shape}")

    return array
