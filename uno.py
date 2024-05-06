import random

# Kartları ve renkleri temsil eden sabitler
COLORS = ['Red', 'Blue', 'Green', 'Yellow']
VALUES = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9','Reverse', 'Skip', 'Draw Two']
WILD_CARDS = ['Wild', 'Wild Draw Four']
class UnoPlayer:
    def __init__(self, name):
        self.name = name
        self.hand = []


    def play_turn(self, top_card):
        valid_cards = [card for card in self.hand if card[0] == top_card[0] or card[1] == top_card[1]]
        if not valid_cards:
            print("No valid cards. Drawing from deck.")
            self.draw_cards(1)
            return None
        else:
            print("Your valid cards:", valid_cards)
            while True:
                try:
                    choice = int(input("Choose the index of the card to play: "))
                    if 0 <= choice < len(valid_cards):
                        played_card = self.hand.pop(choice)
                        return played_card
                    else:
                        print("Invalid choice. Please choose a valid index.")
                except ValueError:
                    print("Invalid input. Please enter a valid index.")

    def draw_cards(self, num_cards):
        for _ in range(num_cards):
            self.hand.append(game.deck.pop())

class UnoGame:
    def __init__(self, players):
        self.players = players
        self.deck = self.generate_deck()
        self.discard_pile = []
        self.current_player_index = 0
        self.direction = 1

    def generate_deck(self):
        deck = [(color, value) for color in COLORS for value in VALUES * 2]
        deck += [(color, value) for color in COLORS for value in WILD_CARDS]
        random.shuffle(deck)
        return deck

    def next_player(self):
        self.current_player_index = (self.current_player_index + self.direction) % len(self.players)

    def play(self):
        # Oyunculara başlangıç eli dağıtılır
        for _ in range(7):
            for player in self.players:
                player.hand.append(self.deck.pop())

        # İlk kart çekilir ve oyun başlar
        self.discard_pile.append(self.deck.pop())

        while True:
            current_player = self.players[self.current_player_index]
            print(f"\n{current_player.name}'s turn:")
            print(f"Current Card: {self.discard_pile[-1]}")
            print(f"Your Hand: {current_player.hand}")

            # Oyuncu kart oynar
            played_card = current_player.play_turn(self.discard_pile[-1])

            # Oyuncunun elindeki kartlar kontrol edilir
            
            # Bir sonraki oyuncuya geçiş yapılır
            if len(current_player.hand) == 0:
                print(f"\n{current_player.name} wins!")
                break
            elif played_card is None:
                pass  # Oyuncu çekmek zorunda kaldı, bir sonraki oyuncuya geçiş yapılır
            elif played_card[1] == "Draw Two":
                self.next_player()
                self.players[self.current_player_index].draw_cards(2)
            elif played_card[1] == "Wild Draw Four":
                self.next_player()
                self.players[self.current_player_index].draw_cards(4)
            else:
                self.next_player()

# Oyuncular oluşturulur
player1 = UnoPlayer("Player 1")
player2 = UnoPlayer("Player 2")

# Oyun başlatılır
game = UnoGame([player1, player2])
game.play()