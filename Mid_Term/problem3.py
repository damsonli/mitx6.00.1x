'''
def closest_power(base, num):
    """
    base: base of the exponential, integer > 1
    num: number you want to be closest to, integer > 0
    Find the integer exponent such that base**exponent is closest to num.
    Note that the base**exponent may be either greater or smaller than num.
    In case of a tie, return the smaller value.
    Returns the exponent.
    """

For example,
  closest_power(3,12) returns 2
  closest_power(4,12) returns 2
  closest_power(4,1) returns 0

Paste your entire function, including the definition, in the box below. Do not leave any debugging print statements.
'''
def closest_power(base, num):
    '''
    base: base of the exponential, integer > 1
    num: number you want to be closest to, integer > 0
    Find the integer exponent such that base**exponent is closest to num.
    Note that the base**exponent may be either greater or smaller than num.
    In case of a tie, return the smaller value.
    Returns the exponent.
    '''
    i = 0
    while abs(base ** i - num) > abs(base ** (i + 1) - num):
      i += 1
    
    return i

print(closest_power(3,12))
print(closest_power(4,12))
print(closest_power(4,1))
print(closest_power(1,5))