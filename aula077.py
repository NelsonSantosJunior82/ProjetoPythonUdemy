# Exercício de perguntas e respostas

perguntas = [
    {
        'Pergunta': 'Qual é o dia do meu aniversário?',
        'Opcões': ['10', '05', '28', '03'],
        'Resposta': '05',
    },
    {
        'Pergunta': 'Qual é o mês do meu aniversário?',
        'Opcões': ['12', '01', '10', '03'],
        'Resposta': '03',
    },
    {
        'Pergunta': 'Qual é o ano do meu aniversário?',
        'Opcões': ['1980', '1989', '2020', '1982'],
        'Resposta': '1982',
    },
    {
        'Pergunta': 'Quantos anos eu tenho?',
        'Opcões': ['41', '38', '52', '45'],
        'Resposta': '41',
    },
]

qtd_acertos = 0
for pergunta in perguntas:
    print('Pergunta', pergunta['Pergunta'])
    print()

    opcoes = pergunta['Opcões']
    for i, opcao in enumerate(opcoes):
        print(f'{i})', opcao)
    print()

    escolha = input('Escolha uma opção: ')

    acertou = False
    escolha_int = None
    qtd_opcoes = len(opcoes)
    
    if escolha.isdigit():
        escolha_int = int(escolha)

    if escolha_int is not None:
        if escolha_int >= 0 and escolha_int < qtd_opcoes:
            if opcoes[escolha_int] == pergunta['Resposta']:
                acertou = True
    print()
    if acertou:
        qtd_acertos += 1
        print('Acertou!!')
    else:
        print('Errou!!')
    
    print()

print('Você acertou', qtd_acertos) 
print('de', len(perguntas), 'perguntas.')
