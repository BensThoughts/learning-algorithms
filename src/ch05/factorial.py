def fact(N):
  if N <= 1:
    return 1
  return N * fact(N-1)

print(fact(3))
print(fact(5))
print(fact(10))
print(fact(20))