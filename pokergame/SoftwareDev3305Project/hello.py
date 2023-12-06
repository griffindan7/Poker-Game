import math
import time

import treys
from treys import Evaluator

import pygame

from pygame.locals import (
    RLEACCEL
)

from Player import Player
from spritesheet import Spritesheet
import random

pygame.init()

screen = pygame.display.set_mode([900, 500])
height = screen.get_height()
width = screen.get_width()
color = (255, 255, 255)
color_light = (170, 170, 170)
color_dark = (100, 100, 100)
smallfont = pygame.font.Font('assets/gluegun.ttf', 35)
text = smallfont.render('Deal', True, color)

running = True

me = Player("me", 100, [])
opponent = Player("oppo", 100, [])

sprite_to_card_format = {
    0: 'Ac', 1: '2c', 2: '3c', 3: '4c', 4: '5c', 5: '6c', 6: '7c', 7: '8c', 8: '9c', 9: 'Tc', 10: 'Jc', 11: 'Qc',
    12: 'Kc',
    13: 'Ah', 14: '2h', 15: '3h', 16: '4h', 17: '5h', 18: '6h', 19: '7h', 20: '8h', 21: '9h', 22: 'Th', 23: 'Jh',
    24: 'Qh', 25: 'Kh',
    26: 'As', 27: '2s', 28: '3s', 29: '4s', 30: '5s', 31: '6s', 32: '7s', 33: '8s', 34: '9s', 35: 'Ts', 36: 'Js',
    37: 'Qs', 38: 'Ks',
    39: 'Ad', 40: '2d', 41: '3d', 42: '4d', 43: '5d', 44: '6d', 45: '7d', 46: '8d', 47: '9d', 48: 'Td', 49: 'Jd',
    50: 'Qd', 51: 'Kd'
}


class Sprite(pygame.sprite.Sprite, ):

    def __init__(self, card):
        super(Sprite, self).__init__()
        self.card = card
        self.surf = pygame.image.load(card).convert()
        self.surf.set_colorkey((1, 1, 1), RLEACCEL)


class Card(pygame.sprite.Sprite):

    def __init__(self, card):
        super(Card, self).__init__()
        self.card = card
        self.surf = my_spritesheet.parse_sprite(card)
        self.surf.set_colorkey((1, 1, 1), RLEACCEL)
        self.rect = self.surf.get_rect()


my_spritesheet = Spritesheet('cards.png')

start = True
preflop = False
flop = False
turn = False
river = False
showdown = False
result_str = ''
player_C1 = ''
player_C2 = ''
oppo_C1 = ''
oppo_C2 = ''
flop_C1 = ''
flop_C2 = ''
flop_C3 = ''
flop_C4 = ''
flop_C5 = ''
pot = 0


def button(btn_width, btn_height, input_text, func, event):
    text = smallfont.render(input_text, True, color)
    mouse = pygame.mouse.get_pos()
    if event.type == pygame.MOUSEBUTTONDOWN:
        if btn_width <= mouse[0] <= btn_width + 140 and btn_height <= mouse[1] <= btn_height + 40:
            func()
    if btn_width <= mouse[0] <= btn_width + 140 and btn_height <= mouse[1] <= btn_height + 40:
        pygame.draw.rect(screen, color_light, [btn_width, btn_height, 140, 40])
    else:
        pygame.draw.rect(screen, color_dark, [btn_width, btn_height, 140, 40])
    screen.blit(text, (btn_width + 40, btn_height))
    pygame.display.flip()


def deal():
    screen.fill((58, 140, 38))
    global start
    global preflop
    global player_C1
    global player_C2
    global oppo_C1
    global oppo_C2
    global flop_C1
    global flop_C2
    global flop_C3
    global flop_C4
    global flop_C5
    global cards_dealt
    rand1 = random.randint(0, 51)
    rand2 = random.randint(0, 51)
    i = 7
    flop_cards = []

    if rand1 != rand2:
        player_C1 = Card('cards-%s.png' % rand1)
        player_C2 = Card('cards-%s.png' % rand2)
        cards_dealt = [rand1, rand2]
    else:
        deal()
    while i != 0:
        rand = random.randint(0, 51)
        if rand not in cards_dealt:
            flop_cards.append(rand)
            cards_dealt.append(rand)
            i -= 1
    flop_C1 = Card('cards-%s.png' % flop_cards[0])
    flop_C2 = Card('cards-%s.png' % flop_cards[1])
    flop_C3 = Card('cards-%s.png' % flop_cards[2])
    flop_C4 = Card('cards-%s.png' % flop_cards[3])
    flop_C5 = Card('cards-%s.png' % flop_cards[4])
    oppo_C1 = Card('cards-%s.png' % cards_dealt[7])
    oppo_C2 = Card('cards-%s.png' % cards_dealt[8])

    start = False
    preflop = True


