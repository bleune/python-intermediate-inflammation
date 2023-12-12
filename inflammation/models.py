"""Module containing models representing patients and their data.

The Model layer is responsible for the 'business logic' part of the software.

Patients' data is held in an inflammation table (2D array) where each row contains 
inflammation data for a single patient taken over a number of days 
and each column represents a single day across all patients.
"""

import numpy as np


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


class Observation:
    """Observation"""
    def __init__(self, day, value):
        self.day = day
        self.value = value

    def __str__(self):
        return str(self.value)

class Person:
    """A person."""
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return self.name

class Patient(Person):
    """A patient in an inflammation study."""
    def __init__(self, name):
        super().__init__(name)
        self.observations = []

    def add_observation(self, value, day=None):
        if day is None:
            try:
                day = self.observations[-1].day + 1
            except IndexError:
                day = 0
        new_observation = Observation(day, value)
        self.observations.append(new_observation)
        return new_observation
    
class Doctor(Person):
    """A doctor that has patients in the inflammation study"""
    def __init__(self,name):
        super().__init__(name)
        self.patients = []


    def add_patient(self, new_patient):
        """Add patient to doctor"""
        self.patients.append(new_patient)

    def __str__(self):
        return self.name
    

# alice = Patient('Alice')
# print(alice)

# obs = alice.add_observation(3)
# print(obs)

# doctor = Doctor('Dr. Phil')
# doctor.add_patient(alice)
# print(doctor.patients)