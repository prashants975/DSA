def swap(a,b):
    return b,a

def BubbleSort(A):
    
    k = 0
    swapped = True
    while swapped:
        swapped = False

        for i in range(len(A) - k - 1):
            if A[i] > A[i+1]:
                A[i], A[i+1] = swap(A[i], A[i+1])
                swapped = True
        k += 1

    return A

A = [6,5,3,1,8,7,2,4]
print("Array:", A)
A = BubbleSort(A)
print("Sorted Array:", A)