def oppo_move(slider):
    choice = random.randint(0, slider)
    if choice == 0:
        return 0
    else:
        return 1


def bet_logic(bet_size):
    global pot
    me.set_bet_amount(bet_size)
    me.remove_chips(bet_size)
    pot += me.bet_amount

    if oppo_move(10) == 0:
        print("oppo folds")
        me.chips += pot
        pot = 0
        return 0
    else:
        print('opponet calls')
        opponent.set_bet_amount(bet_size)
        opponent.set_chips((opponent.chips - opponent.bet_amount))
        pot += opponent.bet_amount

        return 1


def decide_winner():
    global cards_dealt
    global pot
    global start
    global showdown
    global result_str
    board = []
    board.append(sprite_to_card_format[cards_dealt[0]])
    board.append(sprite_to_card_format[cards_dealt[1]])

    board.append(sprite_to_card_format[cards_dealt[2]])
    board.append(sprite_to_card_format[cards_dealt[3]])
    board.append(sprite_to_card_format[cards_dealt[4]])
    board.append(sprite_to_card_format[cards_dealt[5]])
    board.append(sprite_to_card_format[cards_dealt[6]])

    board.append(sprite_to_card_format[cards_dealt[7]])
    board.append(sprite_to_card_format[cards_dealt[8]])


    print(board)


    # board = [
    #     treys.Card.new(board[2]),
    #     treys.Card.new(board[3]),
    #     treys.Card.new(board[4]),
    #
    # ]
    shared_cards = [
        treys.Card.new(board[2]),
        treys.Card.new(board[3]),
        treys.Card.new(board[4]),
        treys.Card.new(board[5]),
        treys.Card.new(board[6])

    ]

    my_hand = [
        treys.Card.new(board[0]),
        treys.Card.new(board[1])
    ]

    oppo_hand = [
        treys.Card.new(board[7]),
        treys.Card.new(board[8])
    ]

    evaluator = Evaluator()
    p1_score = evaluator.evaluate(shared_cards, my_hand)
    p2_score = evaluator.evaluate(shared_cards, oppo_hand)
    p1_class = evaluator.get_rank_class(p1_score)
    p2_class = evaluator.get_rank_class(p2_score)


    print("My hand rank = %d (%s)\n" % (p1_score, evaluator.class_to_string(p1_class)))
    print("opponant hand rank = %d (%s)\n" % (p2_score, evaluator.class_to_string(p2_class)))

    if p1_score < p2_score:
        result_str = "%s beats %s, i win" % (evaluator.class_to_string(p1_class),evaluator.class_to_string(p2_class))
        print(result_str)

        me.add_chips(pot)
        pot = 0

    else:
        result_str = "%s beats %s, i lose" % (evaluator.class_to_string(p2_class),evaluator.class_to_string(p1_class))
        print(result_str)

        opponent.add_chips(pot)
        pot = 0


    showdown = False
    start = True


def bet():

    print("bet button pressed")
    screen.fill((58, 140, 38))
    global pot
    global start
    global preflop
    global flop
    global turn
    global river
    global showdown

    if preflop:
        print('bet preflop sec')
        if bet_logic(5) == 0:
            preflop = False
            start = True
        else:
            preflop = False
            flop = True

    elif flop:
        print('bet flop sec')
        if bet_logic(5) == 0:
            flop = False
            start = True
        else:
            flop = False
            turn = True

    elif turn:
        print('bet turn sec')
        if bet_logic(5) == 0:
            turn = False
            start = True
        else:
            turn = False
            river = True
    elif river:
        print('bet river sec')
        if bet_logic(5) == 0:
            river = False
            start = True
        else:
            river = False
            turn = False
            flop = False
            preflop = False
            showdown = True


def fold():
    screen.fill((58, 140, 38))
    global start
    global preflop
    global flop
    global turn
    global river
    global pot
    print("I folds")
    opponent.chips += pot
    pot = 0
    start = True
    preflop = False
    flop = False
    turn = False
    river = False


