with open('qv.txt', 'r') as f:
    blocos = f.read().split('\n\n')

perguntas = {}
for bloco in blocos:
    linhas = bloco.split('\n')
    pergunta = linhas[0]
    respostas = linhas[1:-1]
    perguntas[pergunta] = respostas

print(perguntas)
