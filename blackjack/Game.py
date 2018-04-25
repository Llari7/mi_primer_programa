from blackjack.Deck import Deck
from blackjack.Player import Player


class Game:
    card_values = {
        1: 11,
        2: 2,
        3: 3,
        4: 4,
        5: 5,
        6: 6,
        7: 7,
        8: 8,
        9: 9,
        10: 10,
        11: 10,
        12: 10,
        13: 10
    }

    def __init__(self):
        self.deck = Deck()
        self.players = []
        self.table_cards = []

    def draft_card(self):
        card = self.deck.give_random_card()
        print(card)
        self.table_cards.append(card)

    def count_table_cards(self):
        total = 0
        for card in self.table_cards:
            if card.number == 1 and total + self.card_values[card.number] > 21:
                total + 1
            else:
                total += self.card_values[card.number]
        return total

    def player_wants_to_continue(self):
        response = input("Quieres otra carta? (Y/N)")
        return response == "Y"

    def run(self):
        user_continue = True
        while user_continue and self.count_table_cards() < 21:
            self.draft_card()
            user_continue = self.player_wants_to_continue()

        score = self.count_table_cards()
        print("Tu puntuación es de {}".format(score))

        if score() > 21:
            print("Has perdido")

    def start_turn(self):
        pass

    def select_winner(self):
        pass

if __name__ == '__main__':
    blackjack = Game()
    blackjack.run()