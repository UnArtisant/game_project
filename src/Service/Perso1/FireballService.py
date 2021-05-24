import pygame
import math

class fireball(pygame.sprite.Sprite):
    def __init__(self,player,game):
        super().__init__()
        #Creer une boule de feu et la positionner a l'emplacement du joueur qui l'a crée
        self.game = game
        self.type = 1
        self.velocity = 20
        self.image = pygame.image.load("src/Service/Perso1/graphismes/projectile.png")
        self.image = pygame.transform.scale(self.image,(50,50))
        self.image = pygame.transform.flip(self.image, 1-player.direction, False)
        self.rect = self.image.get_rect()
        self.direction = player.direction
        self.player = player
        if self.player.direction:
            self.rect.x = player.rect.x + player.rect.width
        else:
            self.rect.x = player.rect.x-50
        self.rect.y = player.rect.y + 80
        self.origin_y = self.rect.y
        self.origin_x = self.rect.x
        self.origin = self.image
        self.dist = 0
        self.max = 50
        self.long = 700
        self.alpha = 2*math.pi/6
        self.g_constant = 9.8



    def remove(self):
        self.player.projectiles.remove(self)

    def move(self):
        #Si il ne touche pas l'ennemi
        if not (self.game.check_colision(self,self.player.enemys)):
            if 0<self.rect.x < 1080  and self.rect.y < (700 - self.rect.height):
                #Avancer en fonction de l'equation de trajectoire
                if self.direction == 1:
                    x = self.velocity * math.cos(self.alpha) * (self.dist/15)
                    self.rect.x = self.origin_x + x
                    self.dist += self.velocity
                    self.rect.y = self.origin_y -( (-1/2) * self.g_constant * ((self.dist/150)**2) + self.velocity*2 * math.sin(self.alpha) * (self.dist/150))

                else :
                    x = self.velocity * math.cos(self.alpha) * (self.dist / 15)
                    self.rect.x = self.origin_x - x
                    self.dist += self.velocity
                    self.rect.y = self.origin_y - ((-1 / 2) * self.g_constant * ((self.dist / 150) ** 2) + self.velocity * 2 * math.sin(self.alpha) * (self.dist / 150))

            else :
                self.remove()
        else :
            # Si colision : supprimer et faire des dommages à l'ennemi
            self.player.enemy.take_damages(dmg = self.player.fireBallDmg,freeze= self.player.fireball_freeze)
            self.remove()
