from total_number_bits_6 import total_number_bits


def packet_transfer_time (linkLength_km, speedOfLight_kms, processingDelay_s, dataRate_bps, maxUserDataBitsPerPacket_b, overheadBitsPerPacket_b):
    """
    To healp to see how everything adds up,
    draw a time-event diagram.
    """
    L = linkLength_km
    C = speedOfLight_kms
    P = processingDelay_s
    R = dataRate_bps
    S = maxUserDataBitsPerPacket_b
    O = overheadBitsPerPacket_b

    bitsPerPacket = total_number_bits(S, O, S)
    propogation = ((L) / (C))
    transmission = bitsPerPacket / R

    return (propogation + transmission + P) * 2
