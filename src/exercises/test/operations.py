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
    # arrays and load
    def test_declare_array(self):
        arr = np.array([1, 2, 3, 4, 5])
        print(arr)

    def test_array_shape(self):
        arr = np.array([[1, 2, 3, 4], [5, 6, 7, 8]])
        print(arr)
        print(arr.shape)

    def test_wine_prices(self):
        wine_dataset = datasets.load_wine()
        X, y = wine_dataset.data, wine_dataset.target
        print(X)

    # PRE-PROCESSING DATA
    # different ways
    # Binarization
    # Mean removal
    # Scaling
    # Normalization
    def test_Binarize(self):
        # Binarization: convert numeric values into boolean, in order to apply we need to define a threshold.
        # The result value will be
        # 0 -> number less or equal to threshold
        # 1 -> number greater than threshols
        input_data = np.array([[5.1, -2.9, 3.3],
                               [-1.2, 7.8, -6.1],
                               [3.9, 0.4, 2.1],
                               [7.3, -9.9, -4.5]])
        data_binarized = preprocessing.Binarizer(threshold=2.1).transform(input_data)
        print("\nBinarized data:\n", data_binarized)
    def test_mean_removal(self):
        input_data = np.array([[5.1, -2.9, 3.3],
                               [-1.2, 7.8, -6.1],
                               [3.9, 0.4, 2.1],
                           [7.3, -9.9, -4.5]])
        # Binarization: convert numeric values into boolean, in order to apply we need to define a threshold.
        # The result value will be
        # 0 -> number less or equal to threshold
        # 1 -> number greater than threshols
        # Print mean and standard deviation
        print("\nBEFORE:")
        print("Mean =", input_data.mean(axis=0))
        print("Std deviation =", input_data.std(axis=0))
        # The preceding line displays the mean and standard deviation of the input data. Let's
        # remove the mean:
        # Remove mean
        data_scaled = preprocessing.scale(input_data)
        print("\nAFTER:")
        print("Mean =", data_scaled.mean(axis=0))
        print("Std deviation =", data_scaled.std(axis=0))
