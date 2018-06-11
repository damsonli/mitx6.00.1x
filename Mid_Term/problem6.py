"""
Write a recursive Python function, given a non-negative integer N, to calculate and return the sum 
of its digits.

Hint: Mod (%) by 10 gives you the rightmost digit (126 % 10 is 6), while doing integer division by 
10 removes the rightmost digit (126 // 10 is 12).

This function has to be recursive; you may not use loops!

This function takes in one integer and returns one integer.

def sumDigits(N):
    '''
    N: a non-negative integer
    '''
    # Your code here
"""
def sumDigits(N):
    '''
    N: a non-negative integer
    '''
    # Your code here
    if N == 0:
        return 0
    else:
        return sumDigits(N // 10) + N % 10

print(sumDigits(126))
print(sumDigits(0))