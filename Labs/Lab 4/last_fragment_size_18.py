from math import ceil


def last_fragment_size(messageSize_bytes, overheadPerPacket_bytes, maximumNPacketSize_bytes):
    """
    Last Fragments. 
    """
    s = messageSize_bytes
    o = overheadPerPacket_bytes
    m = maximumNPacketSize_bytes

    pktMax = m - o
    fragments = ceil(s / pktMax)
    overallPkt = s + o

    return overallPkt - pktMax * (fragments-1)


# print(last_fragment_size(1500, 20, 1500)) # Q)20; Ans = 40
# print(last_fragment_size(10000, 20, 1500)) # Q)22; Ans = 1140
