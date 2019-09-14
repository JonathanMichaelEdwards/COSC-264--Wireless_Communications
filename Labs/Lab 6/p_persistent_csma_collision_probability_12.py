def p_persistent_csma_collision_probability(p):
    count = 0
    for i in range(20):
        count += (1-p)*(p)**i
    return count / (((1-p) / p) + (1 / p))
