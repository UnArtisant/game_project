import pygame
import math

class fireball(pygame.sprite.Sprite):
    def __init__(self,player,game):
        super().__init__()
        self.game = game
        self.type = 1
        self.velocity = 20
        self.image = pygame.image.load("src/Service/Perso1/graphismes/projectile.png")
        self.image = pygame.transform.scale(self.image,(30,30))
        self.rect = self.image.get_rect()
        self.direction = player.direction
        self.player = player
        if self.direction:
            self.rect.x = player.rect.x + player.rect.width
        else:
            self.rect.x = player.rect.x-50
        self.rect.y = player.rect.y + 80
        self.origin_y = self.rect.y
        self.origin = self.image
        self.angle = 0
        self.dist = 0
        self.max = 50
        self.long = 700
        self.alpha = 45
        self.g_constant = 9.8


    def rotate(self):
        self.angle += 3
        self.angle %= 360
        self.image = pygame.transform.rotozoom(self.origin,self.angle,1)
        self.rect = self.image.get_rect(center=self.rect.center)

    def remove(self):
        self.player.projectiles.remove(self)

    def move(self):
        if not (self.game.check_colision(self,self.player.enemys)):
            if 0<self.rect.x < 1080  and self.rect.y < (700 - self.rect.height):
                if self.direction == 1:
                    self.rect.x += self.velocity
                    self.dist += self.velocity
                    a = self.max/((self.long/2)**2 -self.long**2/2 )
                    self.rect.y = self.origin_y + math.ceil(-a*(self.dist**2 - self.dist*self.long))

                else :
                    self.rect.x -= self.velocity
                    self.dist += self.velocity
                    a = self.max / ((self.long / 2) ** 2 - self.long ** 2 / 2)
                    self.rect.y = self.origin_y + math.ceil(-a * (self.dist ** 2 - self.dist * self.long))
                self.rotate()
            else :
                self.remove()
        else :
            self.player.enemy.take_damages(dmg = self.player.fireBallDmg,freeze= self.player.fireball_freeze)
            self.remove()
