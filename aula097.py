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

print('Esse módulo se chama', __name__)
