'''
FUNÇÃO LAMBDA EM PYTHON

A função lambda é uma função como qualquers
outra em Python. Porém, são funções anônimas
que contém apenas uma linha. Ou seja, tudo
deve ser contido dentro de um a única
expressão.
lista = [
    {nome:'Luiz', sobrenome:'Miranda'},
    {nome:'Maria', sobrenome:'Oliveira'},
    {nome:'Daniel', sobrenome:'Silva'},
    {nome:'Eduardo', sobrenome:'Moreira'},
    {nome:'Aline', sobrenme:'Souza'}
]
'''
lista = [
    {'nome': 'Luiz', 'sobrenome': 'Miranda'},
    {'nome': 'Maria', 'sobrenome': 'Oliveira'},
    {'nome': 'Daniel', 'sobrenome': 'Silva'},
    {'nome': 'Eduardo', 'sobrenome': 'Moreira'},
    {'nome': 'Aline', 'sobrenome': 'Souza'}
]


def exibir(lista):
    for item in lista:
        print(item)
    print()


l1 = sorted(lista, key=lambda item: item['nome'])
l2 = sorted(lista, key=lambda item: item['sobrenome'])

exibir(l1)
exibir(l2)
