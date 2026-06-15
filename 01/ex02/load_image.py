import numpy as np
from PIL import Image

def ft_load(path: str): 

    img = Image.open(ex02/animal.jpeg)
    array = np.array(img)

    print(array.shape)

    if not path.endwith(".jpg") or not path.endswith(".jpeg"):
        raise TypeError("image's format must be jpg or jpeg")
    