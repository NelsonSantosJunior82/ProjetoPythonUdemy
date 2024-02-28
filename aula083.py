# Empacotamento e desempacotamento de dicionários

a, b = 1, 2
a, b = b, a
# print(a, b)

pessoa = {
    'nome': 'Aline',
    'sobrenome': 'Souza',
}

a, b = pessoa.values()
a, b = pessoa.items()

# desempacotamento interno
(a1, a2), (b1, b2) = pessoa.items()
# print(a, b)
# print(a1, a2)
# print(b1, b2)


dados_pessoa = {
    'Idade': 16,
    'Altura': 1.6,
}

pessoas_completa = {**pessoa, **dados_pessoa}

# print(pessoas_completa)

# args e kwargs
# args (já vimos)
# kwargs - keyword arguments (argumentos nomeados)


def mostrar_argumentos_nomeados(*args, **kwargs):
    for chave, valor in kwargs.items():
        print(chave, valor)


# mostrar_argumentos_nomeados(nome='Joana', qlq=123)
mostrar_argumentos_nomeados(**pessoas_completa)
