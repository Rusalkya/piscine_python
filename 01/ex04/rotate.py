from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np

from load_image import ft_load


def transpose_image(image: np.ndarray) -> np.ndarray:
    transposed = np.zeros((image.shape[1], image.shape[0]), dtype=image.dtype)
    for row in range(image.shape[0]):
        for col in range(image.shape[1]):
            transposed[col, row] = image[row, col]
    return transposed


def main():
    try:
        image_path = Path(__file__).with_name("animal.jpeg")
        square = ft_load(str(image_path))
        transposed = transpose_image(np.squeeze(square))
        print(f"New shape after Transpose: {transposed.shape}")
        print(transposed)
        plt.imshow(transposed, cmap="gray")
        plt.axis("off")
        plt.savefig(Path(__file__).with_name("rotate.png"), bbox_inches="tight", pad_inches=0)
        if "agg" not in plt.get_backend().lower():
            plt.show()
    except FileNotFoundError:
        print("Error: the file was not found")
    except Exception as e:
        print("An unexpected error occurred:", e)


if __name__ == "__main__":
    main()
