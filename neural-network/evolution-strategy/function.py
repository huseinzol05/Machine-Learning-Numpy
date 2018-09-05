import numpy as np

def mean_square_error(solution, w):
    return -np.mean(np.square(solution - w))

def root_mean_square_error(solution, w):
    return -np.sqrt(np.mean(np.square(solution - w)))

def mean_absolute_error(solution, w):
    return -np.mean(np.abs(solution - w))

def cross_entropy(solution, w):
    return np.mean(solution * np.log(w))

def sigmoid(x):
    return 1 / (1 + np.exp(-x))

def softmax(w):
    exp_scores = np.exp(w)
    return exp_scores / np.sum(exp_scores, axis=1, keepdims=True)