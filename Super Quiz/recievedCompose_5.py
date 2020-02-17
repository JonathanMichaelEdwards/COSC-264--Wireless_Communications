def errorChecker(data, bits, errorCode):
    """
    Checks to see is the data is within the bit range.
    """
    if 0 > data or data >= 2**bits:
        return errorCode



def bitEncoder32(data):
    """
    Returns 4 Bytes of data into 1 Byte broken up.
    """
    byte1 = data >> 24
    byte2 = (data >> 16) & 0xFF
    byte3 = (data >> 8) & 0xFF
    byte4 = data & 0xFF

    return bytes([byte1]) + bytes([byte2]) + bytes([byte3]) + bytes([byte4])



def bitEncoder16(data):
    """
    Returns 2 Bytes of data into 1 Byte broken up.
    """
    byte1 = data >> 8
    byte2 = data & 0xFF
    
    return bytes([byte1]) + bytes([byte2])



def checkSumDecoder(pkt):
    """
    Returns the value of the checksum to see if its correct.
    """
    checkSum = 0 
    for byte in range(0, 20, 2):
        checkSum += pkt[byte] << 8 | pkt[byte+1]

    checkSum = ~((checkSum & 0xFFFF) + (checkSum >> 16)) & 0xFFFF  # invert bits

    return checkSum



def dataPayLoad(pkt, lenTotal, payLoad):
    """
    Adding extra dta to the packet.
    """
    for _ in range(20, lenTotal-len(payLoad)):
        pkt += bytes([0])
    
    for byte in range(len(payLoad)):
        pkt += bytes([payLoad[byte]])



def revisedcompose(hdrlen, tosdscp, identification, flags, fragmentoffset, timetolive, protocoltype, sourceaddress, destinationaddress, payload):
    """
    Compose a packet with the following parameters given.
    """
    version = 4
    headerchecksum = 0
    pktContents = bytearray(0)
    totalLength = (hdrlen * 4) + len(payload)

    listCheck = [
        (tosdscp, 6, 3), (identification, 16, 5), (flags, 3, 6),
        (fragmentoffset, 13, 7), (timetolive, 8, 8), (protocoltype, 8, 9),
        (sourceaddress, 32, 11), (destinationaddress, 32, 12)
        ]


    # Validity Checks
    if errorChecker(hdrlen, 4, 2) == 2 or listCheck[0][0] < 5:
        return 2
    

    # Checks to see if listCheck contains an error
    for i in listCheck:
        if errorChecker(i[0], i[1], i[2]) is not None:  # if error is not None return error code
            return errorChecker(i[0], i[1], i[2])


    # Compose packet data
    pktContents += bytes([version << 4 | hdrlen])                # 1 Byte used for version and hdrlen
    pktContents += bytes([tosdscp << 2 | 0])                     # 1 Byte used for tosdscp with 2 unused bits
    pktContents += bitEncoder16(totalLength)                     # 2 Bytes used to encode totallength 
    pktContents += bitEncoder16(identification)                  # 2 Bytes used to encode identification
    
    byte1 = flags << 5 | fragmentoffset >> 8                     # 2 Bytes used to encode flags and offset
    pktContents += bytes([byte1]) + bytes([fragmentoffset & 0xFF])

    pktContents += bytes([timetolive]) + bytes([protocoltype])   # (x2) 1 Byte each for timetolive and protocoltype
    pktContents += bitEncoder16(headerchecksum)                  # 2 Bytes used to encode headerchecksum
    pktContents += bitEncoder32(sourceaddress)                   # 4 Bytes used to encode the source address
    pktContents += bitEncoder32(destinationaddress)              # 4 Bytes used to encode the destination address

    # Adding the 'check sum' value to the packet
    headerchecksum = checkSumDecoder(pktContents)

    # check 'head sum is within its bounds
    if (headerchecksum, 16, 10) == 10:
        return 10

    pktContents[10] = headerchecksum >> 8
    pktContents[11] = headerchecksum & 0xFF
    dataPayLoad(pktContents, totalLength, payload)  # Add optional space and the payload data to the packet


    return pktContents
