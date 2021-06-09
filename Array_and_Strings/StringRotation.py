### Question: Assume you have a method isSubstring which checks if one word is a substring of another. Given 2 strings, s1 and s2, write code to check if s2 is a rotation of s1 using only one call to isSubstring.

def isSubstring(s1, s2):
  if s2 in s1:
    return True
  else:
    return False

def isRotation(s1, s2):
  s1 += s1
  res = isSubstring(s1, s2)
  return res

print(isRotation("waterbottle", "erbottlewat"))