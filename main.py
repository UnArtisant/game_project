"""
Projet jeu Python
Raphael BARRIET
Pierre-Marie HERRBURGER--PIETRI
Marco-Naji SERHAL
Ahyl PRADHAN
Zyad ZEKRI
"""
import pygame
from pygame.locals import *
import math
from src.Service.GameService import Game
from src.Service.MenuService import Menu
from src.Service.Perso1.PlayerService import Perso1
from src.Service.Perso2.PlayerService import Perso2
from src.Service.Perso3.PlayerService import Perso3
from src.Service.Perso4.PlayerService import Perso4
import time

#Initier pygame et le son (mixer)
pygame.init()
pygame.mixer.init()
#initier la clock et determiner le FPS
clock = pygame.time.Clock()
FPS = 60
#Initier une instance de la classe Menu : menu
menu = Menu()

#Choisir la musique
music = pygame.mixer.Sound("src/sounds/dripfighters.wav")
music.play(-1)

#Initiation des touches
#J1
jump_1 = pygame.K_z
forward_1 = pygame.K_d
backward_1 = pygame.K_q
spe_1 = pygame.K_x
punch_1 = pygame.K_c
block_1 = pygame.K_v
#J2
jump_2 = pygame.K_UP
forward_2 = pygame.K_RIGHT
backward_2 = pygame.K_LEFT
spe_2 = 1073741913
punch_2 = 1073741914
block_2 = 1073741915



#generer la fenetre du jeu
pygame.display.set_caption("DripFighters") #Titre
screen = pygame.display.set_mode((1080,720)) #Taille de la fenetre

background_1 = pygame.image.load('src/ressources_graphiques/bg.jpg')
background_1 = pygame.transform.scale(background_1,(1080,720))

background_menu = pygame.image.load('src/ressources_graphiques/menu_background.jpg')
background_menu = pygame.transform.scale(background_menu,(1080,720))
#Creation du bouton
play_button = pygame.image.load("src/ressources_graphiques/button.png")
play_button = pygame.transform.scale(play_button,(300,150))
play_button_rect = play_button.get_rect()
play_button_rect.x = screen.get_width()//2 - play_button_rect.width//2
play_button_rect.y = screen.get_height()//2 - play_button_rect.height//2

#Bouttons selection de persos :

reset_button = pygame.image.load("src/ressources_graphiques/Reset_button.png")
reset_button = pygame.transform.scale(reset_button,(125,50))






#Bouton Retourner au menu
reset_button_rect = reset_button.get_rect()

game = Game(screen)

