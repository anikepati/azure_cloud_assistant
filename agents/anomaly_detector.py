import numpy as np

def detect_anomaly(current, previous, threshold=2.0):
    mean_prev = np.mean(previous)
    if mean_prev == 0:
        return False
    ratio = current / mean_prev
    return ratio > threshold