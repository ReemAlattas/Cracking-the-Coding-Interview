### Question: Perform basic string compression using the count of repeated characters.

def compress(s):

  # convert s to lowercase and remove whitespaces
  s = s.lower().replace(" ", "")
  print(s, len(s))

  # create a dictionary to count character frequency
  s_dict = {}
  for c in s:
    if c in s_dict:
      s_dict[c] += 1
    else:
      s_dict[c] = 1

  print(s_dict)

  # convert dictionary to string
  res = ""
  for key, value in s_dict.items():
    res = res + key + str(value)

  return res

print(compress("aabbbc"))