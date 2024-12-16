from Listing import List

# def insertionSort(arr:List):
    
#     for i in range(1,len(arr)):
#         j = i-1
#         while j >= 0 and arr[j] >= arr[i] :
#             arr[j] , arr[i] = arr[i] , arr[j]
#             i = j
#             j -= 1
#         j = 0
#     return arr
# print(insertionSort([5,2,4,6,1,3]))

def insertionSort(arr:List):
    k = 0
    for i in range(1,len(arr)):
        k+=1
        key = arr[i]
        j = i-1
        while j>=0 and arr[j] < key:
            arr[j+1] = arr[j]
            
            j -= 1
        arr[j+1] = key
    return arr,k
print(insertionSort([1,2,6,5,3,7,5,2,1]))

#nonincreasingSort
#E 2.1.2
# def NIinsertionSort(arr:List):
#     for i in range(len(arr)-2,-1,-1):
#         key = arr[i]
#         j = i + 1
#         while j<len(arr) and key < arr[j]:
#             arr[j-1] = arr[j]
#             j +=1
#         arr[j-1] = key
#     return arr
# print(NIinsertionSort([7,5,3,6,2,1]))

