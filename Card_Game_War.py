
import random

suits = ('\u2665', '\u2666', '\u2663', '\u2660')
ranks = ('2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A')
values = {'2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8, '9':9, 
          '10':10, 'J':10, 'Q':10, 'K':10, 'A':11}

player = None
war = []


# DEFINING CARD CLASS

class Card:
    
    def __init__(self, suit, rank):
        
        self.suit = suit
        self.rank = rank
        self.value = values[rank]
        
    def __str__(self):
        return self.rank + self.suit



# DEFINING DECK CLASS

class Deck:
    
    def __init__(self):
        
        self.all_cards = []
        self.deck1 = []
        self.deck2 = []
        self.splited_decks = (self.deck1, self.deck2)
        
        for suit in suits:
            for rank in ranks:
                
                new_card = Card(suit, rank)
                self.all_cards.append(new_card)
    
    def shuffle_deck(self):
        
        random.shuffle(self.all_cards)
        
    def deck_split(self):
        
        i = 1
        
        for card in self.all_cards:
            if i % 2 == 0:
                self.deck2.append(card)
            else:
                self.deck1.append(card)
            i += 1


# DEFINING PLAYER CLASS

class Player:
    
    def __init__(self, name):
        
        self.player_cards = None
        self.name = name
        
    def __str__(self):
        
        return self.name
        
    def take_cards(self, deck):
        
        self.player_cards = deck



# WELCOME SCREEN FUNCTION

def welcome():
    
    print('Welcome to card game WAR')
    print(' ')
    print(' ')
    print('Do you wnt to proceed to the game?')
    print(' ')
    print(' ')
    
    answer = 'wrong'
    
    while answer not in ['y','n']:
        answer = input("Ready for new game (y/n): ")
        print(answer)
        if answer not in ['y','n']:
            print("Pls type in y or n (ne zamaraj me)")
            
    if answer == 'y':
        return True
    elif answer == 'n':
        return False



# NEPOTREBNA FUNKCIJA AL JEBIGA OSTALA JE

def player1_name():
    
    global player
    
    player = input("Player1 pls enter your name: ")


# I OVA ISTO

def player2_name():
    
    global player
    
    player = input("Player2 pls enter your name: ")


# JAKO POTREBNA FUNKCIJA ( DA NE KAZEM KLJUCNA ! :D)

def procced():
    
    print(input('Press Enter to continue'))



''' 
IN THIS MOVE FUNC WE HAVE:

- showing players cards (cards they play on that move)
- "throwing" cards on table (pop cards from players_cards and put cards in list "table")
- determening which player has higher card and who wins round (value of Card)
- every time winner of round checks list war and collect cards from that list
if there was a war, player who wins will collect all cards
- if players have same value of card, functon play_war will be called



'''
def move():
    
    table = []
    
    print(' ')
    print(' ')
    print('Play next move?')
    procced()
    
    print(' ')
    print(' ')
    print(Player1.name + ' played: ' + str(Player1.player_cards[0]))
    table.append(Player1.player_cards.pop(0))
    print(' ')
    print(Player2.name + ' played: ' + str(Player2.player_cards[0]))
    table.append(Player2.player_cards.pop(0))
    
    if table[0].value > table[1].value:
        
        while len(war) != 0:
            Player1.player_cards.append(war.pop(0))
            
            
        Player1.player_cards.append(table.pop(0))

        Player1.player_cards.append(table.pop(0))
        
        
        print(' ')
        print(' ')
        print(Player1.name + ' wins this round')
        
    elif table[1].value > table[0].value:
        
        while len(war) != 0:
            Player2.player_cards.append(war.pop(0))
            
        
        Player2.player_cards.append(table.pop(0))
        
        Player2.player_cards.append(table.pop(0))
        
        print(' ')
        print(' ')
        print(Player2.name + ' wins this round')
        
    else:
        play_war(war, table)


# POPING CARDS FROM PLAYERS LISTS AND PUTING THEM IN WAR LIST

def play_war(war, table):
    
    print(' ')
    print(' ')
    print('WAR ! ! ! :D')
    
    procced()
    
    print(' ')
    print('Players put 3 cards each on table')
    
    procced()
    
    war.append(table.pop(0))
    war.append(table.pop(0))
    
    if len(Player1.player_cards) == 3 or len(Player2.player_cards) == 3:
        
        war.append(Player1.player_cards.pop(0))
        war.append(Player1.player_cards.pop(0))
        war.append(Player2.player_cards.pop(0))
        war.append(Player2.player_cards.pop(0))
        return war
    
    elif len(Player1.player_cards) == 2 or len(Player2.player_cards) == 2:
        
        war.append(Player1.player_cards.pop(0))
        war.append(Player2.player_cards.pop(0))
        return war
    
    elif len(Player1.player_cards) == 1 or len(Player2.player_cards) == 1:
    
        return war
    
    else:
        
        war.append(Player1.player_cards.pop(0))
        war.append(Player1.player_cards.pop(0))
        war.append(Player1.player_cards.pop(0))
        war.append(Player2.player_cards.pop(0))
        war.append(Player2.player_cards.pop(0))
        war.append(Player2.player_cards.pop(0))
        return war


# SHOWING SCORE DURING GAME

def score():
    
    print(' ')
    print('CURRENT SCORE:')
    print(' ')
    print(' ')
    print(Player1.name + ' have ' + str(len(Player1.player_cards)) + ' cards left')
    print(' ')
    print(Player2.name + ' have ' + str(len(Player2.player_cards)) + ' cards left')




# MAIN PROGRAM

if welcome() == False:
    
    print(' ')
    print(' ')
    print('Tnx for playing')
    
else:
    # Creating deck
    
    new_deck = Deck()
    
    # Shuffling deck
    
    print(' ')
    print(' ')
    print('Procced to deck shufflingy?')
    procced()
    new_deck.shuffle_deck()
    
    # Spliting deck
    
    new_deck.deck_split()
    
    # Request player1 name
    
    print(' ')
    print(' ')
    player1_name()
    
    # Creating player1
    
    Player1 = Player(player)
    
    # Request player2 name
    
    print(' ')
    print(' ')
    player2_name()
    
    # Creating player2
    
    Player2 = Player(player)
    
    # Dealing cards to players
    
    print(' ')
    print(' ')
    print('Deal cards to players?')
    procced()
    Player1.take_cards(new_deck.deck1)
    Player2.take_cards(new_deck.deck2)
    
    # Start game
    
    print(' ')
    print(' ')
    print('Ready to start the game?')
    procced()
    
    # MAIN GAME
    
    
    while len(Player1.player_cards) != 0 and len(Player2.player_cards) != 0:
        
        score()
        move()
    
    if len(Player1.player_cards) == 0:
        
        print(' ')
        print('Game is over!')
        print(' ')
        print('WINNER IS: ' + str(Player2.name) + ' ! ! !' )
        print(' ')
        print('CONGRATULATIONS ! ! !')
        
    if len(Player2.player_cards) == 0:
        
        print(' ')
        print('Game is over!')
        print(' ')
        print('WINNER IS: ' + str(Player1.name) + ' ! ! !' )
        print(' ')
        print('CONGRATULATIONS ! ! !')