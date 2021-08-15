def find_max(A):

  def rmax(lo, hi):
    if lo == hi:
      return A[lo]

    print('lo:',lo,'hi:',hi)
    mid = (lo+hi) // 2
    # print('mid:',mid)
    L = rmax(lo, mid)
    print('lo:',lo,'hi:',hi)
    # print('L:',L)
    # print('mid2:',mid)
    R = rmax(mid+1, hi)
    # print('R:',R)
    return max(L, R)

  return rmax(0, len(A)-1)

find_max([1, 20, -12, 50, 400])