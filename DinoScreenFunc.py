import pygame, DinoGlobalVar


def GameOver() :

    pygame.mixer.music.stop()

    Over = DinoGlobalVar.OverFont.render('GAME OVER', True, (0, 0, 0))

    DinoGlobalVar.Screen.blit(Over, (100, DinoGlobalVar.Length / 2))

    pygame.time.wait(2000)