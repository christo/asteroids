#!/usr/bin/env python3 

import sys
import pygame
import random

from Asteroid import Asteroid

BLACK = 0, 0, 0

WHITE = 255, 255, 255


def main():

    width = 800
    height = 600
    num_asteroids = 10

    pygame.init()
    screen = pygame.display.set_mode((width, height))
    pygame.display.set_caption("Asteroids")

    font = pygame.font.Font('Planetnv2.ttf', 32)

    clock = pygame.time.Clock()

    # create some asteroids
    asteroids = []
    for i in range(num_asteroids):
        x = random.randint(0, width)
        y = random.randint(0, height)
        a = Asteroid(x, y)
        asteroids.append(a)

    running = True

    while running:
        clock.tick(30)

        # check for quit
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                # if the left button is pressed
                if event.button == 1:
                    for a in asteroids:
                        if a.inside(event.pos):
                            parts = a.explode()
                            if len(parts) > 0:
                                asteroids.extend(parts)
                            else:
                                asteroids.remove(a)

        # update asteroids
        for a in asteroids:
            a.move(width, height)

        # draw screen
        screen.fill(BLACK)

        for a in asteroids:
            a.draw(screen)

        text = font.render('Asteroids: %d' % (len(asteroids)), True, WHITE, BLACK)
        text_rect = text.get_rect()
        text_rect.x = 20
        text_rect.y = 20
        screen.blit(text, text_rect)

        pygame.display.flip()


if __name__ == '__main__':
    sys.exit(main())
