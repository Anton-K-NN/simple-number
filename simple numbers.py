from itertools import takewhile
import itertools

def primes():
    a = 2
    pr=[2]
    yield a
    while True:  # просто пример
        a+=1
        for j in range(2,a):
            if a%j==0:
               break
        else:
            yield a

print(list(itertools.takewhile(lambda x : x <= 31, primes())))