#Boucle de jeu
running = True
while running:
    game.screen = screen
    #Application du fond d'écran
    if game.is_playing:
        screen.blit(game.background.bg,(0,0))
    else:
        screen.blit(background_menu,(0,0))

    chosing = False
    if game.is_playing:
        #Si en jeu : faire toutes les actions d'updates
        game.update(screen,forward_1,forward_2,backward_1,backward_2)
    else :
        #Si pas en jeu :
        if game.menu:
            #Si c'est le menu : afficher les boutons
            menu.printButtons(screen,game)
        else :
            #Sinon : Afficher l'écran d'accueil
            screen.blit(play_button, play_button_rect)
            if not game.pause:
                #Si pas en pause : Afficher le bouton de settings
                screen.blit(menu.parametre_button,menu.parametre_button_rect)
        if game.pause :
            #Si c'est en pause : Afficher le bouton de retour au menu
            screen.blit(reset_button, reset_button_rect)
            game.text = game.font.render("",1,(255, 0, 0))

    #Afficher le résultat : Joueur gagnant
    text_rect = game.text.get_rect()
    screen.blit(game.text,(540 - text_rect.width//2,250))

    #mise a jour de l'écran
    pygame.display.flip()

    #Fermeture du programme quand on clique sur la croix
    for event in pygame.event.get():
        #Si clic sur la croix : fermer le jeu
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
        #Si le type d'événement est une touche préssée :
        elif event.type == pygame.KEYDOWN:
            #Indiquer que la touche est pressée
            game.pressed[event.key] = True
            #Si l'utilisateur est entrain de choisir ses touches, modifier la touche à modifier :
            chosing = menu.choice_attack_1 or menu.choice_block_1 or menu.choice_punch_1 or menu.choice_attack_2 or menu.choice_block_2 or menu.choice_punch_2
            if chosing:
                if menu.choice_attack_1:
                    spe_1 = event.key
                    menu.choice_attack_1 = False
                elif menu.choice_attack_2:
                    spe_2 = event.key
                    menu.choice_attack_2 = False
                elif menu.choice_punch_1:
                    punch_1 = event.key
                    menu.choice_punch_1 = False
                elif menu.choice_punch_2:
                    punch_2 = event.key
                    menu.choice_punch_2 = False
                elif menu.choice_block_1:
                    block_1 = event.key
                    menu.choice_block_1 = False
                elif menu.choice_block_2:
                    block_2 = event.key
                    menu.choice_block_2 = False

            else:
                #Afficher le menu si Echap
                if event.key == 27:
                    if not game.is_playing and not game.pause:
                        if game.menu:
                            game.menu = False
                        else :
                            game.menu = True
                    else :
                        game.is_playing = False
                        game.pause = True
                        game.timepassed = time.time() - game.begginTime
                #Lancement de l'action quand la touche est pressée Si ce n'est pas un bot
                if not game.player1.bot:
                    if event.key == spe_1 :
                        game.player1.attack_spe()
                    elif event.key == punch_1:
                        game.player1.launch_punch()
                    elif event.key == block_1:
                        game.player1.parade_on()
                    elif event.key == jump_1:
                        game.player1.press_jump()

                if not game.player2.bot:
                    if event.key == spe_2:
                        game.player2.attack_spe()
                    if event.key == punch_2:
                        game.player2.launch_punch()
                    if event.key == block_2:
                        game.player2.parade_on()
                    if event.key == jump_2:
                        game.player2.press_jump()

        elif event.type == pygame.KEYUP:
            #Indiquer que la touche est relachée
            game.pressed[event.key] = False
            if not game.player1.bot:
                #Desactivation de la parade
                if event.key == block_1:
                    game.player1.parade_off()
            if not game.player2.bot:
                if event.key == block_2:
                    game.player2.parade_off()

        # Check si c'est un click sur un bouton de menu, si oui, appliquer l'action correspondant au bouton choisi
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if not game.is_playing and not game.pause and menu.parametre_button_rect.collidepoint(event.pos):
                if game.menu:
                    game.menu = False
                else:
                    game.menu = True
            if not game.is_playing:
                if not game.menu:
                    if play_button_rect.collidepoint(event.pos):
                        game.is_playing = True
                        game.text = game.font.render("", 1, (255, 0, 0))
                        if not game.pause :
                            game.begginTime = time.time()
                            game.chrono = game.maxTime
                        else :
                            game.begginTime = time.time() - game.timepassed
                if not game.pause:
                    if game.menu:
                        if menu.b1_1_rect.collidepoint(event.pos):
                            game.player1 = Perso1(game,0,game.is_bot_1)
                            game.player1.finish_init(game.player2)
                            game.player2.finish_init(game.player1)
                        elif menu.b2_1_rect.collidepoint(event.pos):
                            game.player1 = Perso2(game,0,game.is_bot_1)
                            game.player1.finish_init(game.player2)
                            game.player2.finish_init(game.player1)
                        elif menu.b3_1_rect.collidepoint(event.pos):
                            game.player1 = Perso3(game,0,game.is_bot_1)
                            game.player1.finish_init(game.player2)
                            game.player2.finish_init(game.player1)
                        elif menu.b4_1_rect.collidepoint(event.pos):
                            game.player1 = Perso4(game,0,game.is_bot_1)
                            game.player1.finish_init(game.player2)
                            game.player2.finish_init(game.player1)
                        elif menu.b1_2_rect.collidepoint(event.pos):
                            game.player2 = Perso1(game,1,game.is_bot_2)
                            game.player1.finish_init(game.player2)
                            game.player2.finish_init(game.player1)
                        elif menu.b2_2_rect.collidepoint(event.pos):
                            game.player2 = Perso2(game,1,game.is_bot_2)
                            game.player1.finish_init(game.player2)
                            game.player2.finish_init(game.player1)
                        elif menu.b3_2_rect.collidepoint(event.pos):
                            game.player2 = Perso3(game,1,game.is_bot_2)
                            game.player1.finish_init(game.player2)
                            game.player2.finish_init(game.player1)
                        elif menu.b4_2_rect.collidepoint(event.pos):
                            game.player2 = Perso4(game,1,game.is_bot_2)
                            game.player1.finish_init(game.player2)
                            game.player2.finish_init(game.player1)
                        elif menu.b_choix_rect.collidepoint(event.pos):
                            game.is_bot_1 = True
                            game.player1.bot = True
                        elif menu.b_choix_2_rect.collidepoint(event.pos):
                            game.is_bot_2 = True
                            game.player2.bot = True
                        elif menu.j_choix_rect.collidepoint(event.pos):
                            game.is_bot_1 = False
                            game.player1.bot = False
                        elif menu.j_choix_2_rect.collidepoint(event.pos):
                            game.is_bot_2 = False
                            game.player2.bot = False

                        if menu.attack_button_1.collidepoint(event.pos):
                            if menu.choice_attack_1:
                                menu.choice_attack_1 = False
                            else :
                                menu.choice_attack_1 = True

                        if menu.attack_button_2.collidepoint(event.pos):
                            if menu.choice_attack_2:
                                menu.choice_attack_2 = False
                            else :
                                menu.choice_attack_2 = True

                        if menu.punch_button_1.collidepoint(event.pos):
                            if menu.choice_punch_1:
                                menu.choice_punch_1 = False
                            else:
                                menu.choice_punch_1 = True

                        if menu.punch_button_2.collidepoint(event.pos):
                            if menu.choice_punch_2:
                                menu.choice_punch_2 = False
                            else:
                                menu.choice_punch_2 = True

                        if menu.block_button_1.collidepoint(event.pos):
                            if menu.choice_block_1:
                                menu.choice_block_1 = False
                            else:
                                menu.choice_block_1 = True

                        if menu.block_button_2.collidepoint(event.pos):
                            if menu.choice_block_2:
                                menu.choice_block_2 = False
                            else:
                                menu.choice_block_2 = True
                else:
                    if reset_button_rect.collidepoint(event.pos):
                        game.reset()

    #Appliquer la clock
    clock.tick(FPS)

#Quitter le jeu
pygame.quit()