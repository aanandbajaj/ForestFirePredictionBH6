from graphics import *
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from turtle import *
import urllib
from scatter import *


def main():
    # Creating numpy array
    X = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15])
    Y = X**2
    # Setting the figure size
    plt.figure(figsize=(10, 6))
    plt.plot(X, Y)
    plt.show()


main()
