"""
Write a Python function that takes in two lists and calculates whether they are permutations of 
each other. The lists can contain both integers and strings. We define a permutation as follows:

  the lists have the same number of elements
  list elements appear the same number of times in both lists

If the lists are not permutations of each other, the function returns False.

If they are permutations of each other, the function returns a tuple consisting of the following 
elements:

  the element occuring the most times
  how many times that element occurs
  the type of the element that occurs the most times

If both lists are empty return the tuple (None, None, None). If more than one element occurs the 
most number of times, you can return any of them.

For example,

  if L1 = ['a', 'a', 'b'] and L2 = ['a', 'b'] then is_list_permutation returns False
  
  if L1 = [1, 'b', 1, 'c', 'c', 1] and L2 = ['c', 1, 'b', 1, 1, 'c'] 
  then is_list_permutation returns (1, 3, <class 'int'>) because the integer 1 occurs the most, 
  3 times, and the type of 1 is an integer (note that the third element in the tuple is not a 
  string).
"""

def is_list_permutation(L1, L2):
  '''
  L1 and L2: lists containing integers and strings
  Returns False if L1 and L2 are not permutations of each other. 
  If they are permutations of each other, returns a tuple of 3 items in this order: 
    the element occurring most, how many times it occurs, and its type
  '''
  # Your code here
  # Return False since lists contain different number of elements
  if len(L1) != len(L2):
    return False

  # Return tuple (None, None, None) since both lists are empty
  if len(L1) == 0:
    return (None, None, None)

  # Function to generate a dictionary of element occurance for a list
  def return_element_occurance(L):
    '''
    L: a non-empty list containing integers and strings
    Return a dictionary with a pair of (key, value), where
      key: the element in L
      value: the occurance of the key
    '''
    result = {}

    for each in L:
      if each not in result.keys():
        result[each] = 1
      else:
        result[each] += 1
    
    return result

  # Function to compare two dictionaries
  def compare_dictionary(D1, D2):
    '''
    D1, D2: non-empty dictionaries
    Return true if D1 is same as D2
    '''
    if len(D1) != len(D2):
      return False
    
    for x in D1.keys():
      if x not in D2.keys():
        return False
      
      if D1[x] != D2[x]:
        return False

    return True

  def generate_tuple(D):
    '''
    D: non-empty dictionary
    Returns a tuple of 3 items in this order: 
      the element occurring most, how many times it occurs, and its type
    '''
    max = 0
    for key in D.keys():
      if D[key] > max:
        max = D[key]
        element = key
    
    return (element, max, type(element))

  dict_L1 = return_element_occurance(L1)
  dict_L2 = return_element_occurance(L2)

  if not compare_dictionary(dict_L1, dict_L2):
    return False
  else:
    return generate_tuple(dict_L1)


L1 = ['c', 'b', 1, 'c', 'c', 1, 2]
L2 = [2, 1, 'b', 1, 'c', 'c', 'd']
print(is_list_permutation(L1, L2))