"""Given a sorted array arr[] of size N without duplicates, and given a value x. 
Floor of x is defined as the largest element K in arr[] such that K is smaller than or equal to x. 
Find the index of K(0-based indexing)."""

class Solution:
    def findFloor(self,A,N,X):
        max = 0
        for i in range(0, N):
            if A[i] > max and A[i] <= X:
                max = A[i]
        for i in range(0, N):
            if A[i] == max:
                return i
        return -1
        