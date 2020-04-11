import cv2 as cv
import numpy as np

def get_hue(img):
    return cv.cvtColor(img, cv.COLOR_BGR2HSV)[:, :, 0]


def hue_correlation(frame, patch):
    frame_hue = get_hue(frame)
    patch_hue = get_hue(patch)
    cv.namedWindow("Win", cv.WINDOW_NORMAL)
    method = cv.TM_CCORR_NORMED
    res = cv.matchTemplate(frame, patch, method)
    return res


def main():
    frame = cv.imread(cv.samples.findFile("assets/frame2.jpeg"))
    patch = cv.imread(cv.samples.findFile("assets/green_patch.jpeg"))

    res = hue_correlation(frame, patch)
    cv.namedWindow("Win", cv.WINDOW_NORMAL)
    cv.imshow("Win", res)
    cv.waitKey(0)


main()
