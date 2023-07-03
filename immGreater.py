class Solution:
    def immediateGreater(self,arr,n,x):
        temp = []
        for i in arr:
            if i > x:
                temp.append(i)
        if len(temp) == 0:
            return -1
        else:
            return min(temp)