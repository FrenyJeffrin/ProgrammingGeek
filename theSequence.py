def theSequence(n):
    if n==0:
        return 1
    return n+n*(theSequence(n-1))