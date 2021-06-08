### Question: Given 2 strings, write a method to decide if one is a permutation of the other.

def checkPerm(s1, s2):

  # Assumption 1: comparison is not case sensitive
  # Assumption 2: Whitespace is not significant

  s1, s2 = s1.lower().strip(), s2.lower().strip()
  # print(s1, s2)

  # Compare strings length
  if len(s1) != len(s2):
    return False

  sorted_s1 = sorted(s1)
  sorted_s2 = sorted(s2)

  if sorted_s1== sorted_s2:
    return True
  else:
    return False

print(checkPerm("ABC   ", "cba"))
print(checkPerm("ABC   ", "Reem"))

### Another solution using character frequency

def checkPerm_Freq(s1, s2):
  
  # Assumption 1: comparison is not case sensitive
  # Assumption 2: Whitespace is not significant

  s1, s2 = s1.lower().strip(), s2.lower().strip()
  # print(s1, s2)

  # Compare strings length
  if len(s1) != len(s2):
    return False

  # create an array of character frequency for s1
  arr = [0]*128 # Assumption 3: ASCII characters are 128

  for i in range(len(s1)):
    index = ord(s1[i])
    arr[index] += 1
  # print(arr)

  for i in range(len(s2)):
    index = ord(s2[i])
    arr[index] -= 1
    if arr[index] < 0:
      return False

  return True

print(checkPerm_Freq("abc", "cba"))
print(checkPerm_Freq("abc", "reem"))
