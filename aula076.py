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
"""
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
