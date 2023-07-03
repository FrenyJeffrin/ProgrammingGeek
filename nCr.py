def nCr(n,r):
    if n==0 or r==0 or n-r ==0:
        return 1
    return nCr(n-1,r-1)+nCr(n-1,r)