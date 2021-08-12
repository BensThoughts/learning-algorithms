from hashlib import md5

def hash2(s):
  return int(md5(s.encode()).hexdigest(), 16)


class LinkedEntry:
  def __init__(self, k, v, rest=None) -> None:
      self.key = k
      self.value = v
      self.next = rest

class DynamicHashtable:
  def __init__(self, M=10) -> None:
      self.table = [None] * M
      self.M = M
      self.N = 0

      self.load_factor = 0.75
      self.threshold = min(M * self.load_factor, M-1)

  def __iter__(self):
    for entry in self.table:
      while entry:
        yield (entry.key, entry.value)
        entry = entry.next

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

    if self.N >= self.threshold:
      self.resize(2*self.M + 1)

  def resize(self, new_size):
    temp = DynamicHashtable(new_size)
    for n in self.table:
      while n:
        temp.put(n.key, n.value)
        n = n.next
    self.table = temp.table
    self.M = temp.M
    self.threshold = self.load_factor * self.M

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


table = DynamicHashtable(50)
import random
import string
# res = [random.randint(-30, 1000) for i in range(1000)]
arr = []
for i in range(200000):
  key = ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(10))
  arr.append(key)
  table.put(key, i)
# print(table.get(res[5]))
# print(table.get(res[400]))  
print(table.table.__len__())



# table.put('April', 30)
# table.put('May', 31)
# table.put('August', 31)
# table.put('September', 30)
# table.put('October', 31)
# table.put('November', 30)
# table.put('December', 31)


# print(table.get('August'))     # Miss: should print None since not present
# print(table.get('September')) 