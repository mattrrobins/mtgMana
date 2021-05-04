#! python3

from math import trunc

def truncate(number, decimals=0):
    if not isinstance(decimals, int):
        raise TypeError('decimal places must be an integer')
    elif decimals < 0:
        raise ValueError('decimal places have to be at least 0')
    elif decimals == 0:
        return trunc(number)

    factor = 10 ** decimals
    return trunc(number * factor) / factor
