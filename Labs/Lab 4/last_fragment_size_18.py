import math

def last_fragment_size(messageSize_bytes, overheadPerPacket_bytes, maximumNPacketSize_bytes):
    s = messageSize_bytes
    o = overheadPerPacket_bytes
    m = maximumNPacketSize_bytes

    fragments = math.ceil(s / (m-o))

    return fragments


print (last_fragment_size(10000, 100, 1000))