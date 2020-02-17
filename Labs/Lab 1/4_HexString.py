from convert_3 import convert
        

def hexstring(x):
    strHex = "0x"
    base = 16

    if x < 0:
        return -1
    elif x < 0:
        return -2
    else:
        for i in convert(x, base):
            if i >= 10:
                strHex += str(hex(i).strip("0x")).upper()
            else:
                strHex += str(i)

        return strHex