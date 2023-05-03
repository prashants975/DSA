def Count_Sort(A, k):
    """
    A: Array to be sorted
    k: unique value integers
    """

    C = [0]*k #Count Array

    # Get the individual count of each unique value
    for j in range(len(A)):
        C[A[j]] += 1
    #print(C)

    # Cummulative aggregation of Counts
    for i in range(1,k):
        C[i] = C[i] + C[i-1] #here the values of the arr are index of sorted arr
    #print(C)

    sorted_A = [None] * (len(A) + 1) #+1 for zero
    for a in reversed(A):
        sorted_A[C[a]] = a 
        C[a] -= 1
        #print(sorted_A)
    return sorted_A

A = [6,5,3,1,8,7,2,4]
print("Array:", A)
A = Count_Sort(A, k = 9) # values till 8 and +1 for 0
print("Sorted Array:", A)

