import pygame

class People(pygame.sprite.Sprite):
    def __init__(self,position):
        pygame.sprite.Sprite.__init__(self)
        self.image_front = pygame.image.load("images/people/man_front.png").convert_alpha()
        self.image_left = pygame.image.load("images/people/man_left.png").convert_alpha()
        self.image_right = pygame.image.load("images/people/man_right.png").convert_alpha()
        self.image_back = pygame.image.load("images/people/man_back.png").convert_alpha()



        self.people = self.image_front
        self.mask = pygame.mask.from_surface(self.people)
        self.rect = self.people.get_rect()
        self.rect.left,self.rect.top = position
        self.speed = 32

    def moveLeft(self):
        self.rect.left -= self.speed
        self.people = self.image_left       

    def moveRight(self):
        self.rect.left += self.speed
        self.people = self.image_right

    def moveUp(self):
        self.rect.top -= self.speed
        self.people = self.image_back


    def moveDown(self):
        self.rect.top += self.speed
       	self.people = self.image_front
    
        
        

