class Node:
  def __init__(self, data = None, next = None):
    self.data = data
    self.next = next
class LinkedList:
  def __init__(self):
    self.head = None
  def insert_at_begining(self, data):
    node = Node(data, self.head)
    self.head = node

  def insert_at_end(self, data):
    if self.head is None:
      self.insert_at_begining(data)
      return
    itr = self.head
    while itr.next:
      itr = itr.next
    itr.next = Node(data, None)

  def insert_values(self, data_list):
    self.head = None
    for data in data_list:
      self.insert_at_end(data)
    
  def get_length(self):
    itr = self.head
    count = 0
    while itr:
      count += 1
      itr = itr.next
    print(count)

  def print(self):
    if self.head is None:
      print("Linked list is Empty")
      return
    itr = self.head
    while itr:
      print(itr.data, end=" ")
      itr = itr.next

  def remove_at(self, index):
    if index < 0 and index >= self.get_length():
      raise Exception("Invalid index")
    if index == 0:
      self.head = self.head.next
      return
    
    count = 0
    itr = self.head
    while itr:
      if count == index - 1:
        itr.next = itr.next.next # remove a node
        break

      itr = itr.next
      count += 1

  def insert_at(self, index, data):
    if index < 0 and index >= self.get_length():
      raise Exception("Invalid index")
    if index == 0:
      self.insert_at_begining(data)
      return
    
    count = 0
    itr = self.head
    while itr:
      if count == index - 1:
        itr.next = Node(data, itr.next)
        break      
      itr = itr.next
      count += 1
      
      
if __name__ == '__main__':
  ll = LinkedList()
  ll.insert_at_end(20)
  ll.insert_at_begining(10)
  ll.insert_at_begining(7)
  ll.insert_at_end(22)
  ll.insert_at_begining(4)
  ll.print()
  print()
  ll.insert_at(2, 19)
  ll.print()
  

