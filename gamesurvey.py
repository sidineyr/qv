from tkinter import *
from survey import Survey

# Criando as perguntas e respostas
questions = {
    '1. Qual é o seu peso atual?': ['Abaixo do peso ideal', 'Peso ideal', 'Sobrepeso', 'Obeso'],
    '2. Qual é a sua altura atual?': ['Menos de 1,60m', 'Entre 1,60m e 1,70m', 'Entre 1,70m e 1,80m', 'Mais de 1,80m'],
    '3. Você já teve alguma doença crônica, como diabetes ou hipertensão?': ['Sim', 'Não'],
}
survey = Survey(questions)

# Função para apresentar a pergunta e as respostas
def show_question():
    global question_label, button1, button2, button3, button4
    question, options = survey.next_question()
    question_label.configure(text=question)
    button1.configure(text=options[0], command=lambda: choose_option(options[0]))
    button2.configure(text=options[1], command=lambda: choose_option(options[1]))
    button3.configure(text=options[2], command=lambda: choose_option(options[2]))
    button4.configure(text=options[3], command=lambda: choose_option(options[3]))

# Função para escolher a opção
def choose_option(option):
    global choices
    choices.append(option)
    if not survey.is_last_question():
        show_question()
    else:
        save_choices()
        window.destroy()

# Função para salvar as escolhas
def save_choices():
    with open('choices.txt', 'w') as f:
        for i, choice in enumerate(choices):
            f.write(f'Question {i+1}: {choice}\n')

# Criando a janela principal
window = Tk()
window.title('Game Survey')

# Criando os widgets da janela
question_label = Label(window, text='')
question_label.pack()
button1 = Button(window, text='', width=30)
button1.pack()
button2 = Button(window, text='', width=30)
button2.pack()
button3 = Button(window, text='', width=30)
button3.pack()
button4 = Button(window, text='', width=30)
button4.pack()

# Iniciando o jogo
choices = []
show_question()
window.mainloop()
