from math import ceil


def last_fragment_size(messageSize_bytes, overheadPerPacket_bytes, maximumNPacketSize_bytes):
    """
    Last Fragments. 
    """
    s = messageSize_bytes
    o = overheadPerPacket_bytes
    m = maximumNPacketSize_bytes

    payload = m - o
    fragments = ceil(s / payload)
    # overallPkt = s + o

    # return overallPkt - payload * (fragments-1)
    return s 


print(last_fragment_size(1024, 80, 280)) # 104
# print(last_fragment_size(10000, 20, 1500)) # Q)22; Ans = 1140
