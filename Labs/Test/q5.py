def connection_setup_delay (numberSwitches, cableLength_km, speedOfLight_kms, dataRate_bps, messageLengthRequest_b, messageLengthResponse_b, processingTimes_s):
    N     = numberSwitches
    L     = cableLength_km
    C     = speedOfLight_kms
    R     = dataRate_bps
    Mreq  = messageLengthRequest_b
    Mresp = messageLengthResponse_b
    P     = processingTimes_s

    propogration = ((L) / (C))
    transmission_1 = Mreq / R
    transmission_2 = Mresp / R
    process = P

    return ((propogration + transmission_1 + process) + (propogration + transmission_2 + process)) * (N+1)
    

# print ("{:.4f}".format(connection_setup_delay(5, 7500, 200000, 10000000, 2000, 1000, 0.001)))
print ("{:.4f}".format(connection_setup_delay(10, 2000, 200000, 10000000, 2000, 1000, 0.001)))
