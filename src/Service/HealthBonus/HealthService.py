import pygame

class healthBoost(pygame.sprite.Sprite):
    def __init__(self,game):
        super().__init__()
        self.game = game
        self.regen = 20
        self.image = pygame.image.load("src/Service/HealthBonus/heal.png")
        self.image = pygame.transform.scale(self.image, (50, 50))
        self.rect = self.image.get_rect()
        self.rect.x = 1080/2 - self.rect.width/2
        self.rect.y = 720/2 - self.rect.height/2

    def remove(self):
        self.game.bonus.remove(self)

    def check(self):
        if self.game.check_colision(self.game.player1,self.game.bonus):
            self.game.player1.health += self.regen
            if self.game.player1.health > self.game.player1.max_health:
                self.game.player1.health = self.game.player1.max_health
            self.remove()
        if self.game.check_colision(self.game.player2,self.game.bonus):
            self.game.player2.health += self.regen
            if self.game.player2.health > self.game.player2.max_health:
                self.game.player2.health = self.game.player2.max_health
            self.remove()
