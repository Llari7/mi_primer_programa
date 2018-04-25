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
                total += 1
            else:
                total += self.card_values[card.number]
        return total

    @staticmethod
    def ask_yes_no(question):
        response = input("{} (Y/N)".format(question))
        return response.upper() == "Y"

    def run(self):

        new_player = True
        while new_player:
            player_name = input("Cual es el nombre del nuevo jugador?")
            self.players.append(Player(player_name))
            new_player = self.ask_yes_no("Quieres añadir a otro jugador?")
        for player in self.players:
            user_continue = True
            print("Turno del jugador {}.".format(player.name))
            while user_continue and self.count_table_cards() < 21:
                self.draft_card()
                user_continue = self.ask_yes_no("Quieres otra carta?")

            score = self.count_table_cards()
            player.points = score
            print("{} tu puntuación es de {} puntos.".format(player.name, score))
            self.table_cards.clear()

    def start_turn(self):
        pass

    def select_winner(self):
        self.players.sort(key=lambda player: player.points, reverse=True)
        print("El ganador es {} con {} puntos!!".format(self.players[0].name, self.players[0].points))


if __name__ == '__main__':
    blackjack = Game()
    blackjack.run()
    blackjack.select_winner()
