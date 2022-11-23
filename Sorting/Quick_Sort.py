def swap(a,b):
    return b,a

def Partition(A, p, r):
    
    pivot = A[p]

    i = p;
    for j in range(p+1, r+1):
        if A[j] < pivot:
            i += 1
            A[i],A[j]=swap(A[i],A[j])
            
    
    A[i], A[p] = swap(A[i], A[p])

    return i

    
def QuickSort(A, p, r):

    if p < r:
        q = Partition(A, p, r)
        A = QuickSort(A, p, q-1)
        A = QuickSort(A, q+1, r)

    return A


A = [6,5,3,1,8,7,2,4]
print("Array:", A)
A = QuickSort(A, 0, len(A) - 1 )
print("Sorted Array:", A)