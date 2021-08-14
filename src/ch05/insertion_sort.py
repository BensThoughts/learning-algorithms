def insertion_sort(A):
  N = len(A)
  for i in range(1,N):
    for j in range(i,0,-1):
      if A[j-1] <= A[j]:
        break
      A[j], A[j-1] = A[j-1], A[j]

  return A

def insertion_sort_cmp(A, less=lambda one,two: one <= two):
  N = len(A)
  for i in range(1,N):
    for j in range(i,0,-1):
      if less(A[j-1], A[j]):
        break
      A[j],A[j-1] = A[j-1],A[j]

  return A

test = lambda one, two: one >= two
print(insertion_sort_cmp([4, 56, 1, 21, 3, 4], lambda one, two: one >= two))