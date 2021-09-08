import itertools
import os
import numpy as np
import img_transform.img_loader as il
import cv2 as cv
from joblib import load

path = os.path.abspath(__file__ + '/../model_1.svm')
clf = load(path)


def transform_image(number_img):
    img = cv.cvtColor(number_img, cv.COLOR_BGR2GRAY)
    img = cv.resize(img, (16, 16), interpolation=cv.INTER_LINEAR)
    img = np.where(img < 200, 0, img)
    flat_img = img.flatten()
    return flat_img


def predict(number_image):
    flat_img = transform_image(number_image)
    predicted_number = clf.predict([flat_img])
    return predicted_number[0]


def get_numbers(game_name):
    game = il.Identify(game_name)
    predict_func = []
    for coordinate in itertools.product(range(9), range(9)):
        number_image = game.get_number(coordinate)
        predict_func.append(predict(number_image))
    return predict_func


def get_game_string_numbers(game_name):
    numbers_list = get_numbers(game_name)
    return ''.join([str(number) for number in numbers_list])


if __name__ == '__main__':
    game_file = '39.png'
    numbers = get_numbers(game_file)
    print(numbers)
    game = il.Identify(game_file)
