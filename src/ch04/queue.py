class Node:
  def __init__(self, val) -> None:
      self.value = val
      self.next = None

class Queue:
  def __init__(self) -> None:
      self.first = None
      self.last = None
  
  def is_empy(self):
    return self.first is None

  def enqueue(self, val):
    if self.first is None:
      self.first = self.last = Node(val)
    else:
      self.last.next = Node(val)
      self.last = self.last.next

  def dequeue(self):
    if self.is_empy():
      raise RuntimeError('Queue is empty.')

    val = self.first.value
    self.first = self.first.next
    return val
