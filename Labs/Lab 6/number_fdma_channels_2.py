import math


def number_fdma_channels(b_hz, g_hz, u_hz):
    return math.floor(b_hz / (g_hz+u_hz))
