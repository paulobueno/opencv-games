import cv2 as cv
import os
from sklearn.model_selection import train_test_split
from sklearn import svm, metrics
import numpy as np
from joblib import dump, load

for i in range(10):
    name = 'Value: ' + str(i)
    cv.namedWindow(name, cv.WINDOW_NORMAL)
    cv.moveWindow(name, 100 + 100 * i, 100)
    cv.resizeWindow(name, 100, 100)

dataset = []
for file_name in os.listdir('../images_database/'):
    img = cv.imread('../images_database/' + file_name, cv.IMREAD_GRAYSCALE)[10:40, 10:40]
    img = cv.resize(img, (16, 16), interpolation=cv.INTER_LINEAR)
    img = np.where(img < 200, 0, img)
    cv.imshow('Value: ' + file_name[0], img)
    cv.waitKey(2)
    flat_img = img.flatten()
    dataset.append((int(file_name[0]), flat_img))

X = np.array([data[1] for data in dataset])
y = np.array([data[0] for data in dataset])
X_train, X_test, y_train, y_test = train_test_split(X, y)
print('Training data and target sizes: \n{}, {}'.format(X_train.shape, y_train.shape))
print('Test data and target sizes: \n{}, {}'.format(X_test.shape, y_test.shape))

# Create a classifier: a support vector classifier
classifier = svm.SVC(kernel='rbf')
# fit to the training data
classifier.fit(X_train, y_train)

# now to Now predict the value of the digit on the test data
y_pred = classifier.predict(X_test)

print("Classification report for classifier %s:\n%s\n"
      % (classifier, metrics.classification_report(y_test, y_pred)))

print("Confusion matrix:\n%s" % metrics.confusion_matrix(y_test, y_pred))

dump(classifier, 'model_1.svm')
