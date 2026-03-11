import pygame
from circleshape import CircleShape
from constants import PLAYER_SHOOT_SPEED
class Shot(CircleShape):
    def __init__(self,x,y,rotation):
        super().__init__(x,y,2)
        self.velocity = pygame.Vector2(0, 1).rotate(rotation) * PLAYER_SHOOT_SPEED
    def draw(self,screen):
        pygame.draw.circle(screen,"white",self.position,2)
    def update(self,dt):
        self.position += self.velocity * dt
