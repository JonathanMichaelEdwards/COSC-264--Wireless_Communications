def match (dst, netaddr, k):
    return dst & bitmasks[k] == netaddr & bitmasks[k]
