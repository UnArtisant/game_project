import pygame
import math

class boomerang(pygame.sprite.Sprite):
    def __init__(self,player,game):
        super().__init__()
        self.game = game
        self.type = 3
        self.velocity = 20
        self.image = pygame.image.load("src/Service/Perso4/graphismes/projectile.png")
        self.image = pygame.transform.scale(self.image,(30,30))
        self.rect = self.image.get_rect()
        self.direction = player.direction
        self.player = player
        if self.direction:
            self.rect.x = player.rect.x + player.rect.width
        else :
            self.rect.x = player.rect.x-50
        self.rect.y = player.rect.y + 80
        self.origin_x = self.rect.x
        self.origin_y = self.rect.y
        self.origin = self.image
        self.angle = 0
        self.dist = 0
        self.max = 50
        self.long = 500
        self.touch = False
        self.max_dist = self.long
        self.first_time = False

    def rotate(self):
        if self.direction == 1:
            self.angle -= 10
        else:
            self.angle += 10
        self.angle %= 360
        self.image = pygame.transform.rotozoom(self.origin,self.angle,1)
        self.rect = self.image.get_rect(center=self.rect.center)

    def remove(self):
        self.player.projectiles.remove(self)

    def move(self):

        if self.rect.y < (700 - self.rect.height):
            if self.direction == 1:
                self.rect.x += self.velocity
                self.dist += self.velocity
                self.max_dist-= self.velocity
                a = self.max/((self.long/2)**2 -self.long**2/2 )
                if self.first_time:
                    self.rect.y = self.origin_y - math.ceil(-a * (self.dist ** 2 - self.dist * self.long))
                else:
                    self.rect.y = self.origin_y + math.ceil(-a*(self.dist**2 - self.dist*self.long))
                if self.max_dist <=0 :
                    if self.first_time:
                        self.remove()
                    self.first_time = True
                    self.max_dist = self.long
                    self.dist = 1
                    self.direction = 0
            else :
                self.rect.x -= self.velocity
                self.dist += self.velocity
                self.max_dist-= self.velocity
                a = self.max / ((self.long / 2) ** 2 - self.long ** 2 / 2)
                if self.first_time:
                    self.rect.y = self.origin_y - math.ceil(-a * (self.dist ** 2 - self.dist * self.long))
                else:
                    self.rect.y = self.origin_y + math.ceil(-a * (self.dist ** 2 - self.dist * self.long))
                if self.max_dist <=0:
                    if self.first_time:
                        self.remove()
                    self.first_time = True
                    self.max_dist = 600
                    self.dist = 1
                    self.direction = 1
            p = pygame.sprite.Group()
            p.add(self.player)
            if self.game.check_colision(self,p):
                self.remove()
            self.rotate()
        else :
            self.remove()
        if (self.game.check_colision(self, self.player.enemys)):
            if not self.touch:
                self.player.enemy.take_damages(dmg = self.player.bowmerangDmg,freeze= self.player.bowmerang_freeze)
                self.touch = True
        else:
            self.touch = False
