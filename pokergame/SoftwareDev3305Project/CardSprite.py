import pygame
from pygame.locals import (
    RLEACCEL
)
from spritesheet import Spritesheet
import random

my_spritesheet = Spritesheet('cards.png')
class Sprite(pygame.sprite.Sprite, ):

    def __init__(self, card):
        super(Sprite, self).__init__()
        self.card = card
        self.surf = pygame.image.load(card).convert()
        self.surf.set_colorkey((1, 1, 1), RLEACCEL)


class CardSprite(pygame.sprite.Sprite):

    def __init__(self, card):
        super(CardSprite, self).__init__()
        self.card = card
        self.surf = my_spritesheet.parse_sprite(card)
        self.surf.set_colorkey((1, 1, 1), RLEACCEL)
        self.rect = self.surf.get_rect()