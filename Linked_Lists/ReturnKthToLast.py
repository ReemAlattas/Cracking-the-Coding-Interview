### Question: Return the kth to last element in a singly linked list. K = 0 and K = 1 will return the last element

# Node class
class Node:
  
  # Function to initialize the node object
  def __init__(self, data):
    self.data = data  # Assign data
    self.next = None  # Initialize
                        # next as null
  
# Linked List class
class LinkedList:
    
  # Function to initialize the Linked
  # List object
  def __init__(self):
    self.head = None

  def printList(self):
    temp = self.head
    res = ""
    while (temp):
      res = res + str(temp.data) + " "
      temp = temp.next
    print(res)
  
def kthToLast(ll, k):
  length = 0
  arr = []
  current = ll.head

  while current:
    arr.append(current.data)
    length += 1
    current = current.next

  if k == 0:
    k = 1
  return arr[length-k]

llist = LinkedList()
 
llist.head = Node(1)
second = Node(2)
third = Node(3)
fourth = Node(4)

llist.head.next = second # Link first node with second
second.next = third # Link second node with the third node
third.next = fourth

llist.printList()
print(kthToLast(llist, 0))
print(kthToLast(llist, 1))
print(kthToLast(llist, 2))