from load_image import ft_load
import matplotlib.pyplot as plt


def zoom_image(array):

    height, width = array.shape[0], array.shape[1]

    zoom = array[
        height // 4: 3 * height // 4,
        width // 4: 3 * width // 4
    ]

    print(f"New shape after slicing: {zoom.shape}")

    return zoom


if __name__ == "__main__":
    img = ft_load("animal.jpeg")

    if img is not None:
        zoom = zoom_image(img)
        print(zoom)
        
        # Display the zoomed image with matplotlib
        plt.imshow(zoom, cmap='gray')
        plt.show()
