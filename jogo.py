import csv

perguntas = {
    '1. Qual é o seu peso atual?': ['Abaixo do peso ideal', 'Peso ideal', 'Sobrepeso', 'Obeso'],
    '2. Qual é a sua altura atual?': ['Menos de 1,60m', 'Entre 1,60m e 1,70m', 'Entre 1,70m e 1,80m', 'Mais de 1,80m']
}

respostas = {}

with open('respostas.csv', mode='w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['Pergunta', 'Opção escolhida', 'Resposta'])

    for pergunta, opcoes in perguntas.items():
        print(pergunta)
        for i, opcao in enumerate(opcoes):
            print(f'{chr(97 + i)}. {opcao}')
        escolha = input('Escolha uma opção (a, b, c ou d): ')
        resposta = input('Digite sua resposta: ')
        respostas[pergunta] = {'opcao': escolha, 'resposta': resposta}
        writer.writerow([pergunta, escolha, resposta])


