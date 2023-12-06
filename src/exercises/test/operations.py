import unittest
import numpy as np
from sklearn import datasets
import scipy as sp
import matplotlib as mpl
from sklearn import preprocessing



class MyTestCase(unittest.TestCase):
    input_data = np.array([[5.1, -2.9, 3.3],
                           [-1.2, 7.8, -6.1],
                           [3.9, 0.4, 2.1],
                           [7.3, -9.9, -4.5]])
    def test_numpy(self):
        arr = np.array([1, 2, 3, 4, 5])
        print(arr)

    def test_array_shape(self):
        arr = np.array([[1, 2, 3, 4], [5, 6, 7, 8]])
        print(arr)
        print(arr.shape)

    def test_house_prices(self):
        wine_dataset = datasets.load_wine()
        X, y = wine_dataset.data, wine_dataset.target
        print(X)

    # pre-processing data
    def test_classification(self):

        print(X)
