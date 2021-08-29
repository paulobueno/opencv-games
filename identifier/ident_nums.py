import cv2 as cv
import os
import numpy as np


class Identify:
    def __init__(self, file_name, auto_load=True):
        self.image_name = file_name
        self.loaded_image = None
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
        lines = cv.HoughLines(edges, 1, np.pi/2, 200)
        for line in lines:
            rho, theta = line[0]
            a = np.cos(theta)
            b = np.sin(theta)
            x0 = a * rho
            y0 = b * rho
            x1 = int(x0 + 1000 * (-b))
            y1 = int(y0 + 1000 * (a))
            x2 = int(x0 - 1000 * (-b))
            y2 = int(y0 - 1000 * (a))
            cv.line(self.loaded_image, (x1, y1), (x2, y2), (0, 0, 255), 2)

    def preview(self, test=False):
        msg = 'Image Preview'
        if test:
            msg = '## TEST MODE ##: Type y to finish this test'
        cv.imshow(msg, self.loaded_image)
        k = cv.waitKey(0)
        cv.destroyAllWindows()
        return k


if __name__ == '__main__':
    game = Identify('sudoku_example.jpg')
    game.preview()

