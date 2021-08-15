def merge_sort(A):
  aux = [None] * len(A)

  def rsort(lo, hi):
    if hi <= lo: return

    mid = (lo+hi) // 2
    rsort(lo, mid)
    rsort(mid+1, hi)
    merge(lo, mid, hi)

  def merge(lo, mid, hi):
    aux[lo:hi+1] = A[lo:hi+1]

    left = lo
    right = mid+1

    for i in range(lo, hi+1):
      if left > mid:
        A[i] = aux[right]
        right += 1
      elif right > hi:
        A[i] = aux[left]
        left += 1
      elif aux[right] < aux[left]:
        A[i] = aux[right]
        right += 1
      else:
        A[i] = aux[left]
        left += 1
        
  rsort(0, len(A)-1)