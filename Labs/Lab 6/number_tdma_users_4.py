import math


def number_tdma_users (s_s, g_s, u_s):
    return math.floor(s_s / (g_s+u_s))
