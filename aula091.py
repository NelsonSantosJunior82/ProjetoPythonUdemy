# Intrução á Generators functions em Python

# generator = (n for n in range(1000000))

def generator(n=0):
    yield 1
    print('Continuando...')
    yield 2


gen = generator(n=0)
print(next(gen))
print(next(gen))
