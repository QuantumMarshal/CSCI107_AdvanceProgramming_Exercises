"""
Higher or Lower Card Game
------------------------

This program implements a simple command-line card game using object-oriented programming.

Overview:
    The player starts with a set number of credits and is shown a card from a shuffled deck.
    They must guess whether the next card will be higher or lower in value. If the guess is
    correct, the player wins credits; otherwise, they lose credits. The game continues until
    the player runs out of credits or the deck is empty.

Classes used:
    Card:
        Represents a single playing card.
        Stores rank (e.g., Ace, King), suit (e.g., Hearts), and value (numeric).
        Cards can be concealed or revealed, which controls how they are displayed.

    Deck:
        Manages a collection of Card objects.
        Creates a full deck based on a rank-value dictionary.
        Supports shuffling, drawing cards, and returning cards to the deck.
        Maintains two lists:
            - startingDeckList: the original ordered deck
            - playingDeckList: the active shuffled deck used during gameplay

    Game:
        Controls the overall game logic.
        Handles player credits, betting, user input, and win/loss conditions.
        Uses the Deck class to draw and compare cards.

Key Concepts Demonstrated:
    - Classes and objects
    - Constructors (__init__)
    - Magic methods (__str__)
    - Encapsulation (methods controlling state like reveal/conceal)
    - Composition (Game "has a" Deck, Deck "has many" Cards)
    - Input validation and control flow

How to Run:
    Run the script and follow the prompts in the terminal.
    Enter a bet and guess whether the next card will be higher (h) or lower (l).

Note:
    The `window` parameter in the Card and Deck classes is reserved for potential
    future GUI integration but is not used in this version of the program.
"""

import random


class Card:
    """
    This defines the Card class, which represents a single card in the deck with its rank, suit, and value.

    The `window` parameter can be used for GUI integration later
    """
    def __init__(self, rank, suit, value):
        self.__rank = rank
        self.__suit = suit
        self.__value = value
        self.__is_concealed = True


    def __str__(self):
        """
        Returns the card object (i.e. Ace of Hearts) if card not concealed or a message saying such if it is
        """
        if not self.__is_concealed:
            return f'{self.__rank} of {self.__suit}'
        else:
            return f"This card is still concealed."

    def reveal(self):
        # This method reveals the card by setting `is_concealed` to False.
        self.__is_concealed = False

    def conceal(self):
        # This method conceals the card by setting `is_concealed` to True.
        self.__is_concealed = True

    def get_value(self):
        return self.__value

class Deck:
    """
    This class generates a deck of cards by calling the card object.

    We have the ability to generate multiple decks by passing in values used (i.e. we only use cards higher than 6 for certain games)
    """
    # These are class variables that apply to any deck object generated from this class
    SUIT_TUPLE = ('Diamonds', 'Clubs', 'Hearts', 'Spades')
    STANDARD_DECK = {'Ace': 1, '2': 2, '3': 3, '4': 4, '5': 5,
                     '6': 6, '7': 7, '8': 8, '9': 9, '10': 10,
                     'Jack': 11, 'Queen': 12, 'King': 13}

    # The constructor initializes the deck by creating cards for each suit and rank using the given rank-value dictionary.
    def __init__(self):
        self.starting_deck_list = list() # The startingDeckList holds the original un-shuffled deck, which allows resetting the deck if needed.
        for rank, value in Deck.STANDARD_DECK.items():
            for suit in Deck.SUIT_TUPLE:
                self.starting_deck_list.append(Card(rank, suit, value))

        self.playing_deck_list = self.starting_deck_list.copy()  # The playingDeckList is the active deck used during gameplay, which can be shuffled and modified.

    def shuffle(self):
        # This method shuffles the deck and ensures all cards are concealed before shuffling.
        random.shuffle(self.playing_deck_list) # Copy the deck list


    def get_card(self):
        # This method removes and returns the top card from the playing deck. Raises an error if no cards are left.
        card = self.playing_deck_list.pop(0)
        return card


    def return_card_to_deck(self, oCard):
        # This method adds a card back to the top of the playing deck.
        oCard.conceal()
        self.playing_deck_list.insert(0, oCard)


    def print_deck(self):
        for card in self.playing_deck_list:
            print(card)

    def reveal(self):
        for card in self.playing_deck_list:
            card.reveal()

    def count_card(self):
        return len(self.playing_deck_list)

    """
    Counts remaining cards higher or lower the value.
    Tie --> Lose (If you have King and the next one is King --> You lose)
    This uses for calculate probability later.
    """

    def count_higher_lower(self, value):
        higher = 0
        lower = 0

        for card in self.playing_deck_list:
            card_value = card.get_value()

            if card_value > value:
                higher += 1

            elif card_value < value:
                lower += 1

        return higher, lower


