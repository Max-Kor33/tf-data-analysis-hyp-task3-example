import pandas as pd
import numpy as np
from scipy.stats import ttest_ind

chat_id = 957195795 # Ваш chat ID, не меняйте название переменной

def solution(x, y):
    ## Взял T-test тк дисперсия и матожидания конечны
    res = ttest_ind(x, y, equal_var=False, alternative='two-sided')
    return res.pvalue < 0.03
