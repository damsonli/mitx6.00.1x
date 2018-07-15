'''
Implement a function that meets the specifications below.

For example,
  cipher("abcd", "dcba", "dab") returns (order of entries in dictionary may not be the same) 
  ({'a':'d', 'b': 'c', 'd': 'a', 'c': 'b'}, 'adc')
'''

def cipher(map_from, map_to, code):
  """
  map_from, map_to: strings where each contain N unique lowercase letters. 
  code: string (assume it only contains letters also in map_from)
  Returns a tuple of (key_code, decoded).
    key_code: a dictionary with N keys mapping str to str where 
              each key is a letter in map_from at index i and the corresponding 
              value is the letter in map_to at index i. 
    decoded: a string that contains the decoded version of code using the key_code mapping.
  """
  # Your code here
  key_code = {}
  decoded = []

  for i in range(len(map_from)):
    key_code[map_from[i]] = map_to[i]

  for letter in code:
    decoded.append(key_code[letter])

  return (key_code, ''.join(decoded))

map_from = "abcd"
map_to = "dcba"
code = "dab"

print(cipher(map_from, map_to, code))