import pygame


class Gun():

    def __init__(self, screen):
        """инициализаация пушки"""
        self.screen = screen
        self.image = pygame.image.load('image/pixil-frame-0.png')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()
        self.rect.centerx = self.screen_rect.centerx
        self.rect.botton = self.screen_rect.bottom

    def output(self):
        """рисование пушки"""
        self.screen.blit( self.image, self.rect )