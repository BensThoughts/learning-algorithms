class Entry:
  def __init__(self, k, v) -> None:
      self.key = k
      self.value = v

class Hashtable:
  def __init__(self, M=10) -> None:
      self.table = [None] * M
      self.M = M
      self.N = 0
  
  def get(self, k):
    hc = hash(k) % self.M
    while self.table[hc]:
      if self.table[hc].key == k:
        return self.table[hc].value
      hc = (hc + 1) % self.M
    return None

  def put(self, k, v):
    hc = hash(k) % self.M
    while self.table[hc]:
      if self.table[hc] == k:
        self.table[hc].value = v
        return
      hc = (hc + 1) & self.M
    
    if self.N >= self.M - 1:
      raise RuntimeError ('Table is Full.')

    self.table[hc] = Entry(k, v)
    self.N += 1

table = Hashtable(1000)
table.put('April', 30)
table.put('May', 31)
table.put('September', 30)

print(table.get('August'))     # Miss: should print None since not present
print(table.get('September')) 