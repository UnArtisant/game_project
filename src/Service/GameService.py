from src.Service.Perso1.PlayerService import Perso1
from src.Service.Perso2.PlayerService import Perso2
from src.Service.Perso3.PlayerService import Perso3
from src.Service.Perso4.PlayerService import Perso4
from src.Service.HealthBonus.HealthService import healthBoost
from src.Service.AttackBonus.DamagesService import damagesBoost
from src.Service.BackgroundService import background
import pygame
import random
import time
from math import *
class Game :
    def __init__(self,screen):
        #Booléens pour verifier le moment dans le jeu : menu/en jeu/en pause...
        self.is_playing = False
        self.menu = False
        self.pause = False
        #Booléens pour savoir si c'est un joueur ou un bot
        self.is_bot_1 = False
        self.is_bot_2 = False
        #Initiation des instances de joueurs : 1 et 2
        self.player1 = Perso1(self,  0,self.is_bot_1)
        self.player2 = Perso1(self, 1,self.is_bot_2)
        self.bonus = pygame.sprite.Group()
        #Impossibilité d'appeler player2 dans l'initiation de player1 car player2 n'a pas encore été défini donc finir l'initiation
        self.player1.finish_init(self.player2)
        self.player2.finish_init(self.player1)

        self.pressed = {}
        self.screen = screen
        #Choisir la police
        self.font = pygame.font.Font("src/ressources_graphiques/police.ttf",50)
        self.text = self.font.render("",1,(255, 0, 0))
        #Options de chronomètre
        self.begginTime = time.time()
        self.maxTime = 45
        self.chrono = self.maxTime
        self.timepassed = 0
        #Classe fond d'écran
        self.background = background()

    def reset(self):
        #Remettre les conditions de départ à 0
        self.is_playing = False
        self.pause = False
        self.player1 = Perso1(self, 0,self.is_bot_1)
        self.player2 = Perso1(self, 1,self.is_bot_2)
        self.player1.finish_init(self.player2)
        self.player2.finish_init(self.player1)
        self.begginTime = 0
        self.background.chooseBackground();

    def update(self,screen,forward_1,forward_2,backward_1,backward_2):
        self.screen = screen
        # Afficher les personnages et leurs bares de vie
        screen.blit(self.player1.image, self.player1.rect)
        screen.blit(self.player2.image, self.player2.rect)
        self.player1.update_health_bar(screen)
        self.player2.update_health_bar(screen)

        tact = self.maxTime - ceil(time.time() - self.begginTime)
        if tact <= 0 :
            self.is_playing = False
            if self.player1.health > self.player2.health:
                self.text = self.font.render(f"Player 1 win ",1,(255, 0, 0))
            elif self.player1.health < self.player2.health:
                self.text = self.font.render(f"Player 2 win ",1,(255, 0, 0))
            else :
                self.text = self.font.render(f"Draw", 1, (255, 0, 0))
            self.reset()

        if tact < self.chrono:
            if tact // 60 > 0:
                if tact // 60 >= 10:
                    minute = str(tact // 60)
                else:
                    minute = f"0{tact // 60}"
            else:
                minute = "00"
            if tact % 60 > 0:
                if tact % 60 >= 10:
                    seconde = str(tact % 60)
                else:
                    seconde = f"0{tact % 60}"
            else:
                seconde = "00"

            self.textChrono = self.font.render(f"{minute}:{seconde}",1,(0, 0, 0 ))
            self.chrono = tact

        if not self.bonus and not random.randint(0,500):
            self.bonus.add([healthBoost(self),damagesBoost(self)][random.randint(0,1)])

        widthchrono = self.textChrono.get_width()
        screen.blit(self.textChrono, (540 - widthchrono //2, 0))
        # Faire avancer toutes les boules de feu

        for projectile in self.player1.projectiles:
            projectile.move()
        for projectile in self.player2.projectiles:
            projectile.move()

        for bonus in self.bonus:
            bonus.check()
        
        # Faire avancer toutes les boules de feu

        # Afficher à l'écran les projectiles
        self.player1.projectiles.draw(screen)

        self.player2.projectiles.draw(screen)
        self.bonus.draw(screen)

        # Si le joueur a un cooldown alors le diminuerx
        self.player1.low_cooldown()
        self.player2.low_cooldown()

        # Si le joueur est freeze, alors le diminuer la duree de freeze
        self.player1.low_freeze()
        self.player2.low_freeze()

        # Mouvements joueurs 1
        if not self.player1.bot:
            if self.pressed.get(forward_1):
                self.player1.move_right()
                if self.player1.action != 1 :
                    self.action = 1
                    self.frame = 0
            elif self.pressed.get(backward_1):
                self.player1.move_left()
        else:
            self.player1.bot_action()
        self.player1.jump_action()
        if not self.player1.parade and not self.player1.freeze:
            self.player1.animate()
        # Mouvements joueurs 2
        if not self.player2.bot:
            if self.pressed.get(forward_2):
                self.player2.move_right()
            elif self.pressed.get(backward_2):
                self.player2.move_left()
        else :
            self.player2.bot_action()
        self.player2.jump_action()
        if not self.player2.parade and not self.player2.freeze:
            self.player2.animate()

    def check_colision(self,sprite,group):
        return pygame.sprite.spritecollide(sprite,group,False,pygame.sprite.collide_mask)