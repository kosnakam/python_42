from load_image import ft_load
import matplotlib.pyplot as plt
from PIL import Image
import numpy as np


def ft_zoom(arg: list) -> list:
    """This function slices image, show it and return the np.array"""
    try:
        assert type(arg) is np.ndarray, "This argument is not accepted."

        region = Image.fromarray(arg).convert('L').crop((450, 100, 850, 500))
        plt.imshow(region, cmap='gray')
        plt.show()

        arr = np.array(region)
        arr_3d = arr[:, :, np.newaxis]

        print(f"New shape after slicing: {arr_3d.shape} or {arr.shape}")

    except AssertionError as e:
        print(f"Error(ft_zoom): {e}")
        return None

    return (arr_3d)


def main():
    im = ft_load("animal.jpeg")
    print(im)

    zoomed = ft_zoom(im)
    print(zoomed)

    return


if __name__ == "__main__":
    main()
