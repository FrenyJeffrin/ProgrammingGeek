class Solution:
    def printNos(self,N):
        if N==0:
            return 
        self.printNos(N-1)
        print(N,end=" ")