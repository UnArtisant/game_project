"""
Projet jeu Python
Raphael BARRIET
Pierre-Marie HERRBURGER--PIETRI
Marco ....
Ahyl ....
Zyad .....
"""
import pygame
from src.Service.GameService import Game
pygame.init()




#generer la fenetre du jeu
pygame.display.set_caption("DripFighters")
screen = pygame.display.set_mode((1080,720))
background = pygame.image.load('src/ressources_graphiques/bg.jpg')

game = Game()

running = True
while running:

    #Application du fond d'écran
    screen.blit(background,(0,0))

    screen.blit(game.player1.image, game.player1.rect)

    #mise a jour de l'écran
    pygame.display.flip()

    #Fermeture du programme quand on clique su la croix
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
