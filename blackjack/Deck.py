from blackjack.Card import Card
from random import randint


class Deck:
    suits = ['diamonds', 'hearts', 'spades', 'clubs']
    max_number = 13

    def __init__(self):
        self.cards = []

        for suit in self.suits:
            for number in range(1, self.max_number + 1):
                self.cards.append(Card(number, suit))

    def give_random_card(self):
        """pos = randint(0, len(self.cards))
        return self.cards.pop(pos)"""
        pass

    def __str__(self):
        str_cards = {str(card) for card in self.cards}
        return ",\n".join(str_cards)
