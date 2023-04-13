import pandas as pd
import numpy as np
from scipy.stats import anderson_ksamp


chat_id = 230790372 # Ваш chat ID, не меняйте название переменной


def solution(x: np.array, y: np.array) -> bool:
    alpha = 0.04
    pvalue = anderson_ksamp([x,y]).significance_level

    if pvalue <= alpha:
        is_rejected = True
    else:
        is_rejected = False

    return is_rejected
