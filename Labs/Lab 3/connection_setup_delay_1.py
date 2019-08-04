def connection_setup_delay(cableLength_km, speedOfLight_kms, dataRate_bps, messageLength_b, processingTimes_s):
    """
    Let L stand for the length of one link in km, c stand for the speed of light on the cable (in km/s), 
    R stand for the data rate available on either of the links (in bps), M stand for the length of the 
    call-setup-* messages (in bits), and P stand for the processing times required by A, B and C (in seconds). 
    Find a general expression for the duration of the connection setup phase (i.e. the time between A starting
    the process and A being able to commence data transmission) and implement it as a Python function.
    1. propogation delay      t = d/v
    2. transmission delay     t = l/R
    3. processing delay       # fixed time
    """
    t1 = ((cableLength_km) / (speedOfLight_kms))
    t2 = messageLength_b / dataRate_bps
    t3 = processingTimes_s

    return (t1 + t2 + t3) * 4