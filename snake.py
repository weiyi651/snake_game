import pygame
from random import randint


class Snake():
    """
    class for snake
    """
    def __init__(self, size, screen):
        self.size = size
        self.head = [self.size * randint(0, screen.get_width()/self.size -1),
                     self.size * randint(0, screen.get_height()/self.size -1)]
        self.xspeed = self.size
        self.yspeed = 0
        self.color = (0,0,0)
        self.tails = []
        self.length = 1
        self.last_frame_end = None

    def move_head(self):
        self.head[0] += self.xspeed
        self.head[1] += self.yspeed

    def move_body(self):
        for i in reversed(range(1, len(self.tails))):
            self.tails[i] = self.tails[i-1].copy()
        if self.tails:
            self.tails[0] = self.head.copy()

    def increase_length(self, goalX, goalY):
        self.length += 1
        self.tails.append(self.last_frame_end.copy())

    def eaten(self, goalX, goalY):
        if self.head[0] == goalX and self.head[1] == goalY:
            return True
        else:
            return False

    def update(self, goalX, goalY, screen):
        self.move_body()
        self.move_head()
        flag = self.eaten(goalX, goalY)
        if flag:
            self.increase_length(goalX, goalY)
        try:
            self.last_frame_end = self.tails[-1].copy()
        except IndexError:
            self.last_frame_end = self.head.copy()
        self.show(screen)
        return flag

    def show(self, screen):
        # draw head
        for x in range(self.head[0], self.head[0] + self.size):
            for y in range(self.head[1], self.head[1] + self.size):
                screen.set_at((x, y), self.color)
        # draw tails
        for t in self.tails:
            for x in range(t[0], t[0] + self.size):
                for y in range(t[1], t[1] + self.size):
                    screen.set_at((x, y), self.color)


class Goal():
    """
    class for goal
    """
    def __init__(self, size, screen):
        self.size = size
        self.x = self.size * randint(0, screen.get_width()/self.size - 1)
        self.y = self.size * randint(0, screen.get_height()/self.size - 1)
        self.color = (255,0,0)

    def show(self, screen):
        for x in range(self.x, self.x + self.size):
            for y in range(self.y, self.y + self.size):
                screen.set_at((x, y), self.color)
