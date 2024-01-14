"""
Exercícios com funções

Crie uma função que multiplica todos os argumentos
não nomeados não recebidos
Retorne o total para uma variável e mostre
o valor da variável
"""


def multiplicar(*args):
    total = 0
    for numero in args:
        total *= numero
    return total

multiplicacao = multiplicar(1, 2, 3, 4, 5)
print(multiplicacao)
