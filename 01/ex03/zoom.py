from load_image import ft_load
import matplotlib.pyplot as plt


def main():

    try:
        data = ft_load("animal.jpeg")
        print(data)
        zoomed = data[100:500, 450:850, 0:1]
        print(f"New shape after licing: {zoomed.shape}")
        print(zoomed)
        plt.imshow(zoomed, cmap="gray")
        plt.show()
        return
    except FileNotFoundError:
        print("Error: the file was not found")
        return
    except Exception as e:
        print("An unexpected error occurred:", e)
        return


if __name__ == "__main__":
    main()
