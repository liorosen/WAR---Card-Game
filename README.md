## **War Card Game**
Overview
This project is a Python implementation of the classic two-player card game "War." The program employs object-oriented programming (OOP) concepts to simulate deck management, card comparison, and gameplay mechanics.

## **Features**
Dynamic Deck Creation:

A deck of 52 cards is generated with suits and ranks.
Cards are assigned values for comparison during gameplay.
Game Mechanics:

Deck is shuffled and evenly distributed to two players.
Players draw cards and compare their values.
Resolves ties (War) by drawing additional cards.
Interactive Gameplay:

Player names are input dynamically at the start.
Rounds continue until one player runs out of cards.
Technical Highlights
Object-Oriented Design:

Card, Deck, and Player classes encapsulate game components.
Each class focuses on a specific functionality:
Card: Represents individual cards with suits and ranks.
Deck: Manages card shuffling and distribution.
Player: Tracks each player's cards dynamically.
Dynamic Memory and Lists:

Lists are used to manage player hands and the deck of cards.
Extend and pop methods simulate card distribution and play.
Randomization:

Uses Python's random.shuffle for realistic deck shuffling.
