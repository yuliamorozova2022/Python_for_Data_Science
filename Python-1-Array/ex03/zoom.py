import matplotlib.pyplot as plt
from load_image import ft_load


def ft_zoom(img):
    """
    Function that zooms the image (cropping it from the center)
    :param img:
    :return:
    """

    arr = ft_load(img)
    if arr.size == 0:
        return
    print(arr)

    height, width, channel = arr.shape
    if height < 400 or width < 400:
        print("Error: image too small for zoom")
        return
    # center of the image
    center_h = height // 2
    center_w = width // 2
    half_size = 200  # half of 400 (from task)

    # bew image borders
    h_start = max((center_h - half_size), 0)
    h_end = min((center_h + half_size), height)
    w_start = max((center_w - half_size), 0)
    w_end = min((center_w + half_size), width)

    zoomed = arr[h_start:h_end, w_start:w_end]
    if zoomed.ndim == 3:
        zoomed = zoomed[:, :, 0:1]  # leaves only one channel from RGB (R)
    print(
        f"New shape after slicing: {zoomed.shape}"
        f" or {zoomed.shape[0], zoomed.shape[1]}"
    )
    print(zoomed)

    # showing new image with matplotlib (with axes)
    plt.imshow(zoomed, cmap='gray')
    plt.show()


def main():
    """
    Entry poit for program

    :return: nothing
    """
    ft_zoom("../landscape.jpg")
    # ft_zoom("../animal.jpeg")


if __name__ == '__main__':
    main()
