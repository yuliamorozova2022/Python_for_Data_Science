# ex05 – pimp_image

Applies colour filters to a JPEG image loaded as a NumPy array `(height, width, 3)`.  
All functions return an array of the **same shape** and display the result in a named window.

[row, column, channel], which maps to [y, x, channel]:
Index	 Axis	      Values
0	    row (y)     0 … height-1
1	    column (x)  0 … width-1
2	    channel	    0=R, 1=G, 2=B

result[:, :, 0] means: all rows, all columns, channel 0 (Red).

---

## ft_invert

**Operators:** `=`, `+`, `-`, `*`

Subtracts every pixel value from 255, flipping dark pixels light and vice versa.

```
result = 255 - array
```

---

## ft_red

**Operators:** `=`, `*`

Multiplies the array element-wise by `[1, 0, 0]`, keeping the red channel and zeroing green and blue.

```
result = array * [[[1, 0, 0]]]
```

---

## ft_green

**Operators:** `=`, `-`

Copies the array, then zeroes red and blue by subtracting each channel from itself.

```
result[:, :, 0] = result[:, :, 0] - result[:, :, 0]   # zeroes every pixel in channel 0 (red)
result[:, :, 2] = result[:, :, 2] - result[:, :, 2]   # zeroes every pixel in channel 2 (blue)
```

---

## ft_blue

**Operators:** `=`

Copies the array and directly assigns 0 to the red and green channels.

```
result[:, :, 0] = 0
result[:, :, 1] = 0
```

---

## ft_grey

**Operators:** `=`, `/`

Averages the three channels by summing them and dividing by 3, then broadcasts the result back to 3 channels so the shape stays `(H, W, 3)`.

```
grey = array.sum(axis=2, keepdims=True) / 3
result = np.repeat(grey, 3, axis=2)
```
