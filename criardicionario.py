# abrir o arquivo para leitura
with open('qv.txt', 'r') as f:
    # ler o conteúdo do arquivo
    conteudo = f.read()
    
# separar o conteúdo do arquivo em blocos
blocos = conteudo.strip().split('\n\n')

# criar um dicionário para armazenar as perguntas e respostas
perguntas_respostas = {}

# iterar sobre cada bloco
for bloco in blocos:
    # separar o bloco em linhas
    linhas = bloco.strip().split('\n')
    
    # obter a pergunta
    pergunta = linhas[0][2:].strip()
    
    # obter as respostas
    respostas = [linha.strip()[3:] for linha in linhas[1:]]
    
    # adicionar a pergunta e respostas ao dicionário
    perguntas_respostas[pergunta] = respostas
print(perguntas_respostas)
