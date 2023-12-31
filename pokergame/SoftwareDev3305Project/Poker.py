from treys import Card, Evaluator, Deck




# create an evaluator
evaluator = Evaluator()

# or for random cards or games, create a deck
print("Dealing a new hand...")
deck = Deck()
board = deck.draw(5)
print(board)
player1_hand = deck.draw(2)
player2_hand = deck.draw(2)

print("The board:")
print(Card.print_pretty_cards(board))

print("Player 1's cards:")
print(Card.print_pretty_cards(player1_hand))

print("Player 2's cards:")
print(Card.print_pretty_cards(player2_hand))

p1_score = evaluator.evaluate(board, player1_hand)
p2_score = evaluator.evaluate(board, player2_hand)

# bin the scores into classes
p1_class = evaluator.get_rank_class(p1_score)
p2_class = evaluator.get_rank_class(p2_score)

# or get a human-friendly string to describe the score

# or just a summary of the entire hand
hands = [player1_hand, player2_hand]
evaluator.hand_summary(board, hands)
