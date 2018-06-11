'''
Write a Python function that returns a list of keys in aDict that map to integer values that are 
unique (i.e. values appear exactly once in aDict). The list of keys you return should be sorted in 
increasing order. (If aDict does not contain any unique values, you should return an empty list.)

This function takes in a dictionary and returns a list.

def uniqueValues(aDict):
    """
    aDict: a dictionary
    """
    # Your code here
'''

def uniqueValues(aDict):
    '''
    aDict: a dictionary
    '''
    # Your code here
    uniqueList = []

    for key in list(aDict.keys()):
        if list(aDict.values()).count(aDict[key]) == 1:
            uniqueList.append(key)

    uniqueList.sort()
    return uniqueList
    
aDict = {'a': 1, 'b': 2, 'c': 1, 'd': 2}
#print(list(aDict.keys()))
print(uniqueValues(aDict))