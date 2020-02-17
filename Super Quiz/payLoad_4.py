def payload(pkt):
    """
    Extracting IPv4 Payload. 
    """
    pktPayLoad = bytearray(0)
    # Determines the size of the 'Header Length'
    hdrLen = (pkt[0] & 0xF) * 4   # 4 Bytes in a 32-bit row

    for byte in range(len(pkt)):
        if hdrLen <= byte:
            pktPayLoad += bytes([pkt[byte]])

    return pktPayLoad
