import pygame, DinoGlobalVar


class Player(pygame.sprite.Sprite) :

    def __init__(self) :

        pygame.sprite.Sprite.__init__(self)

        self.image = pygame.image.load('dinosaur.png')

        self.rect = self.image.get_rect()

        self.rect.bottomleft = (0, 496)

        self.speed = [0, 0]


    def Update(self, event) :

        if (event.key == pygame.K_SPACE or event.key == pygame.K_UP) and DinoGlobalVar.CanJump :

            self.speed = [0, - 120]

            self.rect.move_ip(self.speed)

            DinoGlobalVar.CanJump = False