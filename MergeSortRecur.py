
def mergeSort(arr,l,r):
    if r>l:
        m=(l+r)//2
        mergeSort(arr,l,m)
        mergeSort(arr,m+1,r)
        merge(arr,l,m,r)