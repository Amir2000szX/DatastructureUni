from Listing import List
import math
def merge(arr:List,p,q,r):
    
    leftArr = [None]*(q-p+2)
    rightArr = [None]*(r-q+1)
    leftArr[-1] = float("inf")
    rightArr[-1] = float("inf")

    for i in range(0,q-p+1):
        leftArr[i] = arr[i]
    for j in range(q-p+1,r+1):
        rightArr[j-(q-p)-1] = arr[j]
    i = 0
    j = 0
    for k in range(r-p+1):
        if leftArr[i] < rightArr[j]:
            arr[k] = leftArr[i]
            i += 1
        else :
            arr[k] = rightArr[j]
            j += 1
    return arr

def Msort(arr,p,r):
    if p < r:
        q = math.floor((p+r)/2)
        Msort(arr,p,q)
        Msort(arr,q+1,r)
        merge(arr,p,q,r)
    else :
        return arr[p]
print(Msort([3, 41, 52, 26, 38, 57, 9, 49],0,7))
    
