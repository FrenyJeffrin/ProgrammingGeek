class Solution:
    def smallerThanX(self,arr,n,x):
        count=0
        for i in range(n):
            if arr[i]<x:
                count+=1
        return count