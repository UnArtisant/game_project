import pygame

class Menu():
    def __init__(self):
        # Images de numeros de persos :
        self.perso_1 = pygame.image.load("src/ressources_graphiques/1_boutton.png")
        self.perso_1 = pygame.transform.scale(self.perso_1, (100, 100))
        self.perso_1_pressed = pygame.image.load("src/ressources_graphiques/1_boutton_pressed.png")
        self.perso_1_pressed = pygame.transform.scale(self.perso_1_pressed, (100, 100))

        self.perso_2 = pygame.image.load("src/ressources_graphiques/2_boutton.png")
        self.perso_2 = pygame.transform.scale(self.perso_2, (100, 100))
        self.perso_2_pressed = pygame.image.load("src/ressources_graphiques/2_boutton_pressed.png")
        self.perso_2_pressed = pygame.transform.scale(self.perso_2_pressed, (100, 100))

        self.perso_3 = pygame.image.load("src/ressources_graphiques/3_boutton.png")
        self.perso_3 = pygame.transform.scale(self.perso_3, (100, 100))
        self.perso_3_pressed = pygame.image.load("src/ressources_graphiques/3_boutton_pressed.png")
        self.perso_3_pressed = pygame.transform.scale(self.perso_3_pressed, (100, 100))

        self.perso_4 = pygame.image.load("src/ressources_graphiques/4_boutton.png")
        self.perso_4 = pygame.transform.scale(self.perso_4, (100, 100))
        self.perso_4_pressed = pygame.image.load("src/ressources_graphiques/4_boutton_pressed.png")
        self.perso_4_pressed = pygame.transform.scale(self.perso_4_pressed, (100, 100))


        # Boutons J1 :
        self.j1_image = pygame.image.load("src/ressources_graphiques/Joueur1_boutton.png")
        self.j1_image = pygame.transform.scale(self.j1_image, (250, 100))
        self.j1_image_rect = self.j1_image.get_rect()
        self.j1_image_rect.x = 145
        self.j1_image_rect.y = 400

        self.j_choix = pygame.image.load("src/ressources_graphiques/joueur.png")
        self.j_choix_pressed = pygame.image.load("src/ressources_graphiques/joueur_pressed.png")
        self.j_choix = pygame.transform.scale(self.j_choix, (120, 100))
        self.j_choix_pressed = pygame.transform.scale(self.j_choix_pressed, (120, 100))
        self.j_choix_rect = self.j_choix.get_rect()
        self.j_choix_rect.x = self.j1_image_rect.x
        self.j_choix_rect.y = self.j1_image_rect.y - 10 - self.j1_image_rect.height


        self.b_choix = pygame.image.load("src/ressources_graphiques/bot.png")
        self.b_choix_pressed = pygame.image.load("src/ressources_graphiques/bot_pressed.png")
        self.b_choix = pygame.transform.scale(self.b_choix, (120, 100))
        self.b_choix_pressed = pygame.transform.scale(self.b_choix_pressed, (120, 100))
        self.b_choix_rect = self.b_choix.get_rect()
        self.b_choix_rect.x = self.j_choix_rect.x + 10 + self.j_choix_rect.width
        self.b_choix_rect.y = self.j_choix_rect.y

        self.b1_1_rect = self.perso_1.get_rect()
        self.b1_1_rect.x = 145
        self.b1_1_rect.y = 505

        self.b2_1_rect = self.perso_2.get_rect()
        self.b2_1_rect.x = 145 + self.j1_image_rect.width - self.b2_1_rect.width
        self.b2_1_rect.y = 505

        self.b3_1_rect = self.perso_3.get_rect()
        self.b3_1_rect.x = 145
        self.b3_1_rect.y = 505 + self.b1_1_rect.height + 10

        self.b4_1_rect = self.perso_4.get_rect()
        self.b4_1_rect.x = 145 + self.j1_image_rect.width - self.b2_1_rect.width
        self.b4_1_rect.y = 505 + self.b1_1_rect.height + 10

        # Boutons J2:
        self.j2_image = pygame.image.load("src/ressources_graphiques/Joueur2_boutton.png")
        self.j2_image = pygame.transform.scale(self.j2_image, (250, 100))
        self.j2_image_rect = self.j2_image.get_rect()
        self.j2_image_rect.x = 685  # math.ceil(screen.get_width()/4*3 - (j2_image_rect.width / 2))
        self.j2_image_rect.y = 400

        self.j_choix_2_rect = self.j_choix.get_rect()
        self.j_choix_2_rect.x = self.j2_image_rect.x
        self.j_choix_2_rect.y = self.j2_image_rect.y - 10 - self.j1_image_rect.height

        self.b_choix_2_rect = self.b_choix.get_rect()
        self.b_choix_2_rect.x = self.j_choix_2_rect.x + 10 + self.j_choix_rect.width
        self.b_choix_2_rect.y = self.j_choix_2_rect.y

        self.b1_2_rect = self.perso_1.get_rect()
        self.b1_2_rect.x = 685
        self.b1_2_rect.y = 505

        self.b2_2_rect = self.perso_2.get_rect()
        self.b2_2_rect.x = 685 + self.j2_image_rect.width - self.b2_2_rect.width
        self.b2_2_rect.y = 505

        self.b3_2_rect = self.perso_3.get_rect()
        self.b3_2_rect.x = 685
        self.b3_2_rect.y = 505 + self.b1_1_rect.height + 10

        self.b4_2_rect = self.perso_4.get_rect()
        self.b4_2_rect.x = 685 + self.j2_image_rect.width - self.b2_2_rect.width
        self.b4_2_rect.y = 505 + self.b1_1_rect.height + 10

        # Boutons choix commandes
        self.punch_button_not_pressed = pygame.image.load("src/ressources_graphiques/punch_not_pressed.png")
        self.punch_button_not_pressed = pygame.transform.scale(self.punch_button_not_pressed, (76, 76))
        self.punch_button_pressed = pygame.image.load("src/ressources_graphiques/punch_pressed.png")
        self.punch_button_pressed = pygame.transform.scale(self.punch_button_pressed, (76, 76))

        self.attack_button_not_pressed = pygame.image.load("src/ressources_graphiques/attack_not_pressed.png")
        self.attack_button_not_pressed = pygame.transform.scale(self.attack_button_not_pressed, (76, 76))
        self.attack_button_pressed = pygame.image.load("src/ressources_graphiques/attack_pressed.png")
        self.attack_button_pressed = pygame.transform.scale(self.attack_button_pressed, (76, 76))

        self.block_button_not_pressed = pygame.image.load("src/ressources_graphiques/block_not_pressed.png")
        self.block_button_not_pressed = pygame.transform.scale(self.block_button_not_pressed, (76, 76))
        self.block_button_pressed = pygame.image.load("src/ressources_graphiques/block_pressed.png")
        self.block_button_pressed = pygame.transform.scale(self.block_button_pressed, (76, 76))

        self.attack_button_1 = self.attack_button_not_pressed.get_rect()
        self.attack_button_1.x = self.j1_image_rect.x
        self.attack_button_1.y = self.j_choix_rect.y - self.attack_button_1.height - 10
        self.choice_attack_1 = False

        self.punch_button_1 = self.punch_button_not_pressed.get_rect()
        self.punch_button_1.x = self.attack_button_1.x + self.attack_button_1.width + 10
        self.punch_button_1.y = self.attack_button_1.y
        self.choice_punch_1 = False

        self.block_button_1 = self.block_button_not_pressed.get_rect()
        self.block_button_1.x = self.punch_button_1.x + self.punch_button_1.width + 10
        self.block_button_1.y = self.attack_button_1.y
        self.choice_block_1 = False

        self.attack_button_2 = self.attack_button_not_pressed.get_rect()
        self.attack_button_2.x = self.j2_image_rect.x
        self.attack_button_2.y = self.j_choix_2_rect.y - self.attack_button_2.height - 10
        self.choice_attack_2 = False

        self.punch_button_2 = self.punch_button_not_pressed.get_rect()
        self.punch_button_2.x = self.attack_button_2.x + self.attack_button_2.width + 10
        self.punch_button_2.y = self.attack_button_2.y
        self.choice_punch_2 = False

        self.block_button_2 = self.block_button_not_pressed.get_rect()
        self.block_button_2.x = self.punch_button_2.x + self.punch_button_2.width + 10
        self.block_button_2.y = self.attack_button_2.y
        self.choice_block_2 = False

        self.parametre_button = pygame.image.load("src/ressources_graphiques/parametre.png")
        self.parametre_button = pygame.transform.scale(self.parametre_button, (50,75))
        self.parametre_button_rect = self.parametre_button.get_rect()
        self.parametre_button_rect.x = 20
        self.parametre_button_rect.y = 20

    def printButtons(self,screen,game):

        # Afficher tous les boutons du menu
        game.text = game.font.render("", 1, (255, 0, 0))
        screen.blit(self.j1_image, self.j1_image_rect)
        screen.blit(self.j2_image, self.j2_image_rect)
        screen.blit(self.perso_1, self.b1_1_rect)
        screen.blit(self.perso_1, self.b1_2_rect)
        screen.blit(self.perso_2, self.b2_1_rect)
        screen.blit(self.perso_2, self.b2_2_rect)
        screen.blit(self.perso_3, self.b3_2_rect)
        screen.blit(self.perso_4, self.b4_2_rect)
        screen.blit(self.perso_3, self.b3_1_rect)
        screen.blit(self.perso_4, self.b4_1_rect)
        screen.blit(self.j_choix, self.j_choix_rect)
        screen.blit(self.b_choix, self.b_choix_rect)
        screen.blit(self.j_choix, self.j_choix_2_rect)
        screen.blit(self.b_choix, self.b_choix_2_rect)
        screen.blit(self.parametre_button,self.parametre_button_rect)

        # Affichage des boutons de choix du perso du joueur 1
        if game.player1.id == 0:
            screen.blit(self.perso_1_pressed, self.b1_1_rect)
        elif game.player1.id == 1:
            screen.blit(self.perso_2_pressed, self.b2_1_rect)
        elif game.player1.id == 2:
            screen.blit(self.perso_3_pressed, self.b3_1_rect)
        elif game.player1.id == 3:
            screen.blit(self.perso_4_pressed, self.b4_1_rect)
        # Affichage des boutons de choix du perso du joueur 2
        if game.player2.id == 0:
            screen.blit(self.perso_1_pressed, self.b1_2_rect)
        elif game.player2.id == 1:
            screen.blit(self.perso_2_pressed, self.b2_2_rect)
        elif game.player2.id == 2:
            screen.blit(self.perso_3_pressed, self.b3_2_rect)
        elif game.player2.id == 3:
            screen.blit(self.perso_4_pressed, self.b4_2_rect)
        #Affichage du bouton du choix du type du joueur 1 (Joueur/Bot)
        if game.is_bot_1:
            screen.blit(self.b_choix_pressed, self.b_choix_rect)
        else:
            screen.blit(self.j_choix_pressed, self.j_choix_rect)
        # Affichage du bouton du choix du type du joueur 2 (Joueur/Bot)
        if game.is_bot_2:
            screen.blit(self.b_choix_pressed, self.b_choix_2_rect)
        else:
            screen.blit(self.j_choix_pressed, self.j_choix_2_rect)

        #Affichage des boutons de choix de touches
        if not self.choice_punch_1:
            screen.blit(self.punch_button_not_pressed, self.punch_button_1)
        else:
            screen.blit(self.punch_button_pressed, self.punch_button_1)

        if not self.choice_punch_2:
            screen.blit(self.punch_button_not_pressed, self.punch_button_2)
        else:
            screen.blit(self.punch_button_pressed, self.punch_button_2)

        if not self.choice_attack_1:
            screen.blit(self.attack_button_not_pressed, self.attack_button_1)
        else:
            screen.blit(self.attack_button_pressed, self.attack_button_1)

        if not self.choice_attack_2:
            screen.blit(self.attack_button_not_pressed, self.attack_button_2)
        else:
            screen.blit(self.attack_button_pressed, self.attack_button_2)

        if not self.choice_block_1:
            screen.blit(self.block_button_not_pressed, self.block_button_1)
        else:
            screen.blit(self.block_button_pressed, self.block_button_1)

        if not self.choice_block_2:
            screen.blit(self.block_button_not_pressed, self.block_button_2)
        else:
            screen.blit(self.block_button_pressed, self.block_button_2)
