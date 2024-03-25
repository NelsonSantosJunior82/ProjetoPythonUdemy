# Try, except, else e finally (parte 2)

try:
    print('ABRIR ARQUIVO')
    8/0
except ZeroDivisionError:
    print('DIVIDIU POR ZERO')
else:
    print('NÃO DEU ERRO')
finally:
    print('FECHAR ARQUIVO')
