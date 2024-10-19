import pygame
from random import randrange

RES = 500  # Розмір екрану 500x500
SIZE = 25  # Розмір сегмента змії

# Ініціалізація Pygame
pygame.init()
sc = pygame.display.set_mode([RES, RES])
clock = pygame.time.Clock()
font_score = pygame.font.SysFont('Arial', 26)
font_end = pygame.font.SysFont('Arial', 26)

# Завантаження фонової картинки
background_image = pygame.image.load('bg.png')  # Змінити на ім'я вашого файлу

x, y = randrange(0, RES, SIZE), randrange(0, RES, SIZE)
apple = randrange(0, RES, SIZE), randrange(0, RES, SIZE)
dirs = {'W': True, 'S': True, 'A': True, 'D': True}
length = 1
snake = [(x, y)]
dx, dy = 0, 0
score = 0
fps = 5

while True:
    # Відображення фону
    sc.blit(background_image, (0, 0))

    # Малюємо змію
    for i, j in snake:
        pygame.draw.rect(sc, pygame.Color('green'), (i, j, SIZE - 2, SIZE - 2))
    
    # Малюємо яблуко
    pygame.draw.rect(sc, pygame.Color('red'), (*apple, SIZE, SIZE)) 
    
    # Відображаємо рахунок
    render_score = font_score.render(f'SCORE: {score}', True, pygame.Color('orange'))
    sc.blit(render_score, (5, 5))

    # Оновлюємо позицію змії
    x += dx * SIZE
    y += dy * SIZE

    # Перевірка на межі екрану
    if x < 0:
        x = RES - SIZE
    elif x >= RES:
        x = 0
    if y < 0:
        y = RES - SIZE
    elif y >= RES:
        y = 0

    snake.append((x, y))
    snake = snake[-length:]

    # Перевіряємо, чи з'їли яблуко
    if snake[-1] == apple:
        apple = randrange(0, RES, SIZE), randrange(0, RES, SIZE)
        length += 1
        score += 1
        fps += 1

    # Перевірка на колізії з самим собою
    if len(snake) != len(set(snake)):
        while True:
            sc.fill(pygame.Color('black'))  # Очищаємо екран
            render_end = font_end.render('GAME OVER', True, pygame.Color('orange'))
            sc.blit(render_end, (RES // 2 - 100, RES // 3))  # Виправлено центр
            pygame.display.flip()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()

    pygame.display.flip()
    clock.tick(fps)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
    
    key = pygame.key.get_pressed()
    if key[pygame.K_w] and dirs['W']:
        dx, dy = 0, -1
        dirs = {'W': True, 'S': False, 'A': True, 'D': True}
    if key[pygame.K_s] and dirs['S']:
        dx, dy = 0, 1
        dirs = {'W': False, 'S': True, 'A': True, 'D': True}
    if key[pygame.K_a] and dirs['A']:
        dx, dy = -1, 0
        dirs = {'W': True, 'S': True, 'A': True, 'D': False}
    if key[pygame.K_d] and dirs['D']:
        dx, dy = 1, 0
        dirs = {'W': True, 'S': True, 'A': False, 'D': True}
