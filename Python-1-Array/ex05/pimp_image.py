import numpy as np
from load_image import print_img_arr

# You have some restriction operators for each function
# (you can only use those given, you don’t have to use them all)


def ft_invert(array) -> np.ndarray:
    """Inverts the color of the image received."""
    # restriction operators: =, +, -, *
    if array.size == 0:
        return array
    # Invert the image by subtracting each pixel value from 255 (dark -> light)
    result = 255 - array
    print_img_arr(result, "Figure VIII.2: Invert")
    return result


def ft_red(array) -> np.ndarray:
    """Keep only the red channel of the image (green and blue set to 0).
    param array: numpy array (height, width, 3) representing the RGB image
    return: numpy array (height, width, 3) with only the
    red channel preserved."""
    # restriction operators: =, *
    if array.size == 0:
        return array
    # multiplying the whole array by [1, 0, 0] will keep onlythe red
    # channel values, setting green and blue to 0 in one shot.
    result = array * np.array([[[1, 0, 0]]], dtype=array.dtype)
    # [np.array([[[1, 0, 0]]], dtype=array.dtype)] creates the mask with uint8
    # values instead of the default int64 (-> result = array * [[[1, 0, 0]]])
    # pixel values must be whole numbers 0–255, so uint8 is required
    print_img_arr(result, "Figure VIII.3: Red")
    return result


def ft_green(array) -> np.ndarray:
    """Keep only the green channel of the image (red and blue set to 0).
    param array: numpy array (height, width, 3) representing the RGB image
    return: numpy array (height, width, 3) with only the
    green channel preserved."""
    # restriction operators: =, -
    if array.size == 0:
        return array
    # Copies the array, so original array remains unchanged, then zeroes red
    # and blue by subtracting each channel from itself.
    result = array.copy()
    result[:, :, 0] = result[:, :, 0] - result[:, :, 0]  # zeroes red channel
    result[:, :, 2] = result[:, :, 2] - result[:, :, 2]  # zeroes blue channel
    print_img_arr(result, "Figure VIII.4: Green")
    return result


def ft_blue(array) -> np.ndarray:
    """Keep only the blue channel of the image (red and green set to 0).
    param array: numpy array (height, width, 3) representing the RGB image
    return: numpy array (height, width, 3) with only the
    blue channel preserved."""
    # restriction operators: =
    if array.size == 0:
        return array
    # Copies the array, so original array remains unchanged and directly
    # assigns 0 to the red and green channels.
    result = array.copy()
    result[:, :, 0] = 0
    result[:, :, 1] = 0
    print_img_arr(result, "Figure VIII.5: Blue")
    return result


def ft_grey(array) -> np.ndarray:
    """Convert the image to greyscale by averaging the RGB channels,
    returning a (height, width, 3) array where all channels
    hold the grey value.
    param array: numpy array (height, width, 3) representing the RGB image
    return: numpy array (height, width, 3) representing the greyscale image."""
    # restriction operators: =, /
    if array.size == 0:
        return array
    result = array.copy()
    grey = (result.sum(axis=2, keepdims=True) / 3).astype(np.uint8)
    # result.sum(axis=2, keepdims=True) gives an array where each value
    # is the R+G+B sum of that pixel and array has shape (257, 450, 1)
    # divide every element of that whole array by 3 in one shot.
    # astype(np.uint8) converts float to int (pixel values must be
    # whole numbers 0–255)
    result = np.repeat(grey, 3, axis=2)
    # np.repeat(grey, 3, axis=2) duplicates the grey values across
    # the three channels (from shape (257, 450, 1) to (257, 450, 3))
    print_img_arr(result, "Figure VIII.6: Grey")
    return result


# def main():
#     """Load landscape.jpg and apply all colour filters, displaying each."""
#     array = ft_load("../landscape.jpg")
#     if array.size == 0:
#         return
#     plt.figure("Figure VIII.1: Original")
#     plt.imshow(array)
#     plt.axis("off")
#     plt.show(block=False)
#     ft_invert(array)
#     ft_red(array)
#     ft_green(array)
#     ft_blue(array)
#     ft_grey(array)


# if __name__ == '__main__':
#     main()
