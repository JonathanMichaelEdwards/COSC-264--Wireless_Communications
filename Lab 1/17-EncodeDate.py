def encodedate(day, month, year):
    x = 0

    if (day < 1 or day > 31):
        return -1
    elif (month < 1 or month > 12):
        return -1
    elif (year > 2**23-1):
        return -1
    else:
        x = (day-1) << 23
        x |= (month-1) << 28
        x |= year
        return x