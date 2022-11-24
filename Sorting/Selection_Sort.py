def SelectionSort(A):

    n = len(A)

    for j in range(0,n):
        min_idx = j
        for i in range(j+1, n):
            if A[min_idx] > A[i]:
                min_idx = i
        
        A[min_idx], A[j] = A[j], A[min_idx]

    return A


A = [6,5,3,1,8,7,2,4]
print("Array:", A)
A = SelectionSort(A)
print("Sorted Array:", A)