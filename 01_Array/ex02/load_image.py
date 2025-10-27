from PIL import Image
import numpy as np


def ft_load(path: str) -> list:
    """This function loads path and analyzes the shape."""
    try:
        assert type(path) is not None, "This argument is not accepted."

        img = Image.open(path)
        arr = np.array(img)
        print(f"The shape of image is: {arr.shape}")

    except (AssertionError, FileNotFoundError) as e:
        print(f"Error(ft_load): {e}")
        return None
    return arr
