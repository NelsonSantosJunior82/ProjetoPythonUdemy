# Dictionary Comprehension e Set Comprehension

produto = {
    'nome': 'Caneta Azul',
    'preco': 2.5,
    'categoria': 'Escritório'
}

dic = {
    chave: valor.upper()
    if isinstance(valor, str) else valor
    for chave, valor
    in produto.items()
}


lista = [
    ('a', 'valor b'),
    ('b', 'valor c'),
    ('c', 'valor a'),
]

dc = {
    chave: valor
    for chave, valor in lista
}
print(dict(dic))
print(dict(lista))

# Set Comprehension

s1 = {i for i in range(10)}
print(s1)
