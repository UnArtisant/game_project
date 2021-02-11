import pygame
import math
import random

class meteorite(pygame.sprite.Sprite):
    def __init__(self,player,game,num):
        super().__init__()
        self.game = game
        self.type = 2
        self.velocity = 20
        self.image = pygame.image.load("src/Service/Perso3/graphismes/projectile.png")
        self.image = pygame.transform.scale(self.image,(50,50))
        self.rect = self.image.get_rect()
        self.direction = player.direction
        self.player = player
        space = 200
        min_x =self.player.enemy.rect.x-space
        max_x = self.player.enemy.rect.x+space
        x = random.randint(min_x,max_x)
        if x < 0:
            x = 0
        elif x > 1080-self.rect.width:
            x = 1080-self.rect.width
        self.rect.x = x #self.player.enemy.rect.x + self.player.enemy.rect.width //2
        self.rect.y = 0
        self.origin = self.image
        self.numb = num


    def remove(self):
        self.player.projectiles.remove(self)
        if self.numb>1:
           self.player.projectiles.add(meteorite(self.player,self.game,self.numb -1))

    def move(self):
        if not (self.game.check_colision(self,self.player.enemys)):
            if 0<self.rect.x < 1080 and self.rect.y < (700 - self.rect.height):
                self.rect.y += self.velocity
            else :
                self.remove()
        else :
            self.player.enemy.take_damages(dmg = self.player.meteoriteDmg,freeze= self.player.fireball_freeze)
            self.remove()
