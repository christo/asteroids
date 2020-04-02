import pygame
import random

WHITE = 255, 255, 255


class Asteroid:

    minimum_size = 20
    
    def __init__(self, x, y, size=200):
        self.x = x
        self.y = y
        self.size = size

        self.vx = random.random() * 10 - 5
        self.vy = random.random() * 10 - 5

    def draw(self, screen):
        pygame.draw.rect(screen, WHITE, (self.x, self.y, self.size, self.size), 5)

    def move(self, width, height):
        self.x += self.vx
        self.y += self.vy
        self.x %= width
        self.y %= height
        if abs(self.vx) > 2:
            self.vx *= 0.999
        if abs(self.vy) > 2:
            self.vy *= 0.999

    def explode(self):
        parts = []
        # split into 4 parts of half edge size each including the current part
        self.size /= 2
        if self.size > self.minimum_size:
            for p in range(3):
                parts.append(Asteroid(self.x, self.y, self.size))
        return parts

    def inside(self, pos):
        return pygame.Rect(self.x, self.y, self.size, self.size).collidepoint(pos[0], pos[1])
