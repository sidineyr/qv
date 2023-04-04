import PySimpleGUI as sg

# Definindo a lista de perguntas e respostas
perguntas_respostas = [
    {'pergunta': 'Qual é a capital do Brasil?', 'respostas': ['São Paulo', 'Rio de Janeiro', 'Brasília', 'Belo Horizonte', 'Salvador']},
    {'pergunta': 'Quantos dias tem uma semana?', 'respostas': ['3', '6', '7']},
    {'pergunta': 'Qual é o maior planeta do sistema solar?', 'respostas': ['Vênus', 'Júpiter', 'Marte', 'Saturno', 'Urano']}
]

# Criando a janela do formulário
layout = []
for pergunta in perguntas_respostas:
    layout.append([sg.Text(pergunta['pergunta'])])
    respostas = []
    for resposta in pergunta['respostas']:
        respostas.append(sg.Checkbox(resposta))
    layout.append(respostas)

layout.append([sg.Submit('Enviar')])

window = sg.Window('Formulário de perguntas e respostas', layout)

# Loop para ler as respostas do usuário
while True:
    event, values = window.read()
    if event == sg.WINDOW_CLOSED:
        break
    if event == 'Enviar':
        for idx, pergunta in enumerate(perguntas_respostas):
            print(pergunta['pergunta'])
            for resposta in pergunta['respostas']:
                if values[idx][resposta]:
                    print(f' - {resposta}')
        break

window.close()
