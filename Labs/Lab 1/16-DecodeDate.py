def decodedate(x):
    dayMask   = 0x0F800000
    monthMask = 0xF0000000
    yearMask  = 0x007FFFFF

    day = ((x & dayMask) >> 23) + 1
    month = ((x & monthMask) >> 28) + 1
    year = (x & yearMask)

    return "{}.{}.{}".format(day, month, year)