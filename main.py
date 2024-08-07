############### Our Blackjack House Rules #####################
## The deck is unlimited in size. 
## There are no jokers. 
## The Jack/Queen/King all count as 10.
## The the Ace can count as 11 or 1.
## Use the following list as the deck of cards:
## cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
## The cards in the list have equal probability of being drawn.
## Cards are not removed from the deck as they are drawn.
## The computer is the dealer.

##################### Hints #####################


import random
from replit import clear
from blackjack_art import logo


def deal_card():
    """Returns a random card from the deck."""
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card = random.choice(cards)
    return card

#Hint 3: Create a function called calculate_score() that takes a List of cards as input 
#and returns the score. 
#Look up the sum() function to help you do this.
def calculate_score(cards):
    #Hint 4: Inside calculate_score() check for a blackjack (a hand with only 2 cards: ace + 10) and return 0 instead of the actual score. 0 will represent a blackjack in our game.
        if sum(cards) ==21 and len(cards) == 2: # if sum of two cards is 21, where one is 10 and another is 11 (Ace)
            return 0 

    #Hint 5: Inside calculate_score() check for an 11 (ace). If the score is already over 21, remove the 11 and replace it with a 1. You might need to look up append() and remove().    
        if 11 in cards and sum(cards) > 21:
            cards.remove(11) # remove() function will remove the first occurrence of the item 11 in the list cards
            cards.append(1) # append() function will add the item 1 to the list cards

        return sum(cards) # sum() function will add all the items in the list cards and return the sum
        """Take a list of cards and return the score calculated from the cards"""

#Hint 10: Create a function called compare() and pass in the user_score and computer_score. If the computer and user both have the same score, then it's a draw. If the computer has a blackjack (0), then the user loses. If the user has a blackjack (0), then the user wins. If the user_score is over 21, then the user loses. If the computer_score is over 21, then the computer loses. If none of the above, then the player with the highest score wins.
def compare(user_score, computer_score):
    if user_score == computer_score:
        return "Draw 👍"
    elif computer_score == 0:
        return "Lose, opponent has Blackjack 😒 "
    elif user_score == 0:
        return "Win with a Blackjack 😍"
    elif user_score > 21:
        return "You went over. You lose 😭"
    elif computer_score > 21:
        return "Opponent went over. You win 😎"
    elif user_score > computer_score:
        return "You win 😁"
    else:
        return "You lose 😤"

# creating a function called play_game() which contain everything till compare to use it later on for restarting the game
def play_game():
    print(logo) # printing logo from art file

    #Hint 2: Deal the user and computer 2 cards each using deal_card() and append().
    user_cards = []
    computer_cards = []
    is_game_over = False # creating a variable is_game_over and setting it to False to end the game

    # using for loop to append 2 cards to each list
    for _ in range(2):
        user_cards.append(deal_card()) # It'll add the random card to the user_cards list
    # we use append() instead of += because we want to add a single item to the list
    # and not a list of items and to do that first we need to extend and after that we can use +=\
        computer_cards.append(deal_card()) # similarly appending the random card in computer card list

    #Hint 8: The score will need to be rechecked with every new card drawn and the checks in Hint 9 need to be repeated until the game ends.
    while not is_game_over:
        #Hint 6: Call calculate_score(). If the computer or the user has a blackjack (0) or if the user's score is over 21, then the game ends.
        user_score = calculate_score(user_cards) # calling the calculate_score function to calculate the score of the user_cards list
        computer_score = calculate_score(computer_cards) # calling the calculate_score function to calculate the score of the user_cards list
        # printing user cards and current score
        print(f"Your cards: {user_cards}, current score: {user_score}")
        # printing computer's first card
        print(f"Computer's first card: {computer_cards[0]}")

        if user_score == 0 or computer_score == 0 or user_score > 21:
            is_game_over = True
        #Hint 7: If the game has not ended, ask the user if they want to draw another card. If yes, then use the deal_card() function to add another card to the user_cards List. If no, then the game has ended.
        else:
            user_should_deal = input("Type 'y' to get another card, type 'n' to pass: ")
            if user_should_deal == "y":
                user_cards.append(deal_card())
            else:
                is_game_over = True

    #Hint 9: Once the user is done, it's time to let the computer play. The computer should keep drawing cards as long as it has a score less than 17.
    while computer_score != 0 and computer_score < 17:
        computer_cards.append(deal_card()) # appending the random card to the computer_cards list
        computer_score = calculate_score(computer_cards) # calling the calculate_score function to calculate the new score of the computer_cards list

    # printing final cards and score of user and computer
    print(f"Your final hand: {user_cards}, final score: {user_score}")
    print(f"Computer's final hand: {computer_cards}, final score: {computer_score}")
    print(compare(user_score, computer_score)) # calling compare() function to compare the user_score and computer_score


#Hint 11: Ask the user if they want to restart the game. If they answer yes, clear the console and start a new game of blackjack and show the logo from art.py.
while input("Do you want to play a game of Blackjack? Type 'y' or 'n': ") == "y":
    clear() #using clear function to clear the console 
    play_game() # calling play_game() function to restart the game
