import cv2
import numpy as np
from PIL import Image

# image channels e.g BGR , GreyScale
channels = 3
# dimensions at which the input image is re-sized
width = height = 256
dim = (height,width)

# reads image as a numpy array
img = cv2.imread('lena.jpg', cv2.IMREAD_UNCHANGED)
# re-sizes image
img = cv2.resize(img, dim, interpolation=cv2.INTER_AREA)

# creates an empty matrix for the approximated image
approx_img = np.zeros((height,width,channels), dtype=int)

# re-sizing the input images from the data-set
resize_tile = (4, 4)

# path variable for the tile with minimum distance
min_path = 'asd'

tile = []

for i in range(1000, 8000, 100):
    path = 'resized/image_0'
    path = path + str(i) + '.png'
    t_og = cv2.imread(path, cv2.IMREAD_UNCHANGED)
    tile.append(t_og)

for y in range(0, height - resize_tile[0]+1, resize_tile[0]):
    for x in range(0, width - resize_tile[1]+1, resize_tile[1]):
        temp = img[y:(y+resize_tile[0]), x:(x + resize_tile[1])]
        min_dist = 999999
        min_t = 0

        for t in range(0, len(tile)):
            euclidean_dist = 0

            for i in range(0, channels):
                compare = temp[:,:,i] - tile[t][:][:][i]
                dist = sum(sum(compare**2))
                euclidean_dist += dist

            euclidean_dist = euclidean_dist**0.5

            if euclidean_dist < min_dist:
                min_dist = euclidean_dist
                min_t = t

        min_tile = tile[min_t]

        # write the values of the minimum distance tile to the new matrix
        for l in range(y, y+resize_tile[0]):
             for m in range(x, x+resize_tile[1]):
                 for n in range(0, channels):
                    approx_img[l, m, n] = min_tile[l-y, m-x, n]

# save the image
cv2.imwrite('approx_lena_.png', approx_img)
