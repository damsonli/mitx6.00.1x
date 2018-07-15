"""
Implement the class myDict with the methods below, which will represent a dictionary without using 
a dictionary object. The methods you implement below should have the same behavior as a dict object, 
including raising appropriate exceptions. Your code does not have to be efficient. Any code that 
uses a Python dictionary object will receive 0.

For example:

With a dict:  |    With a myDict:
-------------------------------------------------------------------------------
d = {}             md = myDict()        # initialize a new object using 
                                          your choice of implementation

d[1] = 2           md.assign(1,2)       # use assign method to add a key,value pair

print(d[1])        print(md.getval(1))  # use getval method to get value stored for key 1

del(d[1])          md.delete(1)         # use delete method to remove 
                                          key,value pair associated with key 1
"""

class myDict(object):
  """ Implements a dictionary without using a dictionary """
  def __init__(self):
    """ initialization of your representation """
    self.keys = []
    self.values = []
      
  def assign(self, k, v):
    """ k (the key) and v (the value), immutable objects  """
    if k not in self.keys:
      self.keys.append(k)
      self.values.append(v)
    else:
      index = self.keys.index(k)
      self.values[index] = v
      
  def getval(self, k):
    """ k, immutable object  """
    if k not in self.keys:
      raise KeyError(k)
    else:
      index = self.keys.index(k)
      return self.values[index]
      
  def delete(self, k):
    """ k, immutable object """   
    if k not in self.keys:
      raise KeyError(k)
    else:
      index = self.keys.index(k)
      self.keys.pop(index)
      self.values.pop(index)

md = myDict()
print(md.keys)
print(md.values)

md.assign(1,2)
print(md.keys)
print(md.values)

md.assign('a', 'c')
print(md.keys)
print(md.values)

md.assign(1,3)
print(md.keys)
print(md.values)

print(md.getval(1))
#print(md.getval('d'))

md.delete(1)
print(md.keys)
print(md.values)
md.delete('d')