###
# Implement an algorithm to determine if a string has all unique charaters.
###

### 1 - Solution using dictionary data structure

def isUnique(s):
  # check string length
  MAX_CHAR = 265
  if len(s) > MAX_CHAR:
    return False
  
  # create a dictionary
  s_dict = {}
  
  # calculate character frequency
  for c in s:
    if c in s_dict:
      s_dict[c] += 1
    else:
      s_dict[c] = 1

  # print(s_dict)

  # sort dictionary by value descendingly
  sorted_dict = sorted(s_dict.items(), key = lambda x: x[1], reverse = True)
  # print(sorted_dict)

  if sorted_dict[0][1] == 1:
    return True
  else:
    return False

# Time complexity = O(nlogn) because of the sorted function

res = isUnique("aabbcc")
print(res)

### 2 - Solution using Array data structure

def isUnique_arr(s):
  #check if string length > 256 charcter then return False
  # check string length
  MAX_CHAR = 265

  if len(s) > MAX_CHAR:
    return False
  
  # create an array of characters
  arr = [False]*MAX_CHAR

  for c in s:
    index = ord(c) # ord() returns an integer representing the unicode character
    if arr[index]:
      return False
    arr[index] = True

  return True

# Time complexity O(n)

res = isUnique_arr("aabbcc")
print(res)

### 3 - Solution without using additional data structure
def isUnique_noDS(s):
  sorted_s = sorted(s)
  # print(sorted_s)

  for i in range(len(sorted_s)-1):
    if sorted_s[i] == sorted_s[i+1]:
      return False
  return True

# Time complexity = O(nlogn)

res = isUnique_noDS("aabbcc")
print(res)
