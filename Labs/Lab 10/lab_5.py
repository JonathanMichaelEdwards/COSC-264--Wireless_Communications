# Q5 
# print(hex((0xE34F+0x2396 + 1) & 0xFFFF)) # 0x06E6

# Q6, Q7
s = (0xE34F+0x2396+0x4427+0x99F3)
print(hex(s+1))  # +1 for the carry


# print(hex(0xFFFF - (s+1)))
print(hex(~(s+1) & 0xFFFFFFF))

# Q8
g = 0b110011
d = 0b11100011

# print(bin(d % g))

