import pandas as pd
import numpy as np
from scipy import stats


chat_id = 230790372 # Ваш chat ID, не меняйте название переменной


def solution(x: np.array, y: np.array) -> bool:
    alpha = 0.04
    _, pvalue = stats.ks_2samp(x, y)

    if pvalue <= alpha:
        is_rejected = True
    else:
        is_rejected = False

    return is_rejected
