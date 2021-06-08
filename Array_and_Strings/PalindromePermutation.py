### Question: Given a string, write a function to check if it is a permutation of a palindrome. 

### Example:
### Input: Tact Coa
### Output: True (Permutations: taco, cat, atco cta, ... etc)

def palindromePermutation(s):
  # convert s to lowercase and remove whitespaces
  s = s.lower().replace(" ", "")
  # print(s, len(s))

  # create a dictionary to count character frequency
  s_dict = {}
  for c in s:
    if c in s_dict:
      s_dict[c] += 1
    else:
      s_dict[c] = 1

  # print(s_dict)

  # if the string has an even number of characters, then every character should have an even number of occurences
  # if the string has an odd number of characters, then one character should have an odd number of occurences and the remaining characters should have even number of occurences

  if (len(s) % 2 == 0):
    for key in s_dict:
      if s_dict[key] % 2 != 0:
        return False
    return True
  else:
    count = 0
    for key in s_dict:
      if s_dict[key] % 2 != 0:
        count += 1
    if count == 1:
      return True
    else:
      return False


res = palindromePermutation("Moom")
print(res)

res = palindromePermutation("Reem")
print(res)

### Time Complexity = O (N) time, where N is the length of the string