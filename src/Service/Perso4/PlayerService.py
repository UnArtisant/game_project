import pygame
import math
import random
from src.Service.Perso4.BoomerangService import boomerang
from src.Service.Perso4.PunchService import punch

class Perso4(pygame.sprite.Sprite):
    def __init__(self,game,num,bot):
        super().__init__()
        self.id = 3
        self.game = game
        self.num_player = num
        self.max_health = 200
        self.enemy = 0
        self.enemys = pygame.sprite.Group()
        self.animations = {}
        self.animations[0] = pygame.transform.scale(
            pygame.image.load("src/Service/Perso4/graphismes/Marche/marche6.png"), (150, 200))
        self.animations[1] = []
        self.animations[2] = []
        for i in range(1, 7):
            self.animations[1].append(
                pygame.transform.scale(pygame.image.load(f"src/Service/Perso4/graphismes/Marche/marche{i}.png"),
                                       (150, 200)))
        for i in range(1, 5):
            self.animations[2].append(
                pygame.transform.scale(pygame.image.load(f"src/Service/Perso4/graphismes/Punch/punch{i}.png"),
                                       (150, 200)))
        self.animation_time = 100
        self.action = 0
        self.frame = 0
        self.health = self.max_health
        self.bowmerangDmg = 10
        self.fistDmg = 15
        self.bowmerang_freeze = 10
        self.punch_freeze = 15
        self.paradeReduction = 0.6
        self.velocity = 7
        self.image = self.animations[0]
        self.origin = self.image
        if self.num_player == 1:
            self.image = pygame.transform.flip(self.origin, True, False)
        self.rect = self.image.get_rect()
        self.rect.x = [0,1080-self.rect.width][self.num_player]
        self.rect.y = 700 - self.rect.height
        self.projectiles = pygame.sprite.Group()
        self.direction = [1,0][num]
        self.parade = False
        self.jump = 0
        self.jump_high = 200
        self.jump_time = 600
        self.jump_speed = 15
        self.cooldown = 0
        self.cooldown_punch = 0
        self.freeze = 0
        self.before = self.origin
        self.bot = bot
        self.try_parade = [False, 0]
        self.last_update = pygame.time.get_ticks()

    def animate(self):
        if self.action != 0:
            current_time = pygame.time.get_ticks()
            if current_time - self.last_update >= self.animation_time:
                self.last_update = current_time
                self.frame +=1
                if self.frame>= len(self.animations[self.action]):
                    self.frame = 0
                    self.action = 0
                    self.image =  pygame.transform.flip(self.animations[self.action],not self.direction,False)
                else :
                    self.image = pygame.transform.flip(self.animations[self.action][self.frame],not self.direction,False)

    def finish_init(self,enemy):
        self.enemys = pygame.sprite.Group()
        self.enemy = enemy
        self.enemys.add(self.enemy)

    def parade_on(self):
        if not self.freeze :
            self.parade = True
            self.before = self.image
            self.image = pygame.image.load("src/Service/Perso4/graphismes/Ryu_parade.png")
            self.image = pygame.transform.scale(self.image, (150, 200))
            if self.direction == 0:
                self.image = pygame.transform.flip(self.image,True,False)

    def parade_off(self):
        self.parade = False
        self.image = self.before

    def low_freeze(self):
        if self.freeze:
            self.freeze -= 1
            if self.freeze >= 1:
                self.image = pygame.image.load("src/Service/Perso4/graphismes/Ryu_freezed.png")
                self.image = pygame.transform.scale(self.image, (150, 200))
                if self.direction == 0:
                    self.image = pygame.transform.flip(self.image, True, False)
            else :
                self.image = self.before

    def low_cooldown(self):
        if self.cooldown>0 :
            self.cooldown-=1
        if self.cooldown_punch>0:
            self.cooldown_punch -= 1

    def attack_spe(self):
        if not self.parade and not self.cooldown and not self.freeze:
            self.projectiles.add(boomerang(self, self.game))
            self.cooldown = 60

    def launch_punch(self):
        if not self.parade and not self.cooldown_punch and not self.freeze:
            self.projectiles.add(punch(self,self.game))
            self.cooldown_punch = 40
            if self.action != 2:
                self.action = 2
                self.frame = 0

    def press_jump(self):
        if self.rect.y == 700 - self.rect.height and not self.freeze and not self.parade:
            self.jump = self.jump_time

    def jump_action(self):
        if self.jump:
            jump = self.jump_time//2 - self.jump
            self.rect.y = 700 - self.rect.height + math.ceil((self.jump_high / (self.jump_time//2)**2) * (jump ** 2 - (self.jump_time//2)**2))
            self.jump -= self.jump_speed
        else:
            self.rect.y = 700 - self.rect.height

    def move_right(self):
        if not self.parade and not self.freeze:
            if self.rect.x+ self.rect.width < 1080:
                self.rect.x += self.velocity
            self.direction = 1
            if self.action != 1:
                self.action = 1
                self.frame = 0

    def move_left(self):
        if not self.parade and not self.freeze:
            if 0<self.rect.x :
                self.rect.x -= self.velocity
            self.direction = 0
            if self.action != 1:
                self.action = 1
                self.frame = 0

    def take_damages(self,dmg,freeze):
        if self.parade :
            dmg *= 1 - self.paradeReduction
            freezebool = False
        else :
            freezebool = True
        self.health -= dmg
        if freezebool:
            if self.freeze==0:
                self.before = self.image
            if self.freeze < freeze:
                self.freeze = freeze

        #Si la vie arrive à 0
        if self.health <= 0:
            self.game.text = self.game.font.render(f"Player {self.enemy.num_player +1} win ",1,(255, 0, 0 ))
            self.game.reset()

    def update_health_bar(self,surface):
        if self.num_player==1:
            bar_color = (255, 0, 0)
        else :
            bar_color = (74, 202, 25)
        bg_bar_color = (105, 102, 102)
        x = self.max_health//100
        bg_bar_position = [self.rect.x, self.rect.y -20,self.max_health//x,10]
        bar_position = [self.rect.x, self.rect.y -20,self.health//x,10]
        pygame.draw.rect(surface,bg_bar_color,bg_bar_position)
        pygame.draw.rect(surface,bar_color,bar_position)

    def bot_action(self):
        #Réorienter le joueur par rapport à l'ennemi :
        move = False
        #utiliser l'attaque speciale dès que possible
        if self.cooldown <= 0:
            if self.enemy.rect.x > self.rect.x and self.direction != 1:
                self.move_right()
                move = True
            if self.enemy.rect.x < self.rect.x and self.direction != 0:
                self.move_left()
                move = True
            self.attack_spe()
            self.cooldown += 30
        #Sauter/bloquer lorsque approchent les projectiles
        #Check si il y a des projectiles ennemis à proximité
        for projectile in self.enemy.projectiles:

            if (projectile.direction==1 and (0 < self.rect.x - projectile.rect.x < 300)) or (projectile.direction == 0 and (0 < projectile.rect.x - self.rect.x - self.rect.width < 300)):
                # Si le projectile est une boule de feu et est à la bonne distance, essayer de sauter
                if projectile.type != 2 and projectile.type:
                    if self.jump<=0 and not random.randint(0,10) and projectile.origin_y  > 400:
                        self.press_jump()
                else:
                    pass
                # Essayer de parer
            if projectile.type !=2:
                if not self.try_parade[0] and ((projectile.direction==1 and (0 < self.rect.x - projectile.rect.x < 200)) or (projectile.direction == 0 and (0 < projectile.rect.x - self.rect.x - self.rect.width < 200))):
                    self.try_parade[1] = random.randint(0,3)
                    self.try_parade[0]=True
                    if self.try_parade[1] > 0 :
                        self.parade_on()
            else:
                if projectile.rect.x-25  <= self.rect.x and projectile.rect.x-self.rect.x < self.rect.width + 25:
                    self.move_right()
                    move = True
                elif self.rect.x <= 25 + projectile.rect.x + projectile.rect.width and self.rect.x-projectile.rect.x < self.rect.width + 25:
                    self.move_left()
                    move = True

            #Si il y a pas de projectile à proximité alors  arreter de parer

        if len(self.enemy.projectiles)==0:
            self.try_parade = [False,0]

        #Arreter la parade
        if not self.try_parade[1] or not self.try_parade[0]:
            self.parade_off()

        #Lancer un coup de poing si le cooldown est au minimum et si l'ennemi est proche
        if self.cooldown_punch <=0 and abs(self.rect.x-self.enemy.rect.x) < 180:
            if not move :
                #Se réorienter en fonction de l'ennemi avant de tirer
                if self.enemy.rect.x > self.rect.x and self.direction != 1:
                    self.move_right()
                    move = True
                if self.enemy.rect.x < self.rect.x and self.direction != 0:
                    self.move_left()
                    move = True
            self.launch_punch()
            self.cooldown_punch += 30


        #Se deplacer vers l'ennemi si on est plus haut en vie que l'adversaire
        if not move:
            if self.health > self.enemy.health + 20 :
                if abs(self.enemy.rect.x-self.rect.x) >150:
                    if self.direction:
                        self.move_right()
                    else:
                        self.move_left()

        # Se déplacer pour arriver a une distance raisonnable de l'ennemi
        if not move:
            if abs(self.enemy.rect.x - self.rect.x) > 500:
                if self.enemy.rect.x > self.rect.x:
                    self.move_right()
                    move = True
                if self.enemy.rect.x < self.rect.x:
                    self.move_left()
                    move = True