'''
Implement a function that meets the specifications below.

def deep_reverse(L):
    """ assumes L is a list of lists whose elements are ints
    Mutates L such that it reverses its elements and also 
    reverses the order of the int elements in every element of L. 
    It does not return anything.
    """
    # Your code here

For example, if L = [[1, 2], [3, 4], [5, 6, 7]] then deep_reverse(L) mutates L to be [[7, 6, 5], [4, 3], [2, 1]]

Paste your entire function, including the definition, in the box below. Do not leave any debugging print statements.

Please read carefully. The question states that you need to mutate L. Your code must work when you do this:

L = [[0, 1, 2], [1, 2, 3], [3, 2, 1], [10, -10, 100]]
deep_reverse(L) 
print(L)
'''

def deep_reverse(L):
    """ assumes L is a list of lists whose elements are ints
    Mutates L such that it reverses its elements and also 
    reverses the order of the int elements in every element of L. 
    It does not return anything.
    """
    # Your code here
    for element in L:
        element.reverse()
    
    L.reverse()

L1 = [[1, 2], [3, 4], [5, 6, 7]]
deep_reverse(L1)
print(L1)

L2 = [[0, 1, 2], [1, 2, 3], [3, 2, 1], [10, -10, 100]]
deep_reverse(L2)
print(L2)