def destaddress(pkt):
    """
    Extracting IPv4 Destination Address. 
    """
    # Find the 32-bit IPv4 Destination Address
    addr = pkt[16] << 24 | pkt[17] << 16 | pkt[18] << 8 | pkt[19]

    # Find the dotted-decimal notation of the 32-bit IPv4 Destination Address
    dd = "{0}.{1}.{2}.{3}".format(addr >> 24, (addr >> 16) & 0xFF , (addr >> 8) & 0xFF, addr & 0xFF)
    
    return (addr, dd)

print(destaddress(bytearray(b'E\x00\x00\x1e\x04\xd2\x00\x00@\x06\x00\x00\x00\x124V3DUf')))
