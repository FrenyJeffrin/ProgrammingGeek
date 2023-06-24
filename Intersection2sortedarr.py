def printIntersection(a,b):
    m=len(a)
    n=len(b)
    i=0
    j=0
    while i<m and j<n:
        if i>0 and a[i]==a[i-1]:
            i+=1
            continue
        if a[i]<b[j]:
            i+=1
        elif a[i]>b[j]:
            j+=1
        else:
            print(a[i],end=" ")
            i+=1
            j+=1
            

