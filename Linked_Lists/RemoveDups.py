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
  
def removeDups(ll):
  current = ll.head
  previous = current
  visited = set()

  while current:
    if current.data in visited:
        previous.next = current.next
    else:
        visited.add(current.data)
        previous = current
    current = current.next
  return ll

llist = LinkedList()
 
llist.head = Node(1)
second = Node(2)
third = Node(2)
fourth = Node(3)

llist.head.next = second # Link first node with second
second.next = third # Link second node with the third node
third.next = fourth

llist.printList()

removeDups(llist)

llist.printList()

### How to solve this if a temporary buffer is not allowed.

def removeDups_noTemp(ll):
  runner = current = ll.head
  while current:
      runner = current
      while runner.next:
          if runner.next.data == current.data:
              runner.next = runner.next.next
          else:
              runner = runner.next
      current = current.next
  return ll