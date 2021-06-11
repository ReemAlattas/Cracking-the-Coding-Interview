### Question: Remove duplicates from unsorted linked list.

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
  
def kthToLast(ll):
  pass

llist = LinkedList()
 
llist.head = Node(1)
second = Node(2)
third = Node(2)
fourth = Node(3)

llist.head.next = second # Link first node with second
second.next = third # Link second node with the third node
third.next = fourth

llist.printList()
