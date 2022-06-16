##### Simple Blackjack Game ##### 
### This is a simplified blackjack game. Player will play against the computer (Dealer).
### Player starts with 50 chips and can choose the amount to bet.
### After dealing out the initial 2 cards, computer will only reveal one of the cards while player will reveal both cards. 
### Player can then choose whether to surrender (lose half of the chips) or double the bet.
### Then player will be able to choose to hit another card or stay with current card.
### After player's turn is over (player chooses to stay with current hand), dealer will start drawing cards if player has not busted.
### If player busts, all bet goes to dealer.
### Dealer continues to draw until it reaches 17 points or busts.
### The goal is to get as close to 21 as possible without busting. Winning against Dealer will get you double the chips.
### After each round, if player still has chips left to bet, player can choose whether to play another game.
##### Note that Ace can count as 1 or 11. The logic automatically adjusts the Ace value.
##########################################################################################################################################
### Author: Clare Ku
### Date Started: June 14, 2022
### Date Completed: June 16, 2022
##########################################################################################################################################


# Import the Random library
import random
import math

# Create global variables for the game:
suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')
values = {'Two':2, 'Three':3, 'Four':4, 'Five':5, 'Six':6, 'Seven':7, 'Eight':8, 
            'Nine':9, 'Ten':10, 'Jack':10, 'Queen':10, 'King':10, 'Ace':11}


# Define Card class:
class Card:
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank
        
        # Assign card value for all cards. Players will be asked about Ace value later, too.:
        self.value = values[rank]
    
    # Define what the string representation of the card is:
    def __str__(self):
        return self.rank + ' of ' + self.suit + ' = ' + str(self.value) + ' points.'


# Define Deck class:
class Deck:
    
    #Creat deck of 52 cards in order:
    def __init__(self):
        # empty list to hold the deck
        self.play_deck = []
        
        # create the deck of 52 cards:
        for suit in suits:
            for rank in ranks:
                self.play_deck.append(Card(suit, rank))
                #print(f"Creating {rank} of {suit}. There are {len(self.play_deck)} cards in the deck.")
        
    # create method to shuffle the deck:
    def shuffle(self):
        random.shuffle(self.play_deck)
        
    # deal one card:
    def deal_one(self):
        return self.play_deck.pop()


# Define player class. Each player starts with 50 chips and no card:
class Player:
    def __init__(self, name):
        self.hand = []
        self.name = name
        self.chips = 50
        self.total_pt = 0
        self.betting = 0
        self.ace_ct = 0
        self.bust = 0
    
    
    # define string representation of the player:
    def __str__(self):
        return f'{self.name} has {self.chips} chips left and holds {len(self.hand)} cards with a sum of {self.total_pt} points, with {self.betting} chips on the table.'
    
    
    # define how to display player hand:
    def show_hand(self):
        print(f"\n{self.name} has the following cards: ")
        for card in self.hand:
            print(f"{card.rank} of {card.suit} = {card.value} points. ")
        print(f"{len(self.hand)} cards in total amouting to {self.total_pt} points.")
    
    
    # define action of drawing one card:
    def hit(self, new_card):
        self.hand.append(new_card)
        self.total_pt += new_card.value
        
        # Keep track of total number of Aces that count for 11 points.
        if new_card.rank == 'Ace':
                self.ace_ct+=1
    
        
        # Adjust the value of Aces as needed and check whether player has busted:
        if self.total_pt > 21:
            if self.ace_ct == 0:
                self.bust = 1
                return f'Bust!! {self.name} has {self.total_pt} points and {self.ace_ct} Aces counting for 11.'
            
            else:
                for card in self.hand:
                    if card.rank == 'Ace' and card.value == 11 and self.total_pt > 21:
                        self.ace_ct -= 1 #Decrease the number of Aces that count as 11
                        self.total_pt -= 10 #Decrease the total number of points
                        card.value = 1 # Set the card value of this Ace to 1
                    
                    elif self.total_pt <= 21:
                        return f'{self.name} has {self.total_pt} points and {self.ace_ct} Aces counting for 11.'
                    
                    elif self.total_pt > 21 and self.ace_ct == 0:
                        self.bust = 1
                        return f'Bust!! {self.name} has {self.total_pt} points and {self.ace_ct} Aces counting for 11.'
    
    
    
    # define betting action:
    def bet(self):
        amt = input('\nHow much would you like to bet in this game of black jack? ')
        
        while amt.isnumeric() == False or int(amt) <= 0 or int(amt) > self.chips:
            print(f'\n\nCurrently you have {self.chips} chips.')
            amt = input('How much would you like to bet? Please enter a whole number smaller or equal to than the chip amount you have. You must bet at least 1 chip. ')
            
        self.chips -= int(amt)
        self.betting += int(amt)


