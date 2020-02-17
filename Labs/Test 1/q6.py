def connection_setup_delay (numberSwitches, cableLength_km, speedOfLight_kms, dataRate_bps, messageLengthRequest_b, messageLengthResponse_b, processingTimes_s):
    # N     = numberSwitches
    # L     = cableLength_km
    # C     = speedOfLight_kms
    # R     = dataRate_bps
    Mreq  = messageLengthRequest_b
    Mresp = messageLengthResponse_b
    # P     = processingTimes_s
    
    t1 = ((cableLength_km) / (speedOfLight_kms))
    t2 = (Mreq) / dataRate_bps
    t3 = processingTimes_s

    return ((t1 + t2 + t3) + (t1 + (Mresp / dataRate_bps) + t3)) * 4

print ("{:.4f}".format(connection_setup_delay(3, 7500, 200000, 10000000, 2000, 1000, 0.001)))
