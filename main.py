"""
Projet jeu Python
Raphael BARRIET
Pierre-Marie HERRBURGER--PIETRI
Marco ....
Ahyl ....
Zyad .....
"""
import pygame
pygame.init()

class Player1(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.health = 100
        self.fireBallDmg = 5
        self.fistDmg = 10
        self.paradeReduction = 0.8
        self.velocity = 5
        self.image = pygame.image.load("src/ressources_graphiques/player.png")
        self.rect = self.image.get_rect()
        self.rect.x = 500
        self.rect.y = 360


#generer la fenetre du jeu
pygame.display.set_caption("DripFighters")
screen = pygame.display.set_mode((1080,720))
background = pygame.image.load('src/ressources_graphiques/bg.jpg')

player1 = Player1()

running = True
while running:

    #Application du fond d'écran
    screen.blit(background,(0,0))

    screen.blit(player1.image, player1.rect)

    #mise a jour de l'écran
    pygame.display.flip()

    #Fermeture du programme quand on clique su la croix
    for  event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
