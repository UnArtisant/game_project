"""
Projet jeu Python
Raphael BARRIET
Pierre-Marie HERRBURGER--PIETRI
Marco ....
Ahyl ....
Zyad .....
"""
import pygame
import math
from src.Service.GameService import Game
from src.Service.Perso1.PlayerService import Perso1
from src.Service.Perso2.PlayerService import Perso2
from src.Service.Perso3.PlayerService import Perso3
from src.Service.Perso4.PlayerService import Perso4
import time
pygame.init()
pygame.mixer.init()

clock = pygame.time.Clock()
FPS = 60

"""pygame.mixer.music.load("src/sounds/music.mp3")
pygame.mixer.music.play(-1)"""

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

#Afficher le fond d'ecran
background = pygame.image.load('src/ressources_graphiques/bg.jpg')
background = pygame.transform.scale(background,(1080,720))

#Creation du bouton
play_button = pygame.image.load("src/ressources_graphiques/button.png")
play_button = pygame.transform.scale(play_button,(400,150))
play_button_rect = play_button.get_rect()
play_button_rect.x = screen.get_width()//3.33
play_button_rect.y = screen.get_height()//2 - play_button_rect.height//2

#Bouttons selection de persos :
#Images de numeros de persos :
perso_1 = pygame.image.load("src/ressources_graphiques/1_boutton.png")
perso_1 = pygame.transform.scale(perso_1,(100,100))
perso_2 = pygame.image.load("src/ressources_graphiques/2_boutton.png")
perso_2 = pygame.transform.scale(perso_2,(100,100))
perso_1_pressed = pygame.image.load("src/ressources_graphiques/1_boutton_pressed.png")
perso_1_pressed = pygame.transform.scale(perso_1_pressed,(100,100))
perso_2_pressed = pygame.image.load("src/ressources_graphiques/2_boutton_pressed.png")
perso_2_pressed = pygame.transform.scale(perso_2_pressed,(100,100))
perso_3 = pygame.image.load("src/ressources_graphiques/3_boutton.png")
perso_3 = pygame.transform.scale(perso_3,(100,100))
perso_4 = pygame.image.load("src/ressources_graphiques/4_boutton.png")
perso_4 = pygame.transform.scale(perso_4,(100,100))
perso_3_pressed = pygame.image.load("src/ressources_graphiques/3_boutton_pressed.png")
perso_3_pressed = pygame.transform.scale(perso_3_pressed,(100,100))
perso_4_pressed = pygame.image.load("src/ressources_graphiques/4_boutton_pressed.png")
perso_4_pressed = pygame.transform.scale(perso_4_pressed,(100,100))

reset_button = pygame.image.load("src/ressources_graphiques/Reset_button.png")
reset_button = pygame.transform.scale(reset_button,(125,50))
#Boutons J1 :
j1_image = pygame.image.load("src/ressources_graphiques/Joueur1_boutton.png")
j1_image = pygame.transform.scale(j1_image,(250,100))
j1_image_rect = j1_image.get_rect()
j1_image_rect.x = 145
j1_image_rect.y = 400

j_choix = pygame.image.load("src/ressources_graphiques/joueur.png")
j_choix_pressed = pygame.image.load("src/ressources_graphiques/joueur_pressed.png")
j_choix = pygame.transform.scale(j_choix,(120,100))
j_choix_pressed = pygame.transform.scale(j_choix_pressed,(120,100))
j_choix_rect = j_choix.get_rect()
j_choix_rect.x = j1_image_rect.x
j_choix_rect.y = j1_image_rect.y -10 - j1_image_rect.height
b_choix = pygame.image.load("src/ressources_graphiques/bot.png")
b_choix_pressed = pygame.image.load("src/ressources_graphiques/bot_pressed.png")
b_choix = pygame.transform.scale(b_choix,(120,100))
b_choix_pressed = pygame.transform.scale(b_choix_pressed,(120,100))
b_choix_rect = b_choix.get_rect()
b_choix_rect.x = j_choix_rect.x +10 + j_choix_rect.width
b_choix_rect.y = j_choix_rect.y
#Boutons J1 choix perso
b1_1_rect = perso_1.get_rect()
b1_1_rect.x = 145
b1_1_rect.y = 505


b2_1_rect = perso_2.get_rect()
b2_1_rect.x = 145 + j1_image_rect.width - b2_1_rect.width
b2_1_rect.y = 505
b3_1_rect = perso_3.get_rect()
b3_1_rect.x = 145
b3_1_rect.y = 505 + b1_1_rect.height+10
b4_1_rect = perso_4.get_rect()
b4_1_rect.x = 145 + j1_image_rect.width - b2_1_rect.width
b4_1_rect.y = 505 + b1_1_rect.height+10


#Boutons J2:
j2_image = pygame.image.load("src/ressources_graphiques/Joueur2_boutton.png")
j2_image = pygame.transform.scale(j2_image,(250,100))
j2_image_rect = j2_image.get_rect()
j2_image_rect.x = 685 #math.ceil(screen.get_width()/4*3 - (j2_image_rect.width / 2))
j2_image_rect.y = 400

j_choix_2_rect = j_choix.get_rect()
j_choix_2_rect.x = j2_image_rect.x
j_choix_2_rect.y = j2_image_rect.y -10 - j1_image_rect.height
b_choix_2_rect = b_choix.get_rect()
b_choix_2_rect.x = j_choix_2_rect.x +10 + j_choix_rect.width
b_choix_2_rect.y = j_choix_2_rect.y
#Boutons J2 choix perso
b1_2_rect = perso_1.get_rect()
b1_2_rect.x = 685
b1_2_rect.y = 505

b2_2_rect = perso_2.get_rect()
b2_2_rect.x = 685 + j2_image_rect.width - b2_2_rect.width
b2_2_rect.y = 505

