def per_from_ber(bitErrorProb, packetLen_b):
    return (1 - (1 - bitErrorProb)**packetLen_b)