def check():
    screen.fill((58, 140, 38))
    global start
    global preflop
    global flop
    global turn
    global river
    global showdown

    if preflop:
        preflop = False
        flop = True

    elif flop:
        flop = False
        turn = True

    elif turn:
        turn = False
        river = True

    elif river:
        river = False
        showdown = True


def text(msg, size, color):
    font = pygame.font.Font('assets/gluegun.ttf', size)
    newText = font.render(msg, True, color)

    return newText


def main():
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                quit()
            if showdown:
                decide_winner()



                text_results = text(result_str, 50, (255,255,255))
                text_results.get_rect()
                result_text = text_results.get_rect()
                screen.blit(text_results, (600 - (result_text[2] / 2), 330))




                text_pot = text("pot: " + str(pot), 50, (255, 255, 255))
                text_pot.get_rect()
                pot_rect = text_pot.get_rect()
                screen.blit(text_pot, (520, 175))

                text_my_chips = text("My Chips: " + str(me.chips), 30, (255, 255, 255))
                text_my_chips.get_rect()
                my_chips_rect = text_my_chips.get_rect()
                screen.blit(text_my_chips, (420, 430))

                text_oppo_chips = text("Opponent Chips: " + str(opponent.chips), 30, (255, 255, 255))
                text_oppo_chips.get_rect()
                oppo_chips_rect = text_oppo_chips.get_rect()
                screen.blit(text_oppo_chips, (420 , 50))

                screen.blit(flop_C1.surf, (10, 150))
                screen.blit(flop_C2.surf, (110, 150))
                screen.blit(flop_C3.surf, (210, 150))
                screen.blit(flop_C4.surf, (310, 150))
                screen.blit(flop_C5.surf, (410, 150))

                screen.blit(oppo_C1.surf, (300, 10))
                screen.blit(oppo_C2.surf, (200, 10))




                pygame.display.flip()

            if river:
                text_stage = text("River", 50, (255, 255, 255))
                text_stage.get_rect()
                stage_rect = text_stage.get_rect()
                screen.blit(text_stage, (800 - (stage_rect[2] / 2), 400))

                button(0, 360, 'Check', check, event)
                button(0, 410, 'Bet ', bet, event)
                button(0, 460, 'Fold', fold, event)

                screen.blit(player_C1.surf, (200, 400))
                screen.blit(player_C2.surf, (300, 400))
                screen.blit(flop_C1.surf, (10, 150))
                screen.blit(flop_C2.surf, (110, 150))
                screen.blit(flop_C3.surf, (210, 150))
                screen.blit(flop_C4.surf, (310, 150))
                screen.blit(flop_C5.surf, (410, 150))

                screen.blit(Sprite('back.png').surf, (300, 10))
                screen.blit(Sprite('back.png').surf, (200, 10))

                text_pot = text("pot: " + str(pot), 50, (255, 255, 255))
                text_pot.get_rect()
                pot_rect = text_pot.get_rect()
                screen.blit(text_pot, (520, 175))

                text_my_chips = text("My Chips: " + str(me.chips), 30, (255, 255, 255))
                text_my_chips.get_rect()
                my_chips_rect = text_my_chips.get_rect()
                screen.blit(text_my_chips, (420, 430))

                text_oppo_chips = text("Opponent Chips: " + str(opponent.chips), 30, (255, 255, 255))
                text_oppo_chips.get_rect()
                oppo_chips_rect = text_oppo_chips.get_rect()
                screen.blit(text_oppo_chips, (420 , 50))

                pygame.display.flip()

            if turn:
                text_stage = text("Turn", 50, (255, 255, 255))
                text_stage.get_rect()
                stage_rect = text_stage.get_rect()
                screen.blit(text_stage, (800 - (stage_rect[2] / 2), 400))

                button(0, 360, 'Check', check, event)
                button(0, 410, 'Bet ', bet, event)
                button(0, 460, 'Fold', fold, event)

                screen.blit(player_C1.surf, (200, 400))
                screen.blit(player_C2.surf, (300, 400))

                screen.blit(flop_C1.surf, (10, 150))
                screen.blit(flop_C2.surf, (110, 150))
                screen.blit(flop_C3.surf, (210, 150))
                screen.blit(flop_C4.surf, (310, 150))

                screen.blit(Sprite('back.png').surf, (200, 10))
                screen.blit(Sprite('back.png').surf, (300, 10))

                text_pot = text("pot: " + str(pot), 50, (255, 255, 255))
                text_pot.get_rect()
                pot_rect = text_pot.get_rect()
                screen.blit(text_pot, (520, 175))

                text_my_chips = text("My Chips: " + str(me.chips), 30, (255, 255, 255))
                text_my_chips.get_rect()
                my_chips_rect = text_my_chips.get_rect()
                screen.blit(text_my_chips, (420, 430))

                text_oppo_chips = text("Opponent Chips: " + str(opponent.chips), 30, (255, 255, 255))
                text_oppo_chips.get_rect()
                oppo_chips_rect = text_oppo_chips.get_rect()
                screen.blit(text_oppo_chips, (420 , 50))

                pygame.display.flip()

            """Flop"""
            if flop:
                text_stage = text("Flop", 50, (255, 255, 255))
                text_stage.get_rect()
                stage_rect = text_stage.get_rect()
                screen.blit(text_stage, (800 - (stage_rect[2] / 2), 400))

                button(0, 360, 'Check', check, event)
                button(0, 410, 'Bet ', bet, event)
                button(0, 460, 'Fold', decide_winner, event)

                screen.blit(player_C1.surf, (200, 400))
                screen.blit(player_C2.surf, (300, 400))

                screen.blit(flop_C1.surf, (10, 150))
                screen.blit(flop_C2.surf, (110, 150))
                screen.blit(flop_C3.surf, (210, 150))

                screen.blit(Sprite('back.png').surf, (310, 150))
                screen.blit(Sprite('back.png').surf, (410, 150))

                text_pot = text("pot: " + str(pot), 50, (255, 255, 255))
                text_pot.get_rect()
                pot_rect = text_pot.get_rect()
                screen.blit(text_pot, (520, 175))

                text_my_chips = text("My Chips: " + str(me.chips), 30, (255, 255, 255))
                text_my_chips.get_rect()
                my_chips_rect = text_my_chips.get_rect()
                screen.blit(text_my_chips, (420, 430))

                text_oppo_chips = text("Opponent Chips: " + str(opponent.chips), 30, (255, 255, 255))
                text_oppo_chips.get_rect()
                oppo_chips_rect = text_oppo_chips.get_rect()
                screen.blit(text_oppo_chips, (420 , 50))
                pygame.display.flip()

            """Preflop"""
            if preflop:
                text_stage = text("Preflop", 50, (255, 255, 255))
                text_stage.get_rect()
                stage_rect = text_stage.get_rect()
                screen.blit(text_stage, (800 - (stage_rect[2] / 2), 400))

                button(0, 360, 'Check', check, event)
                button(0, 410, 'Bet', bet, event)
                button(0, 460, 'Fold', fold, event)

                screen.blit(player_C1.surf, (200, 400))
                screen.blit(player_C2.surf, (300, 400))

                screen.blit(Sprite('back.png').surf, (200, 10))
                screen.blit(Sprite('back.png').surf, (300, 10))

                screen.blit(Sprite('back.png').surf, (10, 150))
                screen.blit(Sprite('back.png').surf, (110, 150))
                screen.blit(Sprite('back.png').surf, (210, 150))
                screen.blit(Sprite('back.png').surf, (310, 150))
                screen.blit(Sprite('back.png').surf, (410, 150))

                text_pot = text("pot: " + str(pot), 50, (255, 255, 255))
                text_pot.get_rect()
                pot_rect = text_pot.get_rect()
                screen.blit(text_pot, (520, 175))

                text_my_chips = text("My Chips: " + str(me.chips), 30, (255, 255, 255))
                text_my_chips.get_rect()
                my_chips_rect = text_my_chips.get_rect()
                screen.blit(text_my_chips, (420, 430))

                text_oppo_chips = text("Opponent Chips: " + str(opponent.chips), 30, (255, 255, 255))
                text_oppo_chips.get_rect()
                oppo_chips_rect = text_oppo_chips.get_rect()
                screen.blit(text_oppo_chips, (420 , 50))

                pygame.display.flip()

            """Game Start"""
            if start:
                button(700, 50, 'Deal', deal, event)
                pygame.display.flip()
                screen.fill((58, 140, 38))

    pygame.quit()


if __name__ == "__main__":
    main()
