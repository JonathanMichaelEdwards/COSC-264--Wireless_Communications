def total_number_bits (maxUserDataBitsPerPacket_b, overheadBitsPerPacket_b, messageLength_b):
    S = maxUserDataBitsPerPacket_b
    O = overheadBitsPerPacket_b
    M = messageLength_b

    maxBits = S - O     # max_packet - overhead
    packageAmount = 0
    packetsCount = 0

    while packageAmount < M:
        if packageAmount <= M-maxBits:
            packageAmount += S
        else:
            packageAmount += O
        packetsCount += 1

    return ((packetsCount * O) + M )
