import pygame
import sys
from snake import Snake, Goal
from time import sleep
from random import randint


def init_settings(screenWidth=900, screenLength=600):
    # set the size of screen
    screen = pygame.display.set_mode((screenWidth,screenLength))
    # set the title of the screen
    pygame.display.set_caption("snake game")
    return screen


def catch_exit(event):
    if event.type == pygame.QUIT:
        pygame.quit()
        sys.exit()


def update_snake_direction(event, snake):
    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_LEFT:
            snake.xspeed = -snake.size
            snake.yspeed = 0
            # print('left')
        if event.key == pygame.K_RIGHT:
            snake.xspeed = snake.size
            snake.yspeed = 0
            # print('right')
        if event.key == pygame.K_UP:
            snake.xspeed = 0
            snake.yspeed = -snake.size
            # print('up')
        if event.key == pygame.K_DOWN:
            snake.xspeed = 0
            snake.yspeed = snake.size
            # print('down')
    return snake


def is_dead(screen, snake):
    screenWidth = screen.get_width()
    screenHeight = screen.get_height()
    con1 = snake.head[0] < 0
    con2 = snake.head[1] < 0
    con3 = snake.head[0] + snake.size > screenWidth
    con4 = snake.head[1] + snake.size > screenHeight
    con5 = snake.head in snake.tails
    return con1 or con2 or con3 or con4 or con5


def game_over(screen, snake):
    if is_dead(screen, snake):
       print('score: ', snake.length)
       snake = Snake(20, screen)
    return snake


def main():
    screenWidth, screenLength = 600, 400
    screen = init_settings(screenWidth, screenLength)
    snake = Snake(20, screen)
    goal = Goal(20, screen)
    while True:
        for event in pygame.event.get():
            catch_exit(event)
            # update snake location
            snake = update_snake_direction(event, snake)
        screen.fill((255, 255, 255))
        # update snake location
        flag = snake.update(goal.x, goal.y, screen)
        # update goal location
        if flag:
            del goal
            # create a new goal
            goal = Goal(20, screen)
        # show goal location
        goal.show(screen)
        pygame.display.flip()
        sleep(0.2)
        # detect game state
        snake = game_over(screen, snake)


if __name__ == '__main__':
    main()