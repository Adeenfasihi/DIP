import cv2
import numpy as np
from matplotlib import pyplot as plt

L = 256

# defining test region to check if histogram is correct
x0 = 10
x1 = 100
y0 = 10
y1 = 100

# reads image as greyscale
img = cv2.imread('cameraman.tif',0)
height, width = img.shape

# creates histogram array for each pixel in the image
hist = np.zeros((height, width, L), dtype=int)

# calculates integral histogram of the first row
for x in range(0, width):
    temp = img[0][x]
    hist[0][x][temp] += 1
    if (x != 0):
        hist[0][x] = hist[0][x] + hist[0][x-1]

# calculates integral histogram of the first column
for y in range(1, height):
    temp = img[y][0]
    hist[y][0][temp] += 1
    hist[y][0] = hist[y][0] + hist[y-1][0]

# calculates integral histogram for the image except the first row and column
for y in range(1, height):
    for x in range(1, width):
        temp = img[y][x]
        hist[y][x][temp] += 1
        hist[y][x] = hist[y][x] + hist[y][x-1] + hist[y-1][x] - hist[y-1][x-1]



# test region for checking integral histogram accuracy
test = img[y0:y1, x0:x1]

# test region's histogram calculated by builtin function
histo,bins = np.histogram(test.flatten(),L,[0,L])

# calculating histogram of the region using intersection
temp = hist[y1-1, x1-1] - hist[y0-1, x1-1] - hist[y1-1, x0-1] + hist[x0-1, y0-1]

print '\nThe absolute difference between the Histogram achieved with Intersection and Calculated Histogram is: ', sum(abs(temp-histo)), '\n'


# uncomment for histogram plots

# plt.figure(1)
# plt.subplot(211)
# for i in range(0, L):
#     plt.bar(i, temp[i], align = 'center')
#
# plt.subplot(212)
# plt.hist(test.flatten(),L,[0,L], color = 'b')
# plt.show()
