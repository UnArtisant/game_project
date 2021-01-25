import pygame

class Player1(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.health = 100
        self.fireBallDmg = 5
        self.fistDmg = 10
        self.paradeReduction = 0.8
        self.velocity = 5
        self.image = pygame.image.load("src/ressources_graphiques/player.png")
        self.rect = self.image.get_rect()
        self.rect.x = 500
        self.rect.y = 360