b3_2_rect = perso_3.get_rect()
b3_2_rect.x = 685
b3_2_rect.y = 505 + b1_1_rect.height+10
b4_2_rect = perso_4.get_rect()
b4_2_rect.x = 685 + j2_image_rect.width - b2_2_rect.width
b4_2_rect.y = 505 + b1_1_rect.height+10


#Bouton Retourner au menu
reset_button_rect = reset_button.get_rect()

game = Game(screen)

#Boucle de jeu
running = True
while running:
    game.screen = screen
    #Application du fond d'écran
    screen.blit(background,(0,0))

    if game.is_playing:
        game.update(screen,forward_1,forward_2,backward_1,backward_2)
    else :
        if game.menu:
            game.text = game.font.render("",1,(255, 0, 0))
            screen.blit(j1_image,j1_image_rect)
            screen.blit(j2_image,j2_image_rect)
            screen.blit(perso_1, b1_1_rect)
            screen.blit(perso_1, b1_2_rect)
            screen.blit(perso_2, b2_1_rect)
            screen.blit(perso_2, b2_2_rect)
            screen.blit(perso_3, b3_2_rect)
            screen.blit(perso_4, b4_2_rect)
            screen.blit(perso_3,b3_1_rect)
            screen.blit(perso_4,b4_1_rect)
            screen.blit(j_choix,j_choix_rect)
            screen.blit(b_choix,b_choix_rect)
            screen.blit(j_choix, j_choix_2_rect)
            screen.blit(b_choix, b_choix_2_rect)
            if game.player1.id == 0:
                screen.blit(perso_1_pressed,b1_1_rect)
            elif game.player1.id == 1:
                screen.blit(perso_2_pressed, b2_1_rect)
            elif game.player1.id == 2:
                screen.blit(perso_3_pressed, b3_1_rect)
            elif game.player1.id == 3:
                screen.blit(perso_4_pressed, b4_1_rect)
            if game.player2.id == 0:
                screen.blit(perso_1_pressed, b1_2_rect)
            elif game.player2.id == 1 :
                screen.blit(perso_2_pressed, b2_2_rect)
            elif game.player2.id == 2 :
                screen.blit(perso_3_pressed, b3_2_rect)
            elif game.player2.id == 3 :
                screen.blit(perso_4_pressed, b4_2_rect)
            if game.is_bot_1:
                screen.blit(b_choix_pressed,b_choix_rect)
            else:
                screen.blit(j_choix_pressed,j_choix_rect)
            if game.is_bot_2:
                screen.blit(b_choix_pressed,b_choix_2_rect)
            else:
                screen.blit(j_choix_pressed,j_choix_2_rect)
        else :
            screen.blit(play_button, play_button_rect)
        if game.pause :
            screen.blit(reset_button, reset_button_rect)
            game.text = game.font.render("",1,(255, 0, 0))
    text_rect = game.text.get_rect()
    screen.blit(game.text,(540 - text_rect.width//2,250))

    #mise a jour de l'écran
    pygame.display.flip()

    #Fermeture du programme quand on clique sur la croix
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
        elif event.type == pygame.KEYDOWN:
            #Indiquer que la touche est pressée
            game.pressed[event.key] = True

            #Afficher le menu
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

            #Lancement de la boule de feu quand la touche est pressée
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


        elif event.type == pygame.MOUSEBUTTONDOWN:
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
                        if b1_1_rect.collidepoint(event.pos):
                            game.player1 = Perso1(game,0,game.is_bot_1)
                            game.player1.finish_init(game.player2)
                            game.player2.finish_init(game.player1)
                        elif b2_1_rect.collidepoint(event.pos):
                            game.player1 = Perso2(game,0,game.is_bot_1)
                            game.player1.finish_init(game.player2)
                            game.player2.finish_init(game.player1)
                        elif b3_1_rect.collidepoint(event.pos):
                            game.player1 = Perso3(game,0,game.is_bot_1)
                            game.player1.finish_init(game.player2)
                            game.player2.finish_init(game.player1)
                        elif b4_1_rect.collidepoint(event.pos):
                            game.player1 = Perso4(game,0,game.is_bot_1)
                            game.player1.finish_init(game.player2)
                            game.player2.finish_init(game.player1)
                        elif b1_2_rect.collidepoint(event.pos):
                            game.player2 = Perso1(game,1,game.is_bot_2)
                            game.player1.finish_init(game.player2)
                            game.player2.finish_init(game.player1)
                        elif b2_2_rect.collidepoint(event.pos):
                            game.player2 = Perso2(game,1,game.is_bot_2)
                            game.player1.finish_init(game.player2)
                            game.player2.finish_init(game.player1)
                        elif b3_2_rect.collidepoint(event.pos):
                            game.player2 = Perso3(game,1,game.is_bot_2)
                            game.player1.finish_init(game.player2)
                            game.player2.finish_init(game.player1)
                        elif b4_2_rect.collidepoint(event.pos):
                            game.player2 = Perso4(game,1,game.is_bot_2)
                            game.player1.finish_init(game.player2)
                            game.player2.finish_init(game.player1)
                        elif b_choix_rect.collidepoint(event.pos):
                            game.is_bot_1 = True
                            game.player1.bot = True
                        elif b_choix_2_rect.collidepoint(event.pos):
                            game.is_bot_2 = True
                            game.player2.bot = True
                        elif j_choix_rect.collidepoint(event.pos):
                            game.is_bot_1 = False
                            game.player1.bot = False
                        elif j_choix_2_rect.collidepoint(event.pos):
                            game.is_bot_2 = False
                            game.player2.bot = False
                else:
                    if reset_button_rect.collidepoint(event.pos):
                        game.reset()


    clock.tick(FPS)