def checkSumDecoder(pkt):
    """
    Returns the value of the checksum to see if its correct.
    """
    packetSize = 0
    for byte in range(0, 20, 2):
        packetSize += pkt[byte] << 8 | pkt[byte+1]
    
    return ((packetSize & 0xFFFF) + (packetSize >> 16))



def basicpacketcheck(pkt):
    """
    Check packet sizes are correct.
    """
    if len(pkt) < 20:
        return 1
    if (pkt[0] >> 4) != 4:
        return 2

    # Checks the sum of the package
    if checkSumDecoder(pkt) != 0xFFFF:
        return 3

    # Checks the length and data in the packet
    if (pkt[2] << 8 | pkt[3]) != len(pkt):  # return error if sizes do not match
        return 4

    return True
