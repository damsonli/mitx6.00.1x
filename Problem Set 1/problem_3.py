"""
Assume s is a string of lower case characters.

Write a program that prints the longest substring of s in which the letters occur in alphabetical order.
For example, if s = 'azcbobobegghakl', then your program should print

Longest substring in alphabetical order is: beggh

In the case of ties, print the first substring. For example, if s = 'abcbcd', then your program should print

Longest substring in alphabetical order is: abc
"""

s = str(input("Input your string: "))
longest = s[0]

for i in range(len(s) - 1):
    temp_str = s[i]
    j = i
    while s[j] <= s[j+1]:
        temp_str += s[j+1]
        if j == len(s) - 2:
            break
        else:
            j += 1
    if len(temp_str) > len(longest):
        longest = temp_str

print("Longest substring in alphabetical order is: " + longest)