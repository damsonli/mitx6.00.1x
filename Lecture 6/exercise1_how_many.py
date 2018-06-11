'''
Consider the following sequence of expressions:
  animals = { 'a': ['aardvark'], 'b': ['baboon'], 'c': ['coati']}

  animals['d'] = ['donkey']
  animals['d'].append('dog')
  animals['d'].append('dingo')

We want to write some simple procedures that work on dictionaries to return information.

First, write a procedure, called how_many, which returns the sum of the number of values associated with a dictionary. For example:

>>> print(how_many(animals))
6
'''
animals = { 'a': ['aardvark'], 'b': ['baboon'], 'c': ['coati']}

animals['d'] = ['donkey']
animals['d'].append('dog')
animals['d'].append('dingo')

def how_many(aDict):
  '''
  aDict: A dictionary, where all the values are lists.

  returns: int, how many values are in the dictionary.
  '''
  total = 0
  for i in aDict.values():
    total += len(i)
  return total

print(how_many(animals))

'''
Answer:
def how_many(aDict):
  result = 0
  for value in aDict.values():
    # Since all the values of aDict are lists, aDict.values() will 
    #  be a list of lists
    result += len(value)
  return result

def how_many(aDict):
  result = 0
  for key in aDict.keys():
    result += len(aDict[key])
  return result
'''