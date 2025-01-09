import pygame
from circleshape import *
from constants import *


class Shot(CircleShape):
    def __init__(self, position, velocity):
        super().__init__(position.x, position.y, SHOT_RADIUS)
        self.velocity = velocity
        self.position = position.copy()
        self.rect = pygame.Rect(0, 0, SHOT_RADIUS * 2, SHOT_RADIUS * 2)
        self.rect.center = (position.x, position.y)
        
        
    def update(self, dt):
        self.position += self.velocity * dt
        # Update rect position
        self.rect.center = (self.position.x, self.position.y)
        

    def draw(self, surface):   
        pygame.draw.circle(surface, "white", self.rect.center, SHOT_RADIUS)