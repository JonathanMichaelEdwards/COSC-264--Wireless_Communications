import math

def min_packet_length (cableLength_km, speedOfLight_kms, dataRate_bps):
    L = cableLength_km
    C = speedOfLight_kms
    R = dataRate_bps

    return math.ceil(((L/C) * R)*2)

print ("{:.1f}".format(min_packet_length(1,200000,1000000)))
