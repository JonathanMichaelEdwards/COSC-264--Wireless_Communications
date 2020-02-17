from total_number_bits_6 import total_number_bits


def total_transfer_time (linkLength_km, speedOfLight_kms, processingDelay_s, dataRate_bps, maxUserDataBitsPerPacket_b, overheadBitsPerPacket_b, messageLength_b):
    l = linkLength_km
    c = speedOfLight_kms
    p = processingDelay_s
    r = dataRate_bps
    s = maxUserDataBitsPerPacket_b
    o = overheadBitsPerPacket_b
    m = messageLength_b

    bitsPerPacket = s + o
    numPackets = m / s
    totalBits = (o*numPackets) + m
    propogation = (l / c)
    transmission_1 = bitsPerPacket / r  # Send bits per packet
    transmission_2 = (totalBits / r)    # Send total bits

    return (((propogation + p) * 2) + transmission_1 + transmission_2)


print ("{:.5f}".format(total_transfer_time (10000, 200000, 0.001, 1000000, 1000, 100, 1000000000)))