# Game Logic:
def simple_black_jack():
    # Global variables:
    surrender = 0
    game_on = 1
    game_ct = 1
    stay_hand = 0

    # First create the deck and shuffle it:
    playdeck = Deck()
    playdeck.shuffle()

    # Asks player for name to create player class:
    name = input('\nHi, player. What is your name? ')
    player1 = Player(name)

    # Create computer dealer:
    dealer = Player('Dealer')

    # Asks player how much they would like to bet:
    print(f'\nYou start with 50 chips.')
    player1.bet()                     

    # Take turn to deal two cards each to player and dealer. Starting with player.
    for count in (1,2):
        player1.hit(playdeck.deal_one())
        dealer.hit(playdeck.deal_one())

    # Show all but one of dealers cards.
    print("\nDealer's hand:")
    print("*** Hidden Card ***")
    print(f"{dealer.hand[1]}")

    # Show all player cards.
    print("\nPlayer's hand:")
    print(f"{player1.hand[0]}")
    print(f"{player1.hand[1]}")




    while game_on == 1:
        print(f'\nThis is game #{game_ct}.')

        # Check if any player has busted or chosen to surrender. 
        if surrender == 0 and player1.bust == 0 and stay_hand == 0:
            # If not, asks player if he/she wants to surrender.
            surrender_game = input('Would you like to surrender? If you surrender, you will lose half of the chips you bet rounded up to the nearest whole number. (Y/N)')

            while surrender_game not in ('Y', 'N', 'y', 'n'):
                surrender_game = input('Would you like to surrender? Please enter "Y" for yes or "N" for no.')

        # Close game or continue depending on whether player choses to surrender:
        if surrender_game in ('Y', 'y'):
            surrender = 1
            print('You have chosen to surrender. Half of the chips you bet will be deducted.')
        else:
            print('The game will continue.')


        # If not, asks if player wants to double the bet if they have enough chips to double.
        if player1.betting <= player1.chips and surrender == 0:
            double = input('Would you like to double the bet? (Y/N): ')

            while double not in ('Y', 'N', 'y', 'n'):
                double = input('Would you like to double the bet? Please enter "Y" for yes or "N" for no.')

            # Recalculate bet amount base on player response:
            if double in ('Y', 'y'):
                player1.chips -= player1.betting
                player1.betting *= 2
            print(f'You chose to bet {player1.betting} for this game.')
        elif surrender == 0:
        	print(f'You chose to bet {player1.betting} for this game.')
        else:
        	pass

        


        # Asks player if he/she wants to hit and continue to deal cards until player decides to stay. 
        # Continue to deal until player choose to stay hand.
        while player1.total_pt <= 21 and surrender == 0:
            choice = input('\nWould you like to hit or stay? Enter "H" for hit and "S" for stay. ')

            while choice not in ('H', 'S', 'h', 's'):
                choice = input('\nWould you like to hit or stay? Enter "H" for hit and "S" for stay. ')

            # Deal more cards as 
            if choice in ('H', 'h'):
                player1.hit(playdeck.deal_one())

                print("\n\nThis is your current hand:")
                player1.show_hand()
            else:
                stay_hand = 1
                print('\n\nYou have chosen to stay hand. This is your current hand:')
                player1.show_hand()
                break

        # Check if player has busted:
        if surrender == 0 and player1.total_pt > 21:
            player1.bust = 1
            print(f"Bust!! {player1.name} has {player1.total_pt} points and {player1.ace_ct} Aces counting for 11.")
        else:
            pass



        # Check if dealer has busted.
        while dealer.total_pt <= 21 and player1.bust == 0 and surrender == 0:
            # Deal to computer dealer until reaches 17 points or bust. Computer dealer only chooses Ace = 11 if current amount <= 10.
            while dealer.total_pt < 17:
                dealer.hit(playdeck.deal_one())
                print("\n ")
                dealer.show_hand()
            else:
                break

        if dealer.total_pt > 21 and player1.bust == 0 and surrender == 0:
            print(f"Bust!! Dealer has {dealer.total_pt} points and {dealer.ace_ct} Aces counting for 11.")
            dealer.bust = 1


        # If neither has busted. Compare which is closer to 21 to determine winner.
        if dealer.bust == 0 and player1.bust == 0 and surrender == 0:  
            print('\n\nHere are the final cards for each player: ')
            player1.show_hand()
            dealer.show_hand()

            if dealer.total_pt > player1.total_pt:
                print('\nDealer has won. All player bet will go to dealer.')
            elif dealer.total_pt < player1.total_pt:
                print('\nPlayer has won. Player will receive twice of bet.')
            else:
                print("\nDraw. Player bet will be returned to player.")


        # Deal out winnings/ losses of chips.
        if surrender == 1:
            player1.chips += math.floor(player1.betting/2)
        elif dealer.bust == 1:
            player1.chips += player1.betting*2
        elif player1.bust == 1:
            pass
        elif dealer.total_pt > player1.total_pt and dealer.bust == 0:
            pass
        elif dealer.total_pt < player1.total_pt and player1.bust == 0:
            player1.chips += player1.betting*2
        else:
            player1.chips += player1.betting

        print(f"\nGame over. {player1.name} has {player1.chips} chips.")


        # Check if player still has chips.
        # Quit game if no chip left.
        if player1.chips <= 0:
            game_on = 0
            print('\nYou do not have any chip left to play. The game will exit.')
            break

        # If has chips, asks if player wants to play again.
        else:
            go_on = input('\nWould you like to play another game? Enter "Y" for yes or "N" for no. ')

            while go_on not in ('Y', 'N', 'y', 'n'):
                go_on = input('\nWould you like to play another game? Enter "Y" for yes or "N" for no. ')


        # Exit game if player choose to quit. Otherwise reset the game.
        if go_on in ('N', 'n'):
            game_on = 0
            print('Exiting the game.')
            break
        else:
            game_ct += 1
            surrender = 0
            stay_hand = 0

            # Reset the game but retain the number of chips:
            playdeck = Deck()
            playdeck.shuffle()

            player1.hand = []
            player1.total_pt = 0
            player1.betting = 0
            player1.ace_ct = 0
            player1.bust = 0

            dealer.hand = []
            dealer.total_pt = 0
            dealer.betting = 0
            dealer.ace_ct = 0
            dealer.bust = 0

            # Clear prior output
            from IPython.display import clear_output
            clear_output()

            print('\nStarting another game.')
            print(f'{player1.name} has {player1.chips} chips right now.')

            player1.bet()

            # Take turn to deal two cards each to player and dealer. Starting with player.
            for count in (1,2):
                player1.hit(playdeck.deal_one())
                dealer.hit(playdeck.deal_one())

            # Show all but one of dealers cards.
            print("\nDealer's hand:")
            print("*** Hidden Card ***")
            print(f"{dealer.hand[1]}")

            # Show all player cards.
            print("\nPlayer's hand:")
            print(f"{player1.hand[0]}")
            print(f"{player1.hand[1]}")


# Run game
simple_black_jack()
