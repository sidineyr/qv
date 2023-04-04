import csv

with open('qv.txt', 'r') as file:
    data = file.readlines()

questions = []
answers = []

for line in data:
    if line.startswith("   "):  # Nova pergunta
        questions.append(line.strip())
        answers.append([])
    elif line.startswith(("a)", "b)", "c)", "d)", "e)")):  # Resposta
        answers[-1].append(line.strip())

with open('textodemacaco.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['pergunta', 'resposta_a', 'resposta_b', 'resposta_c', 'resposta_d', 'resposta_e'])
    for i in range(len(questions)):
        writer.writerow([questions[i]] + answers[i])
