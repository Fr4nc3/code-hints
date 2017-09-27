# *******************************************************
# @Fr4nc3
# 04/27/2013
# nn classifier module
# *******************************************************
import numpy as np
import random
import math


def nn_classifier(training, test):
    """ Purpose of this function is to use the training data to provide
    labels for a set of test data."""
    n = len(test)

    labels = []
    for i in range(n):
        test_row = test[i]

        label_temp = -1
        dist = 0.0
        for j in range(len(training)):
            # The training data is coming with label, we split it.
            training_row = training[j][0]
            label_training = training[j][1]

            # calculated the distance between the two data sets
            dist_temp = euclidean_distance(training_row, test_row)

            """we stored the label of the shortest distance between the
            raining and the test array. """
            if dist_temp <= dist or dist == 0:
                dist = dist_temp
                label_temp = label_training
        # add the label to the list of label for each row of tested data.
        labels.append(label_temp)

    return labels


def euclidean_distance(a, b):
    """calculate the distance between two array, element by element."""
    dist = 0.0
    length = len(a)

    for i in range(length):
        dist += pow((a[i] - b[i]), 2)
    return math.sqrt(dist)


def n_validator(data, p, classifier, *args):
    """This function is to estimate the performance of a classifier in a
    particular setting."""

    # if args are passed it is synthetic data
    if len(args) > 0:
        # merge the two synthetic data
        data = data + args[0]

    # randomized the data
    random.shuffle(data)
    #split the data in p groups
    chunked_data = chunks(data, p)

    n = len(chunked_data)
    training = chunked_data[-1]  # p-1 part of data is training data
    score = 0
    for i in range(n - 1):
        lt = len(chunked_data[i])
        labels_list = []
        test_list = []

        for j in range(lt):
            # separate test data from its label
            labels_list.append(chunked_data[i][j][1])
            test_list.append(chunked_data[i][j][0])
        #classifier is nn_classifier, method passed as param
        labels = classifier(training, test_list)

        #compared the label with the one from classifier
        for t in range(len(labels)):
            if labels[t] == labels_list[t]:
                score += 1
    # return performance of classifier
    return score / len(data)


def chunks(lst, p):
    """ split a list in  p groups."""
    return [lst[i::p] for i in range(p)]


def labeled_synthetic_data(mean, covariance, samples, label):
    """create synthetic data with its label."""
    data = synthetic_data(mean, covariance, samples)
    data_array = []
    n = len(data)
    for i in range(n):
        row = [data[i], label]
        data_array.append(row)

    return data_array


def synthetic_data(mean, covariance, samples):
    return np.random.multivariate_normal(mean, covariance, samples)


def read_data(file_name):
    """ read dataset file."""

    in_file = open(file_name)
    data = []

    for line in in_file.readlines():
        row = line.split(",")
        """from the 3rd element to the end are float numbers
         the second element is the label converted to 0 or 1."""
        row2 = [list(map(float, row[2:])), 0 if row[1] == 'M' else 1]
        data.append(row2)

    in_file.close()
    return data