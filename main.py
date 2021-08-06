import numpy as np
import cv2 as cv
import pyautogui as pag
import os

try:
    os.remove('./images/screenshot.jpg')
except FileNotFoundError:
    print('File not found')

screenshot_path = './images/screenshot.jpg'
pag.screenshot(screenshot_path)
sudoku_example = cv.imread('./images/sudoku_example.jpg',
                           cv.IMREAD_REDUCED_COLOR_4)
screenshot = cv.imread(screenshot_path, cv.IMREAD_REDUCED_COLOR_4)
result = cv.matchTemplate(screenshot, sudoku_example, cv.TM_CCORR_NORMED)
min_val, max_val, min_loc, max_loc = cv.minMaxLoc(result)

top_left = max_loc
img_h = sudoku_example.shape[0]
img_w = sudoku_example.shape[1]

bottom_right = [top_left[0] + img_w, top_left[1] + img_h]

cv.rectangle(screenshot, top_left, bottom_right, (0, 255, 0), 2, cv.LINE_4)

cv.imshow('test', screenshot)
cv.waitKey()
cv.destroyAllWindows()

