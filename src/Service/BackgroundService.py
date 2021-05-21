import pygame,random

class background:
    def __init__(self):
        self.dicobackground = {
            0: pygame.image.load('src/ressources_graphiques/bg.jpg'),
            1: pygame.image.load('src/ressources_graphiques/water.png'),
            2: pygame.image.load('src/ressources_graphiques/swamp_forest.png'),
            3: pygame.image.load('src/ressources_graphiques/temple.png')
        }
        self.bg =  pygame.transform.scale(self.dicobackground[random.randint(0,len(self.dicobackground)-1)],(1080,720))

    def chooseBackground(self):
        self.bg = pygame.transform.scale(self.dicobackground[random.randint(0,len(self.dicobackground)-1)],(1080,720))