def MergeSort(arr):
    if len(arr)>1:
        mid = len(arr)//2
        L = arr[:mid]
        R = arr[mid:]
        MergeSort(L)
        MergeSort(R)
        i =j=k=0
        while i< len(L) and j<len(R):
            if L[i]<R[j]:
                arr[k] = L[i]
                i +=1
            else:
                arr[k]=R[j]
                j+=1
            k+=1
        
        while i<len(L):
            arr[k]=L[i]
            i+=1
            k+=1
        while j<len(R):
            arr[k]=R[j]
            j +=1
            k+=1
def printL():
    for i in range(len(arr)):
        print(arr[i],end="=>")
    print()
if __name__ == '__main__':
    arr = [12, 11, 13, 5, 6, 7]
    print("Given array is", end="\n")
    for x in arr:
        print(x,end="=>")
    print()
    print("Sorted array is: ", end="\n")  
    MergeSort(arr)
    printL()