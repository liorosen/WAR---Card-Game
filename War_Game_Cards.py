#!/usr/bin/env python
# coding: utf-8

# In[214]:


import random
suits = ('Spades', 'Hearts' , 'Clubs', 'Diamonds')
ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten'
          , 'Prince', 'Queen', 'King' ,'Ace')
values = {'Two':2 , 'Three':3, 'Four':4, 'Five':5, 'Six':6, 'Seven':7, 'Eight':8, 'Nine':9, 'Ten':10
          , 'Prince':11 , 'Queen':12, 'King':13,'Ace':14}


# In[215]:


class Card:
    
    def __init__(self,suit,rank):
        self.suit = suit
        self.rank = rank    
        self.value = values[rank]

    def getValue(self):
        return self.value
    def __str__(self):
        return self.rank + " of " + self.suit


# In[216]:


class Deck:
    def __init__(self):
        self.all_cards = []
        
        for suit in suits:
            for rank in ranks:
                Created_Card = Card(suit,rank)
                self.all_cards.append(Created_Card)
                
                
    def shuffle(self):
        random.shuffle(self.all_cards)
    
    def get_one_card(self):
        return self.all_cards.pop()


# In[217]:


class Player:
    def __init__(self,name):
        
        self.name = name
        self.all_cards = []
    
    def addCards(self,new_cards):
        if type(new_cards) == type([]):
            self.all_cards.extend(new_cards)
        else:
            self.all_cards.append(new_cards)
    
    def removeCards(self):
         return self.all_cards.pop(0)
    
    def __str__(self):
        return f'Player {self.name} has {len(self.all_cards)} cards.'


# In[218]:


gameOn = True #Both Players has cards
x = input("Please enter Player1 Name" + '\n')
Player1 = Player(x)
y = input("Please enter Player2 Name" +  '\n')
Player2 = Player(y)
TheDeck = Deck()
TheDeck.shuffle()
for i in range(26) :
    Player1.addCards(TheDeck.get_one_card())
    Player2.addCards(TheDeck.get_one_card())

round = 0

while (gameOn):
    round += 1
    print('Round ' + str(round))
    if len(Player1.all_cards) == 0:
        print(Player1 + 'You Lost')
        gameOn = False
        break
    if len(Player2.all_cards) == 0:
        print(Player2 + 'You Lost')
        gameOn = False
        break
        
    Player1_Cards = []
    Player1_Cards.append(Player1.removeCards())
    Player2_Cards = []
    Player2_Cards.append(Player2.removeCards())
        
    War = True
    while War :
        Card1 = Player1_Cards[-1]
        Card2 = Player2_Cards[-1]
        print(Card1)
        print(Card2)
        while Card1.getValue() == Card2.getValue():
            print("It is a draw please draw another card")
            Card1 = Player1_Cards[-1]
            Card2 = Player2_Cards[-1]

        if Card1.getValue() > Card2.getValue() :
            print("This round winner is" + Player1)
            Player1.addCards(Player1_Cards)
            Player1.addCards(Player2_Cards)
            War = False

        elif Card2.getValue() > Card1.getValue():
            print("This round winner is" + Player2)
            Player2.addCards(Player1_Cards)
            Player2.addCards(Player2_Cards)
            War = False

