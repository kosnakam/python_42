from PIL import Image
import numpy as np


def ft_load(path: str) -> list:
    """This function loads path and analyzes the shape."""
    try:
        assert type(path) is str, "This argument is not accepted."

        im = Image.open(path)
        ret = np.array(im)
        print(f"The shape of image is: {ret.shape}")
        print(ret)

    except (AssertionError, FileNotFoundError) as e:
        print(f"Error(ft_load): {e}")
        return None
    return ret
