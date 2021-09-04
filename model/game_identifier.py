import itertools
import numpy as np
import img_transform.img_loader as il
import cv2 as cv
from joblib import dump, load
from sklearn import svm

game = il.Identify('11.png')
y_predicted = []
clf = load('model_1.svm')

for number_coord in itertools.product(range(9), range(9)):
    img = cv.cvtColor(game.get_number(number=number_coord), cv.COLOR_BGR2GRAY)
    img = cv.resize(img, (16, 16), interpolation=cv.INTER_LINEAR)
    img = np.where(img < 200, 0, img)
    flat_img = img.flatten()
    predicted = clf.predict([flat_img])
    name = 'Transformed'
    cv.imshow(name, img)
    cv.moveWindow(name, 100, 200)
    name = 'Predicted: ' + str(predicted[0])
    cv.imshow(name, game.get_number(number=number_coord))
    cv.moveWindow(name, 500, 200)
    cv.waitKey(500)
    cv.destroyAllWindows()
    y_predicted.append(predicted)
    #
    # for i in range(9):
    #     print(y_predicted[i * 9:9 + (i * 9)])
