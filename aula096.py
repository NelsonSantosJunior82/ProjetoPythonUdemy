# Módulos padrão do Python (import, from, as e *)
# https://docs.python.org/3/py-modindex.html
# inteiro - import nome_modulo
# Vantagens: você tem o namespace do módulo
# Desvantagens: Nomes grandes
# import sys
# print(sys.platform)

# partes - from nome_modulo import objeto1, objeto2
# Vantagens: nomes pequenos
# Desvantagens: Sem o namespace do módulo

# from sys import exit, platform
# print(platform)
# exit()

# alias 1 - import nome_módulo as apelido

# import sys as s

# sys = 'Alguma coisa'
# print(s.platform)
# print(sys)

# alias 2 - from nome_módulo import objeto as apelido

# from sys import exit as ex
# from sys import platform as pf

# print(pf)

# Vantagens: você pode reservar nomes para seu código
# Desvantagens: pode ficar fora do padrão da linguagem

# Má prática - from nome_módulo import *
# Vantagens: Importa tudo de um módulo
# Desvantagens: Importa tudo de um módulo
