class Solution:
    def isSorted(self,arr,n):
        l = sorted(arr)
        m = sorted(arr, reverse = True)
        if arr == l or arr == m:
            return 1
        else:
            return 0