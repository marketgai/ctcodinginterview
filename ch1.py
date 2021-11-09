#1
def uniq(str1):
    letters={}
    for letter in str1:
        if letter in letters:
            return False
        else:
            letters[letter] = 1
    return True

# uniq("1these")

def unique(string):
  for letter in string:
    if string.count(letter) > 1:
      return False
  return True

# unique("these")


#2 Check permutation
def permute(str1, str2):
  letters1 = {}
  letters2 = {}
  for letter in str1:
    if letter in letters1:
      letters1[letter] += 1
    else:
      letters1[letter] = 1
  for letter in str2:
    if letter in letters2:
      letters2[letter] += 1
    else:
      letters2[letter] = 1
  if letters1.keys() != letters2.keys():
    return False
  else:
    for key in letters1:
      if letters1[key] != letters2[key]:
        return False
    return True

# print(permute('helloee', 'elolhee'))

#3 urlify
def urlify(str1):
  s = ''
  for l in str1:
    if l == ' ':
      s += '%20'
    else:
      s += l
  return s

# print(urlify('my john smith'))

#4 palindrome permutation
def pal(str1):
  ls = {}
  singles = 0
  for l in str1:
    if l.isalpha():
      if l.lower() in ls:
        ls[l.lower()]+=1
      else:
        ls[l.lower()] = 1
  for val in ls.values():
    if val % 2 != 0:
      singles += 1
      if singles > 1:
        return False
  return True

# print(pal('Tact Coa'))

#5 One Away
def oneAway(str1, str2):
  diff = len(str1)-len(str2)
  a = 0
  b = 0
  changes = 0
  while a < len(str1) or b < len(str2):
    if abs(diff) > 1:
      return False
    #if str1 is longer
    if (b >= len(str2) or a >= len(str1)):
      return False
    elif (diff == 1):
      if b >= len(str2):
        return False
      if str1[a] == str2[b]:
        a+=1
        b+=1
      else:
        a+=1
        changes+=1
        if changes > 1:
          return False
    elif (diff == -1):
      if a >= len(str1):
        return False
      if str1[a] == str2[b]:
        a+=1
        b+=1
      else:
        b+=1
        changes+=1
        if changes > 1:
          return False
    else:
      if str1[a] == str2[b]:
        a+=1
        b+=1
      else:
        changes += 1
        a+=1
        b+=1
        if changes>1:
          return False
  return True

# print(oneAway('pale', 'ple'))
# print(oneAway('pales', 'pale')) #this one fails bc length of string.. if last one and changes = 0 continue
# print(oneAway('pale', 'bale'))
# print(oneAway('pale', 'bake'))


#6 string compression
def compress(str1):
  result = ''
  count = 0
  letter = str1[0]
  for char in str1:
    if char == letter:
      count += 1
    else:
      result += f'{letter}{count}'
      count = 1
      letter = char
  result += f'{letter}{count}'
  return result
print(compress('abbcccaa'))


#7 rotate matrix
def rotate(matrix):
  newMatrix = []
  r = len(matrix) - 1
  n = 0
  while r > 0:
    for y in matrix:
      for x in y:
        if x == n:
          old
          x = r
          matrix[y][x] = 






