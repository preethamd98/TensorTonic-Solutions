import numpy as np

def sigmoid(x: list | float) -> np.ndarray | float:
    x = np.asarray(x)
    result = 1 / (1 + np.exp(-x))
    return result.item() if result.ndim == 0 else result