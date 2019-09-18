def backoff (numColl):
    if (numColl <= 10):
        return 2**numColl - 1
    else: 
        return 2**10 - 1

print (backoff(11))
