# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame
from constants import PLAYER_RADIUS, SCREEN_WIDTH, SCREEN_HEIGHT
from player import Player
from circleshape import CircleShape
clock = pygame.time.Clock
dt = 0
# Create player in the middle of the screen
player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)


def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill(0000)
        player.draw(screen)
        pygame.display.flip()



    
    clock_time = clock.tick(60)
    dt = clock_time / 1000



if __name__ == "__main__":
    main()