import pygame, DinoGlobalVar


class Obstacle(pygame.sprite.Sprite) :

    def __init__(self) :

        pygame.sprite.Sprite.__init__(self)

        self.image = pygame.image.load('Obstacle.png')

        self.rect = self.image.get_rect()

        self.rect.bottomright = (DinoGlobalVar.Width - 100, 492)

        self.speed = [- 3, 0]


    def Update(self) :

        self.rect.move_ip(self.speed)