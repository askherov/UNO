import random

# Kartları ve renkleri temsil eden sabitler
COLORS = ['Red', 'Blue',]
VALUES = ['0', '1', '2',]
WILD_CARDS = ['Wild',]
class UnoPlayer:
    def __init__(self, name):
        self.name = name
        self.hand = []

    def play_turn(self, current_card):
        valid_cards = [(index, card) for index, card in enumerate(self.hand) if card[0] == current_card[0] or card[1] == current_card[1]]
        if not valid_cards:
            print("No valid cards. Drawing from deck.")
            self.draw_cards(1)
            return None
        else:
            print("Your valid cards:")
            for index, card in valid_cards:
                print(f"{index}: {card}")
            choice = int(input("Choose the index of the card to play: "))
            played_card = self.hand.pop(choice)
            return played_card


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


    
#     ||||||
#    \/\/\/\/ 
        for _ in range(2):
            for player in self.players:
                player.hand.append(self.deck.pop())

    # İlk kart çekilir ve oyun başlar
        current_card = self.deck.pop()
        self.discard_pile.append(current_card)

        while True:
            current_player = self.players[self.current_player_index]
            print(f"\n{current_player.name}'s turn:")
            print(f"Current Card: {self.discard_pile[-1]}")
            print(f"Your Hand: {current_player.hand}")

            # Oyuncu kart oynar
            played_card = current_player.play_turn(self.discard_pile[-1])

            # Oyuncunun elindeki kartlar kontrol edilir
            if len(current_player.hand) == 0:
                print(f"\n{current_player.name} wins!")
                break

            # Bir sonraki oyuncuya geçiş yapılır
            if played_card is not None:
                self.discard_pile.append(played_card)
                if played_card[1] == "Reverse":
                    self.direction *= -1
                elif played_card[1] == "Skip":
                    self.next_player()
                elif played_card[1] == "Draw Two":
                    self.next_player()
                    self.players[self.current_player_index].draw_cards(2)
                elif played_card[1] == "Wild Draw Four":
                    self.next_player()
                    self.players[self.current_player_index].draw_cards(4)
                else:
                    self.next_player()
            else:
                # Oyuncu geçerli bir kart oynamadıysa, kart çeker ve sıra bir sonraki oyuncuya geçer
                self.next_player()

# Oyuncular oluşturulur
player1 = UnoPlayer("Player 1")
player2 = UnoPlayer("Player 2")

# Oyun başlatılır
game = UnoGame([player1, player2])
game.play()