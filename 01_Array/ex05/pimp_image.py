import numpy as np
from PIL import Image
import matplotlib.pyplot as plt


def ft_invert(arg: list) -> list:
    """Inverts the color of the image received."""
    try:
        assert type(arg) is np.ndarray, "This argument is not accepted."

        ret = 255 - arg

        img = Image.fromarray(ret)
        plt.imshow(img)
        plt.show()
        return ret

    except AssertionError as e:
        print(f"Error(ft_invert): {e}")
        return None


def ft_red(arg: list) -> list:
    """Set all color components except red to zero."""
    try:
        assert type(arg) is np.ndarray, "This argument is not accepted."

        ret = arg.copy()

        ret[:, :, 1] = arg[:, :, 1] * 0
        ret[:, :, 2] = arg[:, :, 2] * 0

        img = Image.fromarray(ret)
        plt.imshow(img)
        plt.show()
        return ret

    except AssertionError as e:
        print(f"Error(ft_red): {e}")
        return None


def ft_green(arg: list) -> list:
    """Set all color components except green to zero."""
    try:
        assert type(arg) is np.ndarray, "This argument is not accepted."

        ret = arg.copy()

        ret[:, :, 0] = arg[:, :, 0] - arg[:, :, 0]
        ret[:, :, 2] = arg[:, :, 2] - arg[:, :, 2]

        img = Image.fromarray(ret)
        plt.imshow(img)
        plt.show()
        return ret

    except AssertionError as e:
        print(f"Error(ft_green): {e}")
        return None


def ft_blue(arg: list) -> list:
    """Set all color components except blue to zero."""
    try:
        assert type(arg) is np.ndarray, "This argument is not accepted."
    
        ret = arg.copy()

        ret[:, :, 0] = 0
        ret[:, :, 1] = 0

        img = Image.fromarray(ret)
        plt.imshow(img)
        plt.show()
        return ret

    except AssertionError as e:
        print(f"Error(ft_blue): {e}")
        return None


def ft_grey(arg: list) -> list:
    """Display in grayscale."""
    try:
        assert type(arg) is np.ndarray, "This argument is not accepted."
            
        height, width, _ = arg.shape
        grey = np.zeros((height, width), dtype=np.uint8)

        for i in range(height):
            for j in range(width):
                r = arg[i, j, 0]
                g = arg[i, j, 1]
                b = arg[i, j, 2]
                val = r * 0.2989 + g * 0.5870 + b * 0.1140
                grey[i, j] = int(val)

        img = Image.fromarray(grey)
        plt.imshow(img, cmap='gray')
        plt.show()
        return grey

    except AssertionError as e:
        print(f"Error(ft_grey): {e}")
