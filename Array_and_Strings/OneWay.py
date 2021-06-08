### Question: There are 3 types of edits that can be performed on strings: inset char, remove char, or replace char. Given 2 strings, write a function to check if they are one edit (or zero edits) away.

### Method uses string intersection

def oneAway(s1, s2):
  s1 = s1.lower().strip()
  s2 = s2.lower().strip()
  
  l1 = len(s1)
  l2 = len(s2) 

  if l1 == l2:
    if s1 == s2:
      return True
  elif l1 > l2:
    str1 = s1
    str2 = s2
  else:
    str1 = s2
    str2 = s1

  count = 0
  for c in str1:
    if c not in str2:
      count += 1
  
  if count > 1:
    return False
  else:
    return True
    
print(oneAway("pale", "ple"))
print(oneAway("pales", "pale"))
print(oneAway("pale", "bae"))

### Time Complexity = O(n)