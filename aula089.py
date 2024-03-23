# dir, hasattr, getattr em Python

string = 'Nelson'
metodo = 'upper'
if hasattr(string, metodo):
    print('Existe upper')
    print(getattr(string, metodo)())
else:
    print('Não existe método', metodo)
