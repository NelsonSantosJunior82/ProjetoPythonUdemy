# Generator expression, Iterables, Iterators em Python

import sys

iterable = ['Eu', 'tenho', '__iter__']
iterator = iter(iterable)
print(next(iterator))

lista = [n for n in range(1000000)]
generator = (n for n in range(1000000))

print(sys.getsizeof(lista))
print(sys.getsizeof(generator))
