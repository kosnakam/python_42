from load_image import ft_load
import matplotlib.pyplot as plt
from PIL import Image
import numpy as np


def ft_zoom(arg: list) -> list:
    """This function slices image, show it and return the np.array"""
    try:
        assert type(arg) is np.ndarray, "This argument is not accepted."

        img = Image.fromarray(arg).convert('L').crop((450, 100, 850, 500))
        # plt.imshow(img, cmap='gray')
        # plt.show()

        arr = np.array(img)
        arr_3d = arr[:, :, np.newaxis]

        print(f"New shape after slicing: {arr_3d.shape} or {arr.shape}")

    except AssertionError as e:
        print(f"Error(ft_zoom): {e}")
        return None

    return arr_3d


def ft_rotate(arg: list) -> list:
    try:
        assert type(arg) is np.ndarray, "This argument is not accepted."

        img = Image.fromarray(np.squeeze(arg, axis=2)).rotate(90).transpose(Image.FLIP_TOP_BOTTOM)
        plt.imshow(img, cmap='gray')
        plt.show()

        arr = np.array(img)
        print(f"New shape after Transpose: {arr.shape}")

    except AssertionError as e:
        print(f"Error(ft_rotate): {e}")
        return None

    return arr


def main():
    im = ft_load("animal.jpeg")
    # print(im)

    zoomed = ft_zoom(im)
    print(zoomed)

    rotated = ft_rotate(zoomed)
    print(rotated)

    return


if __name__ == "__main__":
    main()
