## **War Card Game**
<ins> ## **Overview** </ins>
This project is a Python implementation of the classic two-player card game "War." The program employs object-oriented programming (OOP) concepts to simulate deck management, card comparison, and gameplay mechanics.

## **Features**
<ins>Dynamic Deck Creation:</ins><br>
A deck of 52 cards is generated with suits and ranks.<br>
Cards are assigned values for comparison during gameplay.<br>

<ins>Game Mechanics: </ins><br>
Deck is shuffled and evenly distributed to two players.<br>
Players draw cards and compare their values.<br>
Resolves ties (War) by drawing additional cards.<br>

<ins>Interactive Gameplay:</ins><br>
Player names are input dynamically at the start.<br>
Rounds continue until one player runs out of cards.<br>

Technical Highlights
<ins>Object-Oriented Design:</ins>
Card, Deck, and Player classes encapsulate game components.<br>
Each class focuses on a specific functionality:<br>
Card: Represents individual cards with suits and ranks.<br>
Deck: Manages card shuffling and distribution.<br>
Player: Tracks each player's cards dynamically.<br>

<ins>Dynamic Memory and Lists:</ins><br>
Lists are used to manage player hands and the deck of cards.<br>
Extend and pop methods simulate card distribution and play.<br>
<ins>Randomization: </ins>Uses Python's random.shuffle for realistic deck shuffling.
