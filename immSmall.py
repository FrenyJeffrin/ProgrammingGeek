class Solution:
    def immediateSmaller(self,arr,n,x):
        res=0
        if n<=1 or x==1:
            return -1
        for i in arr:
            if (i>res) and (i<x):
                res=i
        return res