import random

def main():
  res = [random.randint(-30, 1000) for i in range(10)]
  print(res)
  print(largest(res))


def largest(A):
  my_max, second = A[:2]
  if my_max < second:
    my_max,second = second,my_max

  for idx in range(2, len(A)):
    if my_max < A[idx]:
      my_max,second = A[idx],my_max
    elif second < A[idx]:
      second = A[idx]

  # for idx in range(2, len(A)):
  #   if second < A[idx]:
  #     second = A[idx]
  #   if my_max < A[idx]:
  #     my_max, second = second, my_max
  return (my_max, second)

main()