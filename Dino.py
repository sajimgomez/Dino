import pygame, sys, random, time

from pygame import mixer

pygame.init()

Length = 600

Width = 800

Screen = pygame.display.set_mode((Width, Length))

pygame.display.set_caption('Dino')

Icon = pygame.image.load('IconImage.png')

pygame.display.set_icon(Icon)

BackgroundImage = pygame.image.load('Background.png')

mixer.music.load('BackgroundSound.wav')

mixer.music.play(- 1)

CanJump = True


class Player(pygame.sprite.Sprite) :

    def __init__(self) :

        pygame.sprite.Sprite.__init__(self)

        self.image = pygame.image.load('dinosaur.png')

        self.rect = self.image.get_rect()

        self.rect.bottomleft = (0, 496)

        self.speed = [0, 0]


    def Update(self, event) :

        global CanJump

        if (event.key == pygame.K_SPACE or event.key == pygame.K_UP) and CanJump :

            self.speed = [0, - 120]

            self.rect.move_ip(self.speed)

            CanJump = False



class Obstacle(pygame.sprite.Sprite) :

    def __init__(self) :

        pygame.sprite.Sprite.__init__(self)

        self.image = pygame.image.load('Obstacle.png')

        self.rect = self.image.get_rect()

        self.rect.bottomright = (Width - 100, 492)

        self.speed = [- 3, 0]


    def Update(self) :

        self.rect.move_ip(self.speed)
        



TRex = Player()

Obs = Obstacle()


while True :

    Screen.blit(BackgroundImage, (0, 0))

    if not CanJump :

        TRex.speed = [0, 1.5]

        TRex.rect.move_ip(TRex.speed)

    
    for event in pygame.event.get() :

        if event.type == pygame.QUIT :

            pygame.quit()

            sys.exit()

        if event.type == pygame.KEYDOWN :

            TRex.Update(event)


    if TRex.rect.bottomleft[1] > 496 :

        TRex.rect.bottomleft = (0, 496) 

        CanJump = True


    if Obs.rect.bottomleft[0] < 0 :

        Obs.rect.bottomleft = (Width, 492)


    Screen.blit(TRex.image, TRex.rect)

    Obs.Update()

    Screen.blit(Obs.image, Obs.rect)

    pygame.display.update()