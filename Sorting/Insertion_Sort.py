def InsertionSort(A):
    for j in range(1, len(A)):
        k = A[j]    # key to insert in sorted array 
        i = j - 1

        # insert till the first location or till when the left ele is smaller than key
        while i >= 0 and A[i] > k:
            A[i+1] = A[i]
            i = i - 1

        A[i+1] = k

    return A

A = [6,5,3,1,8,7,2,4]
print("Array:", A)
A = InsertionSort(A)
print("Sorted Array:", A)

