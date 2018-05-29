'''
In this problem you'll be given a chance to practice writing some for loops.

1. Convert the following into code that uses a for loop.

print 2
prints 4
prints 6
prints 8
prints 10
prints Goodbye!
'''
for i in range(2,11,2):
  print(i)
print("Goodbye!")

'''
Answer 1:
# There are many ways to solve this problem! Here is one:
for count in range(11):
  if count != 0 and count % 2 == 0:
    print(count)
print("Goodbye!")

# Here is another:
for count in range(2, 12, 2):
  print(count)
print("Goodbye!")
'''

'''
2. Convert the following into code that uses a for loop.

prints Hello!
prints 10
prints 8
prints 6
prints 4
prints 2
'''
print("Hello!")
for i in range(10,0,-2):
  print(i)

'''
Answer 2:
# There are always many ways to solve a programming problem. Here is one:
print("Hello!")
for num in range(0, 10, 2):
  print(10 - num)

# Here is another:
print("Hello!")
for num in range(10, 0, -2):
  print(num)

'''

'''
3. Write a for loop that sums the values 1 through end, inclusive. end is a variable that we define for you. 
So, for example, if we define end to be 6, your code should print out the result:

21
which is 1 + 2 + 3 + 4 + 5 + 6.

For problems such as these, do not include input statements or define variables we will provide for you. 
Our automating testing will provide values so write your code in the following box assuming these variables 
are already defined.
'''
total=0
for i in range(1,end+1):
  total += i
print(total)

'''
Answer 3:
# Here is one of a few ways to solve this problem:
total = 0
for next in range(1, end+1):
  total += next
print(total)

# Here is another:
total = end
for next in range(end):
  total += next
print(total)
'''