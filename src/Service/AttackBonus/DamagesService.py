import pygame

class damagesBoost(pygame.sprite.Sprite):
    def __init__(self,game):
        super().__init__()
        self.game = game
        self.regen = 20
        self.image = pygame.image.load("src/Service/AttackBonus/crossed.png")
        self.image = pygame.transform.scale(self.image, (50, 50))
        self.rect = self.image.get_rect()
        self.rect.x = 1080/2 - self.rect.width/2
        self.rect.y = 720/2 - self.rect.height/2

    def remove(self):
        self.game.bonus.remove(self)

    def check(self):
        if self.game.check_colision(self.game.player1,self.game.bonus):
            self.game.player1.fistDmg *= 1.2
            self.remove()
        if self.game.check_colision(self.game.player2,self.game.bonus):
            self.game.player2.fistDmg *= 1.2
            self.remove()
