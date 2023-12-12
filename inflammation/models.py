"""Module containing models representing patients and their data.

The Model layer is responsible for the 'business logic' part of the software.

Patients' data is held in an inflammation table (2D array) where each row contains 
inflammation data for a single patient taken over a number of days 
and each column represents a single day across all patients.
"""

import numpy as np
from functools import reduce


def load_csv(filename):
    """Load a Numpy array from a CSV

    :param filename: Filename of CSV to load
    """
    return np.loadtxt(fname=filename, delimiter=',')


def daily_mean(data):
    """Calculate the daily mean of a 2D inflammation data array for each day.
    :param data: a 2D array containing inflammation data (each row contains a patient)
    :returns: array of mean inflammations per day
    """
    return np.mean(data, axis=0)


def daily_max(data):
    """Calculate the daily max of a 2D inflammation data array for each day.
    :param data: a 2D array containing inflammation data (each row contains a patient)
    :returns: array with the maximum inflammation per day
    """
    return np.max(data, axis=0)


def daily_min(data):
    """Calculate the daily min of a 2D inflammation data array for each day.
    :param data: a 2D array containing inflammation data (each row contains a patient)
    :returns: array with the minimum inflammation per day
    """
    return np.min(data, axis=0)


def daily_above_threshold(data,threshold,patient_num):
    """Calculate daily if threshold is exceeded per patient 2D inflammation data array for each day.
    :param data: a 2D array containing inflammation data (each row contains a patient)
    :param threshold: An inflammation threshold to check each daily value against
    :param patient_num: Patient row number
    :returns: a number of exceedance of the inflammation threshold per day
    """
    above_threshold = map(lambda x: x > threshold, data[patient_num])
    return reduce(lambda a, b: int(a) + int(b),above_threshold )
