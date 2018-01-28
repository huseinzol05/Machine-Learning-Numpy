import numpy as np

def l1(alpha, w,grad=False):
    if grad:
        return alpha * np.sign(w)
    else:
        return alpha * np.sum(np.abs(w))

def l2(alpha, w, grad=False):
    if grad:
        return alpha * w
    else:
        return alpha * np.sum(w * w)

def l1_l2(alpha, w, l1_ratio = 0.5, grad=False):
    if grad:
        return alpha * ((l1_ratio * np.sign(w)) + ((1 - l1_ratio) * w))
    else:
        return alpha * ((l1_ratio * np.sum(np.abs(w))) + ((1 - l1_ratio) * np.sum(w * w)))
