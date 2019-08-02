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



def composepacket (version, hdrlen, tosdscp, totallength, identification, flags, fragmentoffset, timetolive, protocoltype, headerchecksum, sourceaddress, destinationaddress):
    """
    Encode and compose a 20 Byte data Packet.
    """
    packetSize = bytearray(0)
    listCheck = [
        (hdrlen, 4, 2), (tosdscp, 6, 3), (totallength, 16, 4), (identification, 16, 5), (flags, 3, 6),
        (fragmentoffset, 13, 7), (timetolive, 8, 8), (protocoltype, 8, 9), (headerchecksum, 16, 10),
        (sourceaddress, 32, 11), (destinationaddress, 32, 12)
        ]


    if version != 4:
        return 1

    # Checks to see if listCheck contains an error
    for i in listCheck:
        if errorChecker(i[0], i[1], i[2]) is not None:  # if error is not None return error code
            return errorChecker(i[0], i[1], i[2])

    # Compose packet data
    packetSize += bytes([version << 4 | hdrlen])               # 1 Byte used for version and hdrlen
    packetSize += bytes([tosdscp << 2 | 0])                    # 1 Byte used for tosdscp with 2 unused bits
    packetSize += bitEncoder16(totallength)                    # 2 Bytes used to encode totallength 
    packetSize += bitEncoder16(identification)                 # 2 Bytes used to encode identification

                 
    byte1 = flags << 5 | fragmentoffset >> 8                   # 2 Bytes used to encode flags and offset
    packetSize += bytes([byte1]) + bytes([fragmentoffset & 0xFF])

    packetSize += bytes([timetolive]) + bytes([protocoltype])  # (x2) 1 Byte each for timetolive and protocoltype
    packetSize += bitEncoder16(headerchecksum)                 # 2 Bytes used to encode headerchecksum
    packetSize += bitEncoder32(sourceaddress)                  # 4 Bytes used to encode the source address
    packetSize += bitEncoder32(destinationaddress)             # 4 Bytes used to encode the destination address


    return packetSize
