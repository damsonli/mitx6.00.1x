'''
In this problem you'll be given a chance to practice writing some while loops.

1. Convert the following into code that uses a while loop.

print 2
prints 4
prints 6
prints 8
prints 10
prints Goodbye!
'''
i = 2
while i <= 10:
  print(i)
  i += 2
print("Goodbye!")

'''
Answer 1:
# There are many ways to solve this problem! Here is one:
num = 2
while num < 11:
  print(num)
  num += 2
print("Goodbye!")

# Here is another:
num = 2
while num <= 10:
  print(num)
  num += 2
print("Goodbye!")

# And another:
num = 0
while True:
  num += 2
  print(num)
  if num >= 10:
    print("Goodbye!")
    break

# And one more:
num = 1
while num <= 10:
  if num % 2 == 0:
    print(num)
  num += 1
print("Goodbye!")

# There are always many, many different ways to solve a programming
# problem. Here are just four examples and surely there are quite
# a few more.
'''

'''
2. Convert the following into code that uses a while loop.

prints Hello!
prints 10
prints 8
prints 6
prints 4
prints 2
'''
i = 10
print("Hello!")
while i > 0:
  print(i)
  i -= 2

'''
Answer 2:
# There are always many ways to solve a programming problem. Here is one:
print("Hello!")
num = 10
while num > 0:
  print(num)
  num -= 2

# Here is another:
num = 11
print("Hello!")
while num > 1:
  num -= 1
  if num %2 == 0:
    print(num)
'''

'''
3. Write a while loop that sums the values 1 through end, inclusive. end is a variable that we define for you. 
So, for example, if we define end to be 6, your code should print out the result:

21
which is 1 + 2 + 3 + 4 + 5 + 6.

For problems such as these, do not include input statements or define variables we will provide for you. Our 
automating testing will provide values so write your code in the following box assuming these variables are already defined.
'''

sums = 0
i = 1
while i<=end:
  sums += i
  i += 1
print(sums)

'''
Answer 3:
# Here is one of a few ways to solve this problem:
total = 0
current = 1
while current <= end:
  total += current
  current += 1

print(total)
'''