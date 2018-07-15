"""
Write a Python function that takes in a string and prints out a version of this string that does not 
contain any vowels, according to the specification below. Vowels are uppercase and lowercase 'a', 
'e', 'i', 'o', 'u'.

For example, if s = "This is great!" then print_without_vowels will print Ths s grt!. If s = "a" 
then print_without_vowels will print the empty string "".

The "None" in each test case comes from the function call being printed. Your function does not 
return anything, only prints a string as described above.
"""

def print_without_vowels(s):
  '''
  s: the string to convert
  Finds a version of s without vowels and whose characters appear in the 
  same order they appear in s. Prints this version of s.
  Does not return anything
  '''
  # Your code here
  vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
  result = []

  for letter in s:
    if letter not in vowels:
      result.append(letter)
  
  print(''.join(result))

s = "This Is Great!"
print_without_vowels(s)
