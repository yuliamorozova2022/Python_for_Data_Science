from PIL import Image
import numpy as np


# np.ndarray - type of return object
def ft_load(path: str) -> np.ndarray:
    """Load an image from a file.
    Prints its format and returns its pixels as a numpy array.
    Supports JPG/JPEG files."""
    # open file
    try:
        img = Image.open(path)
    except FileNotFoundError:
        print(f"Error: file '{path}' not found.")
        return np.array([])
    except Exception as e:
        print(f"Error: cannot open the file '{path}': {e}")
        return np.array([])

    # check file format
    if img.format not in ['JPEG', 'JPG']:
        print(f"Error: image format '{img.format}' is not supported.")
        return np.array([])

    # in PIL img.size has format (WIDTH, HEIGHT), but for task
    # height has to be printed first
    # that's why size[::-1] is used - to revert order (height, width)

    # (3,) is appended to indicate RGB channels. (3,) is a tuple;
    # (3) alone is an int and cannot be concatenated with a tuple
    # (will cause TypeError)
    # (1,) or (3,) is specific syntax for tuple with only one element
    # print(f"The shape of image is: {img.size[::-1] + (3,)}")

    # convertion to RGB just to be sure
    img = img.convert("RGB")

    # convertion to numpy array and returning
    return np.array(img)