class Game:
    def __init__(self):
        # The Game class handles the game logic, including initializing the deck and managing the score.

        pass  # Pass "None" for window as we are not using GUI
        self.credits = 100  # Starting credits for the player
        self.deck = Deck()
        self.deck.shuffle()
        self.current_card = self.deck.get_card()
        self.current_card.reveal()


    def get_bet(self):
        """
        Validates the bet.

        Returns the bet amount or a message saying the bet is invalid
        """
        is_correct = False
        bet = ""

        """
        Have you ever try Ctrl + D for input? This causes EOF error.
        I am trying to figure it.
        """

        while not is_correct:
            try:
                bet = int(input("Enter the bet amount: "))

                if bet <= 0:
                    print("Pls enter the positive integer amount.")
                elif bet > self.credits:
                    print("Pls enter the valid integer amount.")
                else:
                    is_correct = True
            except ValueError:
                print("This is incorrect, pls try again.")

        return bet

    """
    Show the probability to the terminal.
    """

    def show_prob(self):
        card_value = self.current_card.get_value()
        higher, lower = self.deck.count_higher_lower(card_value)
        total = self.deck.count_card()

        if total == 0:
            return

        print(f"Higher wins: {higher}/{total} ({100 * higher / total:.1f}%) | Lower wins: {lower}/{total} ({100 * lower / total:.1f}%)\n")

    def calc_prob_by_choice(self, cmd):
        card_value = self.current_card.get_value()
        higher, lower = self.deck.count_higher_lower(card_value)
        total = self.deck.count_card()

        if cmd == "h":
            return higher / total

        return lower / total

    def calc_bet(self, bet, win_prob):
        # Case 0% win but still choose: --> Lose all the bet credits
        if win_prob <= 0:
            return 1000000000, bet

        """
        Take 50% as a fair situation. 
        --> Less than 50% increase the bet
        --> More than 50% decrease the bet
        
        I use simple linear equation: 
            + win = bet * (50% / win_probability)
            + lose = bet / (50% / win_probability) = bet * (win_probability / 50%)
        
        Based on this equation we can see that highest multiplier can be 25%
        
        [Warning: I do math here you can skip it or double check for me :)]
            + Win situation:
                Worst case: Queen and choose higher and only have 1 King left 
                    Card left: 51-3 (3 Kings) = 48 --> Prob = 1/48 = 2%
                    --> 50/2 = 25 --> Max Mul is 25 --> too high --> Reduced it to 5 by default.
            
            + Lose situation:
                Worst case: King and choose lower and only have 1 King left:
                    Card left: 51 - 2 (2 Kings) = 49 --> Prob = 48/49 = 98%
                    --> 98/50 = 1.96 --> You have many chance to win but still lose
                    --> Lose bet * 1.96 (more than you bet) (I like this one)
                    --> Lose your bet (your actual bet) 
        """

        win = bet * (0.5 / win_prob)
        max_win = bet * 5

        win = int(min(round(win), max_win))

        loss = bet * (win_prob / 0.5)
        min_loss = max(bet / 5, 1)

        # I have 2 version of calculating lose
        # loss = int(max(bet * 0.5, round(bet * (win_prob / Game.NEUTRAL_WIN_PROB))))
        loss = int(min(bet, max(min_loss, round(loss))))

        return win, loss

    def start_game(self):
        """
        This method runs the game logic during the game.
        It manages checking if there is enough cards, revealing cards, checking bets, calculating credits, and ending the game.
        """
        print("Welcome to the Higher or Lower Card Game!")
        print(f"You have {self.credits} credits.")
        print(f"The first card is: {self.current_card}")

        while True:
            if self.deck.count_card() <= 0:# Check if there is any cards left first
                break

            if self.credits <= 0: # Check if there is any credits left
                break

            self.show_prob()

            bet = self.get_bet()

            correct_input = False
            cmd = ""
            while not correct_input: # Validate input to only allow 'h' or 'l'
                cmd = input("Enter higher (h) or lower (l): ")
                if cmd == "h" or cmd == "l":
                    correct_input = True
                else:
                    print("Pls enter the correct input (h/l).")

            win_prob = self.calc_prob_by_choice(cmd)
            win, loss = self.calc_bet(bet, win_prob)

            print(f"Betting system: Win +{win} credits | Lose -{loss} credits\n")

            # Check if correct guess and adjust winnings (credit amount)
            next_card = self.deck.get_card()

            if (cmd == "h" and self.current_card.get_value() < next_card.get_value()) or (cmd == "l" and self.current_card.get_value() > next_card.get_value()):
                next_card.reveal()
                print(f"You are correct. The next card is: {next_card}")
                self.credits += win

            else:
                next_card.reveal()
                print(f"You are incorrect. Worst luck ever. The next card is: {next_card}")
                self.credits -= loss

            print(f"Your credits now is: {self.credits}")


            self.current_card = next_card # Get the next card
            self.current_card.reveal()

        # Show final result
        if self.credits > 0: # Currently will only show 0 because this is displayed only when credits reach 0
            print(f"Your credits is: {self.credits}")
        else:
            print(f"Your credits is 0, you owe me {-self.credits} dollars.")


if __name__ == "__main__":
    my_game = Game() # Create a game object
    my_game.start_game() # Run the game