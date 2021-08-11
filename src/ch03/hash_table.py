class Entry:
  def __init__(self, k, v) -> None:
      self.key = k
      self.value = v

class Hashtable:
  def __init__(self, M=10) -> None:
      self.table = [None] * M
      self.M = M
  
  def get(self, k):
    hc = hash(k) % self.M
    return self.table[hc].value if self.table[hc] else None

  def put(self, k, v):
    hc = hash(k) % self.M
    entry = self.table[hc]
    if entry:
      if entry.key == k:
        entry.value = v
      else:
        raise RuntimeError('Key Collision: {} and {}'.format(k, entry.key))
    else:
      self.table[hc] = Entry(k, v)

table = Hashtable(1000)
table.put('April', 30)
table.put('May', 31)
table.put('September', 30)

print(table.get('August'))     # Miss: should print None since not present
print(table.get('September')) 