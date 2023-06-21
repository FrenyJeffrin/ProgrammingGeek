class Solution:
    def leftIndex (self, N, arr, X):
        l=0
        r=N-1
        while l<=r:
            m=(l+r)//2
            if X>arr[m]:
                l=m+1
            elif X<arr[m]:
                r=m-1
            else:
                if m==0 or arr[m-1]!=arr[m]:
                    return m
                else:
                    r=m-1
        return -1