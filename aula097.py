# Entendo seus próprios módulos Python
# O primeiro módulo executado chama-se __main__
# Você pode importar outro módulo inteiro ou parte do módulo
# O Python conhece a pasta onde o __main__ está e as pastas
# abaixo dele.
# Ele não reconhece pastas e módulos acima do __main__ por
# padrão
# O Python conhece todos os módulo e pacotes presentes
# nos caminhos de sys.path

import aula097_m
from aula097_m import variavel_modulo, soma


print('Esse módulo se chama', __name__)
print(aula097_m.variavel_modulo)
print(variavel_modulo)
print(soma(2, 3))
print(aula097_m.soma(2, 3))
