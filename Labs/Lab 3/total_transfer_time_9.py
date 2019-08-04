from total_number_bits_6 import total_number_bits


def total_transfer_time (linkLength_km, speedOfLight_kms, processingDelay_s, dataRate_bps, maxUserDataBitsPerPacket_b, overheadBitsPerPacket_b, messageLength_b):
    l = linkLength_km
    c = speedOfLight_kms
    p = processingDelay_s
    r = dataRate_bps
    s = maxUserDataBitsPerPacket_b
    o = overheadBitsPerPacket_b
    m = messageLength_b

    bitsPerPacket = total_number_bits(s, o, m)
    propogation = (l / c)
    transmission = bitsPerPacket / r

    return (propogation + transmission + p) * 2

print ("{:.4f}".format(total_transfer_time(20000, 200000, 0.001, 1000000, 1000, 100, 5000)))
# 0.2086