import math


def convert(x, base):
    if x < 0:
        return -1
    elif base < 0:
        return -2
    elif x < 0:
        return -3
    elif base < 2:
        return -4
    else:
        coefficients = []
        valueLen = x
        i = 0
     
        while i <= math.log(valueLen, base):
            coefficients.append(x % base)
            x //= base
            i += 1
            
        return coefficients[::-1]