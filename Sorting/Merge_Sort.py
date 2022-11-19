def merge(A, left, right):

    i = 0; j = 0; k = 0

    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            A[k] = left[i]
            i += 1
        else:
            A[k] = right[j]
            j += 1
        k += 1

    while i < len(left):
        A[k] = left[i]
        i += 1
        k += 1
    
    while j < len(right):
        A[k] = right[j]
        j += 1
        k += 1



def merge_sort(A):
    
    if len(A) > 1:
        mid = int(len(A) / 2)
        left = A[:mid]
        right = A[mid:]
        merge_sort(left)
        merge_sort(right)
        merge(A, left, right)


A = [6,5,3,1,8,7,2,4]
print("Array:", A)
merge_sort(A)
print("Sorted Array:", A)