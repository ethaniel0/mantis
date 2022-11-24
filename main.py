from itertools import combinations
import random
from pprint import pprint
from mantisPlayer import MantisPlayer


colors = ['PINK', 'RED', 'ORANGE', 'YELLOW', 'GREEN', 'BLUE', 'PURPLE']

class Card:
    def __init__(self, color, back):
        self.color = color  # one color as a number
        self.back = back    # three possible colors the card could be

class Deck:
    def __init__(self):
        self.cards = []
        for i in combinations(range(7), 3):
            for j in range(3):
                self.cards.append(Card(i[j], i))

        random.shuffle(self.cards)
    
    def deal(self):
        return self.cards.pop()
    
    def topColors(self):
        return self.deck[-1].back

class MantisGame:
    def __init__(self, num_players):
        self.num_players = num_players
        self.players = []
        self.hands = []
        self.collected = [0]*num_players
        self.turn = 0
        self.cur_player = 0

        # give everyone a hand
        for _ in range(num_players):
            self.hands.append([0]*7)
            self.players.append(MantisPlayer())
        
        # deal the deck
        self.deck = Deck()
        for _ in range(4):
            for j in range(num_players):
                card = self.deck.deal()
                self.hands[j][card.color] += 1
    
    def isOver(self):
        for i in range(self.num_players):
            if self.collected[i] >= 10:
                return i + 1
        return False

    def play(self):
        while True:
            # check if the game is over
            if self.isOver():
                break

            # get the top card
            top = self.deck.topColors()

            result = self.players[self.cur_player].play(top, self.cur_player, self.hands, self.collected)

            if result == -1: # go for score
                pass
            else: # steal from the result index
                pass

            # increment the turn
            self.turn += 1
            self.cur_player = self.turn % self.num_players

game = MantisGame(4)