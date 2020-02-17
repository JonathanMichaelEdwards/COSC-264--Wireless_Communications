from per_from_ber_28 import *
from average_trials_26 import *


def avg_trials_from_ber(bit_error_probability, packetLength_b):
    return average_trials(per_from_ber(bit_error_probability, packetLength_b))


print("{:.3f}".format(avg_trials_from_ber(0.001, 2000)))
