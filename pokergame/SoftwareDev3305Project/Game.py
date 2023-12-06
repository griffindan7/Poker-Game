from Deck import Deck
from Player import Player
from treys import *




class Game:


    player_list = []
    board = []

    def __init__(self, no_of_players, small_blind, big_blind):
        self.no_of_players = no_of_players
        self.small_blind = small_blind
        self.big_blind = big_blind

    def start_game(self):

        game_deck = Deck()
        # shuffle deck
        game_deck.shuffle()

        i = 0
        # adding required number of players
        while i < self.no_of_players:
            self.player_list.append(Player(i,100, []))
            i += 1

    def print_playerlist(self):
        return_string = ''
        for player in self.player_list:
            return_string += player.__str__() + "  //  "

        print(return_string)






def main():



    deck = Deck()
    board = [
        Card.new('Ah'),
        Card.new('Kd'),
        Card.new('Jc')
       ]
    hand = [
        Card.new('Qs'),
        Card.new('Th')
        ]
    board = deck.draw(5)
    player1_hand = deck.draw(2)
    player2_hand = deck.draw(2)
    print(Card.print_pretty_cards(board))






if __name__ == "__main__":
    main()
