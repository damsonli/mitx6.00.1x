"""
Write a generator, genPrimes, that returns the sequence of prime numbers on successive calls to its next() method: 2, 3, 5, 7, 11, ...
Hints
Ideas about the problem

Have the generator keep a list of the primes it's generated. A candidate number x is prime if (x % p) != 0 for all earlier primes p.
"""

def genPrimes():
    primes = []
    number = 1

    while True:
        number += 1
        for prime in primes:
            if number % prime == 0:
                break
        else:
            primes.append(number)
            yield number


prime = genPrimes()
for i in range(10):
    print(prime.__next__())

"""
Answer:

# Note that our solution makes use of the for/else clause, which 
# you can read more about here:
# http://docs.python.org/release/1.5/tut/node23.html 

def genPrimes():
    primes = []   # primes generated so far
    last = 1      # last number tried
    while True:
        last += 1
        for p in primes:
            if last % p == 0:
                break
        else:
            primes.append(last)
            yield last
"""


