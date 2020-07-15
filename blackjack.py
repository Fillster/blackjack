from enum import Enum
import random

class Ranks(Enum):
    Ace   = 1
    Two   = 2
    Three = 3
    Four  = 4
    Five  = 5
    Six   = 6
    Seven = 7
    Eight = 8
    Nine  = 9
    Ten   = 10
    Jack  = 11
    Queen = 12
    King  = 13


class Suits(Enum): 
    Club    = 1
    Diamond = 2
    Heart   = 3
    Spades  = 4

running = True
deck = []

class Card:
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank




def createDeck():
    for suit in Suits:
        for rank in Ranks:
            deck.append(Card(suit, rank))
        random.shuffle(deck)


class Player:
    def __init__(self, name):
        self.name = name
        self.playerHand = []
        self.score = 0

    def displayHand(self):
        for x in self.playerHand:
            print("Kort :", x.rank.name, x.suit.name)
        print("dina poäng är: ", self.score)

    def drawCardFromDeck(self):
        self.playerHand.append(deck[0])
        self.score += deck[0].rank.value
        deck.remove(deck[0])

    def isPlayerBust(self):
        if self.score > 21:
            return False
        else:
            return True
        

while running:
    createDeck()


    print("Welcome to black jack")
    print("What is your name?")
    playerName = input()
    player1 = Player(playerName)
    ai = Player("AI")


    player1.drawCardFromDeck()
    player1.drawCardFromDeck()

    ai.drawCardFromDeck()
    ai.drawCardFromDeck()

    running = player1.isPlayerBust()

    player1.displayHand()

    while playing:
        print("VIll du dra ett till kort?")
        playerInput = input()
        if playerInput == "yes":
            player1.drawCardFromDeck()
            running = player1.isPlayerBust()

        player1.displayHand()

        ai.displayHand()
        if ai.score >= 17:
            ai.drawCardFromDeck()

        ai.displayHand()

    

print("Game Over!")