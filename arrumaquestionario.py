import re

# Lê o arquivo de perguntas e respostas
with open('qv.txt', 'r') as f:
    texto = f.read()

# Separa as perguntas e respostas em uma lista
perguntas_respostas = re.split('\n\n', texto)

# Cria um dicionário para armazenar as respostas para cada pergunta
respostas_por_pergunta = {}

# Loop pelas perguntas e respostas
for i in range(0, len(perguntas_respostas), 2):
    pergunta = perguntas_respostas[i].strip()
    resposta = perguntas_respostas[i+1].strip()
    respostas_por_pergunta[pergunta] = resposta

# Imprime o dicionário com as respostas para cada pergunta
print(respostas_por_pergunta)
