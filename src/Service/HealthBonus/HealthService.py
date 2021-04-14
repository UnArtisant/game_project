import pygame

class healthBoost(pygame.sprite.Sprite):
    def __init__(self,game):
        super().__init__()
        self.game = game
        self.regen = 20
        self.image = pygame.image.load("src/Service/HealthBonus/heal.png")
        self.image = pygame.transform.scale(self.image, (30, 30))
        self.rect = self.image.get_rect()
        self.rect.x = 500
        self.rect.y = 500

    def remove(self):
        self.game.bonus.remove(self)

    def check(self):
        if self.game.check_colision(self.game.player1,self.game.bonus):
            self.game.player1.health += self.regen
            self.remove()
        if self.game.check_colision(self.game.player2,self.game.bonus):
            self.game.player2.health += self.regen
            self.remove()
