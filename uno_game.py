import random

# 1 Card class
# 2 Deck class
# 3 Player class
# 4 Game class

COLORS = ["Red", "Yellow", "Blue", "Green"]
NUMBERS = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']#,'Reverse', 'Skip', 'Draw Two'


class Card:
    def __init__(self,color,number) -> None:
        self.color = color
        self.number = number

class CardDeck:
    def __init__(self) -> None:
       self.cards = [Card(color, number) for color in COLORS for number in NUMBERS]

    def deck_shuffle(self):
        random.shuffle(self.cards)

    def first_card(self, ):
        return self.cards.pop()
   
class Player:
    def __init__(self,name) -> None:
        self.name = name
        self.hand = []
    
    def draw(self, deck, num_cards=1):
        for x in range(num_cards):
            self.hand.append(deck.first_card())
    
    def show_hand(self):
        for card in self.hand:
            print(f"{self.hand.index(card) + 1}. {card.color} {card.number}")           

class Game:
    def __init__(self, *players) -> None:
        self.index =0
        self.deck = CardDeck()
        self.players = [Player(name) for name in players]
        # self.current_card = self.deck.first_card

    def next_player(self):
        self.index = (self.index + 1) % len(self.players)

    def start_game(self):
        for player in self.players:
            player.draw(self.deck, 7)

    def check(self, card,current_card):
        if card.color == self.current_card.color or card.number == self.current_card.number:
            return True
        return False

    def play(self):
        self.deck.deck_shuffle()
        self.start_game()
        self.current_card = self.deck.cards.pop()
        while True:
            players_index = self.players[self.index]
            print(self.current_card.color,self.current_card.number)
            print(f"{players_index.name}")
            players_index.show_hand()
            while True:
                choise = int(input("Enter card number (0 is draw a card): "))
                
                if choise==0:
                    players_index.draw(self.deck)
                    players_index.show_hand()
                    continue
                elif self.check(players_index.hand[choise-1],self.current_card):
                    self.current_card= players_index.hand[choise-1]
                    del players_index.hand[choise-1]
                    break
                else:
                    print("You can't play this card! Please choose another card")
                    print(f"Curent card: {self.current_card.color, self.current_card.number}")

            if len(players_index.hand) == 0:
                print(f'{players_index} Win game !')
                break
            self.next_player()

game = Game('a', 'b')
game.play()







        

