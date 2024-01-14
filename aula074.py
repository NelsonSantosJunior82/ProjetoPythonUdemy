# Closure e funções que retornam outras funções

def criar_saudadacao(saudacao, nome):
    def saudar():
        return f'{saudacao}, {nome}'
    return saudar


s1 = criar_saudadacao('Bom dia', ' Luiz')
s2 = criar_saudadacao('Boa noite', 'Luiz')


print(s1())
print(s2())
