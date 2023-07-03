
def mergeSort(a,low,high):
    if high>low:
        mid=(low+high)//2
        mergeSort(a,low,mid)
        mergeSort(a,mid+1,high)
        mergeSubarrays(a,low,mid,high)