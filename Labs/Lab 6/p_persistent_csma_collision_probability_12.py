def p_persistent_csma_collision_probability(p):
    return p / (2 - p)

print ("{:.3f}".format(p_persistent_csma_collision_probability(0.2)))
