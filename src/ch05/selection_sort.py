def selection_sort(A):
  N = len(A)
  for i in range(N-1):
    min_index = i
    for j in range(i + 1, N):
      if A[j] < A[min_index]:
        min_index = j
    
    A[i], A[min_index] = A[min_index], A[i]

  return A

print(selection_sort([4, 56, 1, 21, 3, 4]))