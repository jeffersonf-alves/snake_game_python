from os import close
import pygame
from pygame.locals import *
import random

def on_grid_random():
    x = random.randint(0, 490)
    y = random.randint(0, 490)
    return (x//10 * 10, y//10 * 10)

def collision(c1, c2):
    return (c1[0] == c2[0]) and (c1[1] == c2[1])

UP = 0
RIGHT = 1
DOWN = 2
LEFT = 3

pygame.init()
screen = pygame.display.set_mode((500, 500))
pygame.display.set_caption('Snake')
screen.fill((255, 255, 255))



snake = [(200, 200), (210, 200), (220, 200)]
snake_skin = pygame.Surface((10,10))
my_direction = LEFT

apple_pos = on_grid_random()
apple = pygame.Surface((10, 10))
apple.fill((255, 0, 0))

clock = pygame.time.Clock()

while True:
    clock.tick(20)
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
        if event.type == KEYDOWN:
            if event.key == K_UP:
                my_direction = UP
            if event.key == K_DOWN:
                my_direction = DOWN
            if event.key == K_LEFT:
                my_direction = LEFT
            if event.key == K_RIGHT:
                my_direction = RIGHT
    if collision(snake[0], apple_pos):
        apple_pos = on_grid_random()
        snake.append((0, 0))

    for i in range(len(snake) -1, 0, -1):
        snake[i] = (snake[i-1][0], snake[i-1][1])

    if my_direction == UP:
        snake[0] = (snake[0][0], snake[0][1] - 10)
        if snake[0][1] == -10:
            my_direction = DOWN
    if my_direction == DOWN:
        snake[0] = (snake[0][0], snake[0][1] + 10)
        if snake[0][1] == 490:
            my_direction = UP
    if my_direction == RIGHT:
        snake[0] = (snake[0][0] + 10, snake[0][1])
        if snake[0][0] == 500:
            my_direction = LEFT
    if my_direction == LEFT:
        snake[0] = (snake[0][0] - 10, snake[0][1])
        if snake[0][0] == -10:
            my_direction = RIGHT

    screen.fill((255, 255, 255))
    screen.blit(apple, apple_pos)
    for pos in snake:
        screen.blit(snake_skin, pos)

    
    pygame.display.update()