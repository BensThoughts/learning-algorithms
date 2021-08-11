from hashlib import md5

def hash2(s):
  return int(md5(s.encode()).hexdigest(), 16)


class LinkedEntry:
  def __init__(self, k, v, rest=None) -> None:
      self.key = k
      self.value = v
      self.next = rest

class Hashtable:
  def __init__(self, M=10) -> None:
      self.table = [None] * M
      self.M = M
      self.N = 0

  def get(self, k):
    hc = hash2(k) % self.M
    entry = self.table[hc]
    while entry:
      if entry.key == k:
        return entry.value
      entry = entry.next
    return None

  def put(self, k, v):
    hc = hash2(k) % self.M
    entry = self.table[hc]
    while entry:
      if entry.key == k:
        entry.value = v
      entry = entry.next

    self.table[hc] = LinkedEntry(k, v, self.table[hc])
    self.N += 1

  def remove(self, k):
    hc = hash2(k) % self.M
    entry = self.table[hc]
    prev = None
    while entry:
      if entry.key == k:
        if prev:
          prev.next = entry.next
        else:
          self.table[hc] = entry.next

        self.N -= 1
        return entry.value

      prev, entry = entry, entry.next

    return None


table = Hashtable(10)
table.put('April', 30)
table.put('May', 31)
table.put('August', 31)
table.put('September', 30)
table.put('October', 31)
table.put('November', 30)
table.put('December', 31)


print(table.get('August'))     # Miss: should print None since not present
print(table.get('September')) 

# x = table.table
# c = 0
# for i in x:
#   print(c, ':', i)
#   c += 1
#   n = i
#   if (n):
#     count = 1
#     while n.next:
#       n = n.next
#       print('   ', count, ':', n)
#       count += 1
  
# x = table.table
# c = 0
# for i in x:
#   print(c, ':', i)
#   c += 1
#   if i:
#     count = 1
#     while i.next:
#       i = i.next
#       print('   ', count, ':', i)
#       count += 1
    


# print(md5(b'test').hexdigest() % 10)
# print(int(md5("test".encode()).hexdigest(), 16) % 10)


