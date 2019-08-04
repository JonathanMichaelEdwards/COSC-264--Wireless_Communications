def message_delay(connSetupTime_s, cableLength_km, speedOfLight_kms, messageLength_b, dataRate_bps):
    """
    t0. connsection setup  (connSetupTime_s)
    t1. propagation
    t2. propagation
    t3. transmission
    """
    t1_2 = ((cableLength_km) / (speedOfLight_kms))  #  A -> B -> C
    t3 = messageLength_b / dataRate_bps             #  C
    
    return (connSetupTime_s + (t1_2 * 2) + t3)