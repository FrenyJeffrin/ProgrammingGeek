class Solution:
    def insert(self, alist, index, n):
        for i in range(0,n):
            self.index=i
            alist[index]=alist[i]
    def insertionSort(self, alist, n):
        for i in range(1,n):
            x=alist[i]
            j=i-1
            while j>=0 and x<alist[j]:
                alist[j+1]=alist[j]
                j=j-1
            alist[j+1]=x