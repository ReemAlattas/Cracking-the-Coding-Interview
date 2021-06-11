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
  
### Solution 1: Iteration and an array

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

### Solution 2: Iteration without additional data structure

def kthToLast_no_arr(ll, k):
  p1 = ll.head
  p2 = ll.head

  if k == 0:
    k = 1

  # move p1 to the kth element
  for _ in range(k):
    if p1 == None:
      return -1
    p1 = p1.next

  # move p1 and p2. When p1 hits the end, p2 hit the Kth to last elemnt

  while p1:
    p1 = p1.next
    p2 = p2.next
  
  return p2.data


###

llist = LinkedList()
 
llist.head = Node(1)
second = Node(2)
third = Node(3)
fourth = Node(4)

llist.head.next = second # Link first node with second
second.next = third # Link second node with the third node
third.next = fourth

llist.printList()

# print(kthToLast(llist, 0))
# print(kthToLast(llist, 1))
# print(kthToLast(llist, 2))

print(kthToLast_no_arr(llist, 0))
print(kthToLast_no_arr(llist, 1))
print(kthToLast_no_arr(llist, 2))



### Time complexity = O(n)
### Space Complexity = O(n)