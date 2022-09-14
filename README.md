# Blackjack

### What it does:

Blackjack is a command-line Python application. It is a game where the user plays Blackjack against the computer. After compiling, the user gets £100 and types the amount to bet, which is doubled in case of winning, or lost in case of losing. Both players get 2 cards, but the user can only see one card from computer's hand. The computer will draw cards until reaching 17 or more. The user can draw as many cards as they want, but in case of exceeding 21, they lose. The player is then asked if they want to play another game or not.

### How I built it:

- I built a function that creates the deck.
- I built a class named Player with 3 attributes: the hand, cards, and amount of money, which are retuned in a message.
- The Player class has functions for initialising the hand, getter and setter for money, functions for drawing a card, betting, and winning.
- I built a print function for computer's hand.
- The game runs until the player quits.

### Challenges I ran into:

I knew how to work in Python, but sometimes I can not remember all the functions I have created and how to properly use them, especially if I take a break before finishing it.

![Blackjack1](https://github.com/tudormihail5/Blackjack/blob/main/Screenshot1.png)

The user bet £20.

![Blackjack2](https://github.com/tudormihail5/Blackjack/blob/main/Screenshot2.png)

The user typed 'y' to draw another card, but then typed 'n' to stop, winning, and having a total of £120.
