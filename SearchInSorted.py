class Solution:
    def searchInSorted(self,arr,N,K):
        for i in range(0,N):
            if arr[i]==K:
                return 1
        return -1