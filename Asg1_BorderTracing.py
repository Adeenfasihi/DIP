import numpy as np
import cv2
import sys


def clean(image):

    global max_x   # maximum width
    global max_y   # max height
    global start_x, start_y     # starting coordinates where the first white pixel appears

    max_y, max_x = image.shape
    binary = np.zeros((image.shape[0], image.shape[1]))     # empty black image

    # this loop finds the first white pixel in the image, saves its coordinates and breaks
    # it also sets the same pixel in the empty black image, white.
    check = False
    y = 0
    for row in image:
        x = 0
        for pixel in row:
            # print image[y][x]
            if image[y][x] == 255:
                start_x, start_y = x, y
                binary[y][x] = 255
                check = True
                break
            x = x + 1
        if (check): break
        y = y + 1

    # starts iterating the image from the first white pixel that we found in the loop above
    x = start_x
    y = start_y

    # stores the direction from which the iterator came
    prev = (0,0)
    check = [False,False,False,False,False,False,False,False]

    while True:

        if ((y - 1 >= 0) and (x - 1 >= 0) and (y - 1 >= 0) and ((y - 1 >= 0) and (x + 1 < max_x)) and (x + 1 < max_x) and ((y + 1 < max_y) and (x + 1 < max_x))
            and (y + 1 < max_y) and ((x - 1 >= 0) and (y + 1 < max_y)) and (x - 1 >= 0)):

            if ((image[y - 1][x - 1] == 255) and not(binary[y - 1][x - 1] == 255)):
                prev = (1, 1)
                x = x - 1
                y = y - 1
                binary[y][x] = 255

            elif ((image[y - 1][x] == 255) and not(binary[y - 1][x] == 255)):
                prev = (0, 1)
                y = y - 1
                binary[y][x] = 255

            elif ((image[y - 1][x + 1] == 255) and not(binary[y - 1][x + 1] == 255)):
                prev = (-1, 1)
                x = x + 1
                y = y - 1
                binary[y][x] = 255

            elif ((image[y][x + 1] == 255) and not(binary[y][x + 1] == 255)):
                prev = (-1, 0)
                x = x + 1
                binary[y][x] = 255

            elif ((image[y + 1][x + 1] == 255) and not(binary[y + 1][x + 1] == 255)):
                prev = (-1, -1)
                x = x + 1
                y = y + 1
                binary[y][x] = 255

            elif ((image[y + 1][x] == 255) and not(binary[y + 1][x] == 255)):
                prev = (0, -1)
                y = y + 1
                binary[y][x] = 255

            elif ((image[y + 1][x - 1] == 255) and not(binary[y + 1][x - 1] == 255)):
                prev = (1, -1)
                x = x - 1
                y = y + 1
                binary[y][x] = 255

            elif ((image[y][x - 1] == 255) and not(binary[y][x - 1] == 255)):
                prev = (1, 0)
                x = x - 1
                binary[y][x] = 255

            else:
                # print 'break'
                break
    return binary


im = cv2.imread('asg.png', 0)
binary = clean(im)

cv2.imwrite("Assignment1_Output.png", binary)
im = cv2.imread("Assignment1_Output.png", 0)
cv2.imshow('Result', im)
cv2.waitKey()
cv2.destroyAllWindows()
