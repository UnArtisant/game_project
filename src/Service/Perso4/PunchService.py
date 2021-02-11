import pygame

class punch(pygame.sprite.Sprite):
    def __init__(self,player,game):
        super().__init__()
        self.game = game
        self.player = player
        self.type = 0
        self.image = pygame.image.load("src/Service/Perso1/graphismes/fist.png")
        self.image = pygame.transform.scale(self.image,(50,50))
        self.rect = self.image.get_rect()
        if self.player.direction:
            self.rect.x = player.rect.x + player.rect.width//2
            self.image = pygame.transform.flip(self.image, True, False)
        else :
            self.rect.x = player.rect.x
        self.rect.y = player.rect.y + 60
        self.dist = 5
        self.velocity = 20
        self.direction = self.player.direction

    def remove(self):
        self.player.projectiles.remove(self)

    def move(self):
        self.dist -= 1
        if not (self.game.check_colision(self,self.player.enemys)):
            if 0<self.rect.x < 1080 :
                if self.direction == 1:
                    self.rect.x += self.velocity
                else :
                    self.rect.x -= self.velocity
            else :
                self.remove()
        else :
            self.player.enemy.take_damages(dmg = self.player.fistDmg,freeze= self.player.punch_freeze)
            self.remove()
        if self.dist <= 0:
            self.remove()