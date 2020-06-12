import pygame, sys, random, time, DinoPlayer, DinoGlobalVar, DinoObs, DinoScreenFunc

from pygame import mixer

pygame.init()

pygame.display.set_caption('Dino')

Icon = pygame.image.load('IconImage.png')

pygame.display.set_icon(Icon)

BackgroundImage = pygame.image.load('Background.png')

mixer.music.load('BackgroundSound.wav')

mixer.music.play(- 1)

TRex = DinoPlayer.Player()

Obs = DinoObs.Obstacle()

while True :

    DinoGlobalVar.Screen.blit(BackgroundImage, (0, 0))

    if not DinoGlobalVar.CanJump :

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

        DinoGlobalVar.CanJump = True


    if Obs.rect.bottomleft[0] < 0 :

        Obs.rect.bottomleft = (DinoGlobalVar.Width, 492)


    DinoGlobalVar.Screen.blit(TRex.image, TRex.rect)

    Obs.Update()

    DinoGlobalVar.Screen.blit(Obs.image, Obs.rect)

    if TRex.rect.colliderect(Obs) :

        TRex.speed = [0, 0]

        TRex.rect.move_ip(TRex.speed)

        Obs.speed = [0, 0]

        Obs.rect.move_ip(Obs.speed)

        DinoScreenFunc.GameOver()

        break

    pygame.display.update()