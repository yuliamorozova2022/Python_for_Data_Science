import atexit
from PIL import Image
import numpy as np
import matplotlib.pyplot as plt

# Blocking show registered once here — runs on script exit regardless
# of which functions were called or in what order.
atexit.register(plt.show)


def print_img_arr(array, string, print_array=True):
    """Helper function to print the image with a title."""
    if print_array:
        print(array)
    plt.figure(string)
    plt.imshow(array)
    plt.axis("off")
    # plt.show()  # is essential so all image windows will be kept open


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

    # convertion to RGB just to be sure
    img = img.convert("RGB")
    # convertion to numpy array
    arr = np.array(img)
    print(f"The shape of image is: {arr.shape}")
    # print(arr)
    print_img_arr(arr, "Figure VIII.1: Original", False)
    return arr
