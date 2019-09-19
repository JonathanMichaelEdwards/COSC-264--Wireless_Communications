from math import ceil


def number_fragments (messageSize_bytes, overheadPerPacket_bytes, maximumNPacketSize_bytes):
    """
    Generated Fragments.
    """
    s = messageSize_bytes
    o = overheadPerPacket_bytes
    m = maximumNPacketSize_bytes

    fragments = s / (m-o)

    return ceil(fragments)


print(number_fragments(10000, 20, 1500)) # Q)21; Ans = 7
