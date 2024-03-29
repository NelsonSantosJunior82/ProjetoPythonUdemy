"""
Dicionários em Python (tipo dict)
Dicionários são estrutura de dados do tipo
par de chave "{}" e valor.
Chaves podem ser consideradas como o "indíce"
que vimos na lista e podem ser de tipo imutáveis
como: str, int, float, bool, tuple, etc.
O valor pode ser qualquer tipo, incluindo outro
dicionário.
Usamos chaves "{}" ou a classe dict para criar
dicionários.
Imutáveis: str, int, float, bool, tuple
Mutáveis: dict, list.

"""
"""
pessoa = {
    'nome': 'Nelson',
    'sobrenome': 'Santos Júnior',
    'idade': 41,
    'altura': 1.67,
    'endereço': [
        {'Rua: Joaquim Teodoro Tavares, 46'},
        {'Rua: Magalhães Lemos, 174'}]
}

pessoa = dict(
    nome='Nelson',
    sobrenome='Santos Júnior',
    idade=41,
    altura=1.67,
    endereco=['Rua Joaquim Teodoro Tavares, 46',
              'Rua Magalhães Lemos, 174']
)
for chave in pessoa:
    print(chave, pessoa[chave])


Métodos úteis dos dicionários em Python
Len - Quantas vezes
Keys - Iterável com as chaves
Values - Iterável com valores
Items - Iterável com chaves e valores
Setdefault - Adiciona valor se a chave não existe
Copy - Retorna uma cópia rasa (Shallow copy)
Get - Obtém a chave
Pop - Apaga um item com a chave especifica (del)
Popitem - Apaga um item adicionado
Update - Atualiza um dicionário com outro
"""
pessoa = {
    'nome': 'Nelson',
    'sobrenome': 'Santos Júnior',
    'idade': '41',
}

'''nome = pessoa.pop('nome')
print(nome)
print(pessoa)'''

'''last_key = pessoa.popitem()
print(last_key)
print(pessoa)'''

'''pessoa.update({
    'nome': 'Nelso José'
}
print(pessoa)'''

# pessoa.setdefault('idade')
# print(list(pessoa.keys()))
# print(list(pessoa.values()))
# print(list(pessoa.items()))
# print(pessoa['idade'])
# print(pessoa['nome'])
# print(pessoa.get('nome'))
