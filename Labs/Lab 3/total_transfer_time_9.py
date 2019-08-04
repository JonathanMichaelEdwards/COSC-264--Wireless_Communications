def total_transfer_time (linkLength_km, speedOfLight_kms, processingDelay_s, dataRate_bps, maxUserDataBitsPerPacket_b, overheadBitsPerPacket_b, messageLength_b):
    l = linkLength_km
    c = speedOfLight_kms
    p = processingDelay_s
    r = dataRate_bps
    s = maxUserDataBitsPerPacket_b
    o = overheadBitsPerPacket_b
    m = messageLength_b

    bitsPerPacket = s - o  # s + o
    numPackets = m / s
    propogation = (l / c)
    transmission = bitsPerPacket / r


    return (transmission * numPackets) + (p * numPackets) - transmission
    # return (((transmission * (numPackets-1)) + (p * numPackets) + propogation*2))



    # return ((propogation*2) + (transmission*4) + (p*9))


    # return (propogation + transmission + p) * 2 + transmission*2 + p*7


print ("{:.4f}".format(total_transfer_time(20000, 200000, 0.001, 1000000, 1000, 100, 50000)))
# print ("{:.4f}".format(total_transfer_time(20000, 200000, 0.001, 1000000, 1000, 100, 5000)))
# 0.2086