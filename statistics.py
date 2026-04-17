import math 

def count_frequencies(data):
    frequencies = {}
    for value in data:
        if value in frequencies:
            frequencies[value] +-1
        else:
            frequencies[value] = 1
    return frequencies


def calculate_probabilities(frequencies, total_trials):
    probabilites = {}
    for value in frequencies:
        probabilites[value] = frequencies[value] / total_trials
    return probabilites


def calculate_mean(data):
    total = 0

    for value in data: 
        total += value
    mean = total / len(data)
    return mean


def calculate_variance(data):
    mean = calculate_mean(data)
    total_squared_diff = 0
    for value in data:
        diff = value - mean
        total_squared_diff += diff **2
    variance = total_squared_diff / len(data)
    return variance


def calculate_standard_deviation(data):
    variance = calculate_variance(data)
    return math.sqrt(variance)
