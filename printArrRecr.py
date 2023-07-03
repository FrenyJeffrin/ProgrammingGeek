class Solution:
    def printArrayRecursively(self,arr,n):
        if n==0:
            return 
        self.printArrayRecursively(arr,n-1)
        print(arr[n-1],end=" ")
