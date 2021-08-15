def partition(A, lo, hi, idx):
  """Partition using A[idx] as value."""
  if lo == hi: return lo

  A[idx], A[lo] = A[lo], A[idx] # swap into position
  i = lo
  j = hi + 1
  while True:
    while True:
      i += 1
      if i == hi: break
      if A[lo] < A[i]: break

    while True:
      j -= 1
      if j == lo: break
      if A[j] < A[lo]: break

    if i >= j: break
    A[i], A[j] = A[j], A[i]
    print(A)

  A[lo], A[j] = A[j], A[lo]
  return j

def quick_sort(A):

  def qsort(lo, hi):
    if hi <= lo:
      return
    
    pivot_idx = lo
    location = partition(A, lo, hi, pivot_idx)
    print(A)

    qsort(lo, location-1)
    qsort(location+1, hi)

  qsort(0, len(A)-1)

# B = [15, 21, 20, 2, 15, 24, 5, 19]
# partition(B, 0, 7, 0)
# print(B)

C = [15, 21, 20, 2, 15, 24, 5, 19]
quick_sort(C)
print(C)