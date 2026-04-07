import numpy as np
import matplotlib.pyplot as plt
from load_image import ft_load


def ft_rotate(img):
    """
    Function that zooms the image (cropping it from the center)
    :param img:
    :return:
    """

    arr = ft_load(img)
    if arr.size == 0:
        return
    # print(arr)

    height, width, channel = arr.shape
    if height < 400 or width < 400:
        print("Error: image too small for zoom")
        return
    # center of the image
    center_h = height // 2
    center_w = width // 2
    half_size = 200  # half of 400 (from task)

    # New image borders
    h_start = max((center_h - half_size), 0)
    h_end = min((center_h + half_size), height)
    w_start = max((center_w - half_size), 0)
    w_end = min((center_w + half_size), width)

    zoomed = arr[h_start:h_end, w_start:w_end]
    if zoomed.ndim == 3:
        zoomed = zoomed[:, :, 0:1]  # leaves only one channel from RGB (R)
    print(
        f"The shape of image is: {zoomed.shape}"
        f" or {(zoomed.shape[0], zoomed.shape[1])}"
    )
    print(zoomed)
    # transpose function is used to reverse or permute the axes of an array.
    # For 2D arrays, it simply flips rows and columns. For 1D arrays,
    # transpose has no effect because they have only one axis.
    # This function is commonly used in matrix operations and
    # data transformations where orientation matters.
    # numpy.transpose(a, axes=None) a: Input array to transpose,
    # axes (Optional): tuple that defines the new axis order
    # (e.g., (1, 0) for swapping rows and columns)

    transposed_zoomed = np.transpose(zoomed, (1, 0, 2))
    transposed_zoomed = transposed_zoomed.squeeze()
    print(f"New shape after Transpose: {transposed_zoomed.shape}")
    print(transposed_zoomed)

    # showing new image with matplotlib (with axes)
    plt.imshow(transposed_zoomed, cmap='gray')
    plt.show()


def main():
    """
    Entry point for program

    :return: nothing
    """
    # ft_rotate("../landscape.jpg")
    ft_rotate("../animal.jpeg")


if __name__ == '__main__':
    main()
