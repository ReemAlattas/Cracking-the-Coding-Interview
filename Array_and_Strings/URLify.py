### Replace all spaces in a string with '%20'.

def urlify(s, n):
  ### s is the input string
  ### n is the true length of the string 

  res = s[:n]
  res = res.replace(" ", "%20")

  return res

str = "Mr John Smith        "
print(urlify(str, 13))
