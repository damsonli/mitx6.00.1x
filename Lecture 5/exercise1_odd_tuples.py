'''
Write a procedure called oddTuples, which takes a tuple as input, and returns a new tuple as output,
 where every other element of the input tuple is copied, starting with the first one. So if test is 
 the tuple ('I', 'am', 'a', 'test', 'tuple'), then evaluating oddTuples on this input would return 
 the tuple ('I', 'a', 'tuple'). 
'''

def oddTuples(aTup):
  '''
  aTup: a tuple
  returns: tuple, every other element of aTup. 
  '''
  x = ()
  for i in range(len(aTup)):
    if i % 2 == 0:
      x += (aTup[i],)
  return x

'''
Answer:

def oddTuples(aTup):
  # a placeholder to gather our response
  rTup = ()
  index = 0

  # Idea: Iterate over the elements in aTup, counting by 2
  #  (every other element) and adding that element to 
  #  the result
  while index < len(aTup):
    rTup += (aTup[index],)
    index += 2

  return rTup

def oddTuples2(aTup):
  # Here is another solution to the problem that uses tuple 
  #  slicing by 2 to achieve the same result
  return aTup[::2]
'''