import pygame

class Wall(pygame.sprite.Sprite):
    def __init__(self,position,isice):
        pygame.sprite.Sprite.__init__(self)
        if isice == 0:
            self.image1 = pygame.image.load("images/wall/2.png").convert_alpha()
        else:
            self.image1 = pygame.image.load("images/wall/ice.png").convert_alpha()

        self.rect = self.image1.get_rect()

        self.rect.left,self.rect.top = position
        self.mask = pygame.mask.from_surface(self.image1)

