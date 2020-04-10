import cv2
import numpy as np
import cube as rubiks
from graphics import *
import drawing


def detect(mask, frame, color):
    contours, _ = cv2.findContours(mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)
    frame = cv2.drawContours(frame, contours, -1, color, 2)
    return frame


def color_mask(frame, hue, rng):
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    lower = np.array([hue - rng, 50, 50])
    upper = np.array([hue + rng, 255, 255])
    mask = cv2.inRange(hsv, lower, upper)
    return mask


def cube_filter(frame):
    cpy = frame
    blue_mask = color_mask(frame, 100, 15)
    green_mask = color_mask(frame, 60, 20)
    # red_mask = color_mask(frame, 0, 0)
    # yellow_mask = color_mask(frame, 30, 5)
    # orange_mask = color_mask(frame, 20, 3)
    # cv2.bitwise_and(frame, frame, mask=green_mask)
    detected = detect(green_mask, frame, (0, 255, 0))
    detected = detect(blue_mask, detected, (255, 0, 0))
    return detected


def main():
    win_name = "Live"
    cv2.namedWindow(win_name)
    cap = cv2.VideoCapture(0)

    if cap.isOpened():
        ret, frame = cap.read()
    else:
        ret = False

    for i in range(1000):
        ret, frame = cap.read()
        frame = cube_filter(frame)
        cv2.imshow(win_name, frame)
        if cv2.waitKey(1) == 27:
            break
    cv2.destroyWindow(win_name)
    cap.release()


# print(np.rot90(arr))
drawing.draw()
# color = np.uint8([[[0, 165, 255]]])
# color = cv2.cvtColor(color, cv2.COLOR_BGR2HSV)
# print(color)
