import pygame
import csv

# Definindo as cores
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# Definindo as dimensões da janela
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

# Definindo as perguntas e respostas
perguntas = {
    "Qual é a capital do Brasil?": ["Rio de Janeiro", "Brasília", "São Paulo", "Belo Horizonte"],
    "Qual é a cor do cavalo branco de Napoleão?": ["Preto", "Branco", "Marrom", "Cinza"],
    "Qual é a capital do Japão?": ["Tóquio", "Osaka", "Kyoto", "Hiroshima"]
}

# Lista para armazenar as respostas do usuário
respostas = []

# Inicializando o Pygame
pygame.init()

# Criando a janela
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Jogo de Perguntas e Respostas")

# Definindo a fonte
font = pygame.font.Font(None, 36)

# Loop principal
running = True
pergunta_index = 0
while running:
    # Tratando eventos
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                # Salvando a resposta do usuário
                opcao_selecionada = None
                for opcao in opcoes:
                    if opcao["caixa"].collidepoint(pygame.mouse.get_pos()):
                        opcao_selecionada = opcao["texto"]
                        break
                respostas.append([pergunta, opcao_selecionada])
                pergunta_index += 1

    # Exibindo a pergunta e as opções
    pergunta, opcoes = list(perguntas.items())[pergunta_index]
    screen.fill(WHITE)
    pergunta_render = font.render(pergunta, True, BLACK)
    screen.blit(pergunta_render, (SCREEN_WIDTH/2 - pergunta_render.get_width()/2, 100))

    y = 200
    for i, opcao in enumerate(opcoes):
        opcao_render = font.render(opcao, True, BLACK)
        caixa = pygame.draw.rect(screen, BLACK, (SCREEN_WIDTH/2 - opcao_render.get_width()/2 - 20, y, 20, 20))
        opcao_render_rect = opcao_render.get_rect()
        opcao_render_rect.x = SCREEN_WIDTH/2 - opcao_render.get_width()/2
        opcao_render_rect.y = y
        screen.blit(opcao_render, opcao_render_rect)
        opcoes[i] = {"texto": opcao, "caixa": caixa}
        y += 40

    pygame.display.update()

# Salvando as respostas em um arquivo CSV
with open('respostas.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(["Pergunta", "Resposta"])
    for resposta in respostas:
        writer.writerow(resposta)

# Finalizando o Pygame
pygame.quit()
