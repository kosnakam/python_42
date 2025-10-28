from load_image import ft_load
import matplotlib.pyplot as plt
from PIL import Image
import numpy as np


def ft_grey(arg: list) -> list:
    """This function converts the argument to grayscale."""
    height, width, _ = arg.shape
    grey = np.zeros((height, width), dtype=np.uint8)

    for i in range(height):
        for j in range(width):
            r = arg[i, j, 0]
            g = arg[i, j, 1]
            b = arg[i, j, 2]
            val = r * 0.2989 + g * 0.5870 + b * 0.1140
            grey[i, j] = int(val)
    return grey


def ft_zoom(arg: np.ndarray) -> np.ndarray:
    """This function slices image, show it and return the np.array"""
    try:
        assert isinstance(arg, np.ndarray), "This argument is not accepted."

        arr = ft_grey(arg[100:500, 450:850])
        arr_3d = arr[:, :, np.newaxis]

        img = Image.fromarray(arr)
        plt.imshow(img, cmap='gray')
        plt.show()

        print(f"New shape after slicing: {arr_3d.shape} or {arr.shape}")
        return arr_3d

    except AssertionError as e:
        print(f"Error(ft_zoom): {e}")
        return None


def main():
    img = ft_load("animal.jpeg")
    print(img)

    zoomed = ft_zoom(img)
    print(zoomed)
    return


if __name__ == "__main__":
    main()
