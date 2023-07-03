import math
class Solution:
    def median(self,A,N):
        A.sort()
        if N%2==0:
            mid=(A[N//2-1]+A[N//2])/2
            return math.floor(mid)
        else:
            mid=A[N//2]
            return math.floor(mid)
    def mean(self,A,N):
        sum=0
        for i in range(N):
            sum+=A[i]
        mean=sum/N
        return math.floor(mean)