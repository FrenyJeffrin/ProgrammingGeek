class Solution:    
    def termOfGP(self,A,B,N):
        r=B/A
        s=A*r**(N-1)
        return s