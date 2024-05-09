import random

# 1 kard clasi
# 2 player calsi
# 3 deste calsi
# 4 oyun mentiqi clasi

class Card:
    def __init__(self,color,number) -> None:
        self.color = color
        self.number = number

class CardDeck:
    def __init__(self) -> None:
        self.colors = ["Qırmızı", "Sarı", "Mavi", "Yaşıl"]
        self.numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']#,'Reverse', 'Skip', 'Draw Two'
        self.cards = [Card(color, number) for color in self.colors for number in self.numbers]
    """
    Kartlari qarışdırmaq funksiyası:
    Parametrlər : None
    Return : None
    """
    def deck_shuffle(self):
        random.shuffle(self.cards)

    """
    Ilk karti secmek:
    Parametrlər : None
    Return : kart
    """
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

    def check(self, kart,current_card):
        if kart.color == self.current_card.color or kart.number == self.current_card.number:
            return True
        else: return False

    def play(self):
        self.deck.deck_shuffle()
        self.start_game()
        self.current_card = self.deck.cards.pop()
        while True:
            print(self.current_card.color,self.current_card.number)
            print(f"{self.players[self.index].name}in sırasıdır !")
            self.players[self.index].show_hand()
            while True:
                choise = int(input("Enter card number (0 is draw a card): "))
                if choise==0:
                    self.players[self.index].draw(self.deck)
                    self.players[self.index].show_hand()
                    continue
                elif self.check(self.players[self.index].hand[choise-1],self.current_card):
                    self.current_card= self.players[self.index].hand[choise-1]
                    del self.players[self.index].hand[choise-1]
                    break
                else:
                    print("You can't play this card! Please choose another card")
                    print(f"Curent card: {self.current_card.color, self.current_card.number}")

            if len(self.players[self.index].hand) == 0:
                print(f'{self.players[self.index]} Win game !')
                break
            self.next_player()

game = Game('a', 'b')
game.play()







        

