import os

import cv2 as cv
import pyautogui as pag


def gen_sudoku_image():
    if 'screenshot.png' in os.listdir('../images'):
        os.remove('../images/screenshot.png')

    screenshot_path = '../images/screenshot.png'
    pag.screenshot(screenshot_path)
    sudoku_example = cv.imread('../images/sudoku_example.png')
    screenshot = cv.imread(screenshot_path)
    result = cv.matchTemplate(screenshot, sudoku_example, cv.TM_CCORR_NORMED)
    min_val, max_val, min_loc, max_loc = cv.minMaxLoc(result)
    top_left = max_loc
    img_h = sudoku_example.shape[0]
    img_w = sudoku_example.shape[1]
    bottom_right = [top_left[0] + img_w, top_left[1] + img_h]
    cropped_screenshot = screenshot[
                         top_left[1]:bottom_right[1],
                         top_left[0]:bottom_right[0]

                         ]
    cv.rectangle(screenshot, top_left, bottom_right, (0, 255, 0), 2, cv.LINE_4)
    cv.imshow('test', result)
    cv.waitKey()
    cv.imshow('test', screenshot)
    cv.waitKey()
    cv.destroyAllWindows()
    if 'cropped_screenshot.png' in os.listdir('../images'):
        os.remove('../images/cropped_screenshot.png')
    cv.imwrite('../images/cropped_screenshot.png', cropped_screenshot)
    return None
