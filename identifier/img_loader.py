import itertools
import random
import cv2 as cv
import os
import numpy as np


class Identify:
    def __init__(self, file_name, auto_load=True):
        self.image_name = file_name
        self.loaded_image = None
        if auto_load:
            self.load_image()
            self.crop_image()
            # self.add_red_lines()

    def load_image(self):
        main_script_dir = os.path.abspath(__file__ + '/../..')
        rel_path = 'images/' + self.image_name
        image_path = os.path.join(main_script_dir, rel_path)
        self.loaded_image = cv.imread(image_path)
        return self.loaded_image

    def gen_lines_rho(self, axis=None):
        gray = cv.cvtColor(self.loaded_image, cv.COLOR_BGR2GRAY)
        edges = cv.Canny(gray, 50, 150, apertureSize=3)
        lines = cv.HoughLines(edges, 1, np.pi / 2, 100)
        if axis == 0:
            # horizontal lines
            rho = [line[0][0] for line in lines if line[0][1] != 0]
        elif axis == 1:
            # vertical lines
            rho = [line[0][0] for line in lines if line[0][1] == 0]
        else:
            rho = [line[0][0] for line in lines]
        return rho

    def get_clean_x_rho(self):
        rho_list = self.gen_lines_rho(axis=1)
        rho_list.sort()
        rho_diffs = []
        for i in range(len(rho_list) - 1):
            if rho_list[i + 1] - rho_list[i] <= 5:
                rho_list[i] = rho_list[i + 1]
        return list(set(rho_list))

    def get_clean_y_rho(self):
        rho_list = self.gen_lines_rho(axis=0)
        rho_list.sort()
        for i in range(len(rho_list) - 1):
            if rho_list[i + 1] - rho_list[i] <= 5:
                rho_list[i] = rho_list[i + 1]
        return list(set(rho_list))

    def get_symmetric_rho(self):
        rho_list = self.gen_lines_rho(axis=1)
        rho_list.sort()
        rho_diffs = []
        for i in range(len(rho_list) - 1):
            if rho_list[i + 1] - rho_list[i] <= 5:
                rho_list[i] = rho_list[i + 1]
            rho_diffs.append(rho_list[i + 1] - rho_list[i])
        rho_diffs = list(set(rho_diffs))
        median = np.median(rho_diffs)
        return median

    def crop_image(self):
        clean_x = self.get_clean_x_rho()
        clean_y = self.get_clean_y_rho()
        if len(clean_y) + len(clean_x) >= 20:
            start_h = int(min(clean_y))
            end_h = int(max(clean_y))
            start_l = int(min(clean_x))
            end_l = int(max(clean_x))
            self.loaded_image = self.loaded_image[start_h:end_h, start_l:end_l]
            return None

    def add_red_lines(self):
        y0, x0, z0 = self.loaded_image.shape
        for i in range(11):
            y = int(y0 / 9) * i
            x = int(x0 / 9) * i
            cv.line(self.loaded_image, (y, 0), (y, x0), (0, 0, 255), 1)
            cv.line(self.loaded_image, (0, x), (y0, x), (0, 0, 255), 1)
        return None

    def get_number(self, number):
        y0, x0, z0 = self.loaded_image.shape
        rho_y = int(y0 / 9)
        rho_x = int(x0 / 9)
        xy0 = (rho_y * number[0], rho_x * number[1])
        xy1 = (xy0[0] + rho_y, xy0[1] + rho_x)
        return self.loaded_image[xy0[0]:xy1[0], xy0[1]:xy1[1]]

    def preview(self, test=False, number=None, save=False):
        name = 'Game Preview'
        cv.namedWindow(name, cv.WINDOW_NORMAL)
        cv.moveWindow(name, 100, 100)
        cv.resizeWindow(name, 500, 500)
        if test:
            name = '## TEST MODE ##: Type y to finish this test'
        if number:
            name = 'Number Preview'
            cv.namedWindow(name, cv.WINDOW_NORMAL)
            cv.moveWindow(name, 800, 100)
            cv.resizeWindow(name, 100, 100)
            img = self.get_number(number)
            cv.imshow(name, img)
        else:
            img = self.loaded_image
            cv.imshow(name, self.loaded_image)
        k = cv.waitKeyEx(0)
        if save:
            main_script_dir = os.path.abspath(__file__ + '/../..')
            rel_path = 'images_database/' + chr(k) + '_' + str(random.randint(0, 1000)) + '.jpg'
            image_path = os.path.join(main_script_dir, rel_path)
            cv.imwrite(image_path, img)
        return k


if __name__ == '__main__':
    for num in range(2, 45):
        game = Identify(str(num) + '.png')
        game.add_red_lines()
        k = game.preview()
        if k == ord('y'):
            for i in itertools.product(range(9), range(9)):
                game.preview(number=i, save=True)
    cv.destroyAllWindows()
