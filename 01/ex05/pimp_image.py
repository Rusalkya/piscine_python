"""Image color filter module."""

import builtins

import numpy as np
import matplotlib.pyplot as plt


def ft_invert(array) -> np.ndarray:
    """Inverts the color of the image received."""
    result = array.copy()
    if result.ndim == 3 and result.shape[2] >= 3:
        result[:, :, 0] = 255 - result[:, :, 0]
        result[:, :, 1] = 255 - result[:, :, 1]
        result[:, :, 2] = 255 - result[:, :, 2]
        plt.imshow(result)
        plt.axis("off")
        plt.show()
    return result


def ft_red(array) -> np.ndarray:
    """Keeps only the red channel of the image received."""
    result = array.copy()
    if result.ndim == 3 and result.shape[2] >= 3:
        result[:, :, 1] = 0
        result[:, :, 2] = 0
    return result


def ft_green(array) -> np.ndarray:
    """Keeps only the green channel of the image received."""
    result = array.copy()
    if result.ndim == 3 and result.shape[2] >= 3:
        result[:, :, 0] = result[:, :, 0] - result[:, :, 0]
        result[:, :, 2] = result[:, :, 2] - result[:, :, 2]
    return result


def ft_blue(array) -> np.ndarray:
    """Keeps only the blue channel of the image received."""
    result = array.copy()
    if result.ndim == 3 and result.shape[2] >= 3:
        result[:, :, 0] = 0
        result[:, :, 1] = 0
    return result


def ft_grey(array) -> np.ndarray:
    """Converts the image to grayscale."""
    result = array.copy()
    if result.ndim == 3 and result.shape[2] >= 3:
        grey = (
            result[:, :, 0].astype(np.uint16)
            + result[:, :, 1].astype(np.uint16)
            + result[:, :, 2].astype(np.uint16)
        ) / 3
        result[:, :, 0] = grey
        result[:, :, 1] = grey
        result[:, :, 2] = grey
    return result


builtins.ft_red = ft_red
builtins.ft_green = ft_green
builtins.ft_blue = ft_blue
builtins.ft_grey = ft_grey
