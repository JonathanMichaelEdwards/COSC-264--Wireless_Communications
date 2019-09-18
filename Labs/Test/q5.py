def twowrongbits (pktLength_b, bitErrorProb):
    L = pktLength_b
    P = bitErrorProb

    return (1 - (1 - P)**(L))

print ("{:.3f}".format(twowrongbits(1000, 0.0005)))
print ("{:.3f}".format(twowrongbits(1000, 0.001)))
