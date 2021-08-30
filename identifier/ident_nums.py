import itertools
import random
import cv2 as cv
import os
import numpy as np


class Identify:
    def __init__(self, file_name, auto_load=True):
        self.image_name = file_name
        self.loaded_image = None
        self.rho = 0
        if auto_load:
            self.load_image()
            self.transform_image()

    def load_image(self):
        main_script_dir = os.path.abspath(__file__ + '/../..')
        rel_path = 'images/' + self.image_name
        image_path = os.path.join(main_script_dir, rel_path)
        self.loaded_image = cv.imread(image_path)
        return self.loaded_image

    def transform_image(self):
        gray = cv.cvtColor(self.loaded_image, cv.COLOR_BGR2GRAY)
        edges = cv.Canny(gray, 50, 150, apertureSize=3)
        lines = cv.HoughLines(edges, 1, np.pi / 2, 100)
        rho_list = [int(rt[0][0]) for rt in lines]
        rho_list.sort()
        smooth_rho_list = []
        for k, rho in enumerate(rho_list[1:], start=1):
            if rho - rho_list[k - 1] > 5 or k == 1:
                smooth_rho_list.append(rho)
                cv.line(self.loaded_image, (rho, 0), (rho, 1000), (0, 0, 255), 1)
                cv.line(self.loaded_image, (0, rho), (1000, rho), (0, 0, 255), 1)
        min_rho = min(smooth_rho_list)
        max_rho = max(smooth_rho_list)
        self.loaded_image = self.loaded_image[min_rho:max_rho, min_rho:max_rho]
        self.rho = smooth_rho_list[1] - smooth_rho_list[0]

    def preview(self, test=False, number=None, save=False):
        msg = 'Image Preview'
        if test:
            msg = '## TEST MODE ##: Type y to finish this test'
        if number:
            xy0 = (self.rho * number[0], self.rho * number[1])
            xy1 = (xy0[0] + self.rho, xy0[1] + self.rho)
            img = self.loaded_image[xy0[0]:xy1[0], xy0[1]:xy1[1]]
            cv.imshow(msg, img)
        else:
            img = self.loaded_image
            cv.imshow(msg, self.loaded_image)
        k = cv.waitKeyEx(0)
        if save:
            main_script_dir = os.path.abspath(__file__ + '/../..')
            rel_path = 'images_database/' + chr(k) + '_' + str(random.randint(0, 100)) + '.jpg'
            image_path = os.path.join(main_script_dir, rel_path)
            cv.imwrite(image_path, img)
        cv.destroyAllWindows()
        return k


if __name__ == '__main__':
    # game = Identify('sudoku_example.jpg')
    game = Identify('sudoku_example2.png')
    game.preview(number=None)
    for i in itertools.product(range(9), range(9)):
        game.preview(number=i, save=True)
