# Matthew Greenbaum 

import random

"""
(a) What is the program?
    This is a black jack game using methods we have discussed in class. The playing cards will
    consist of four decks of cards, and the user will be playing against the simulated dealer.
    At the start of the game the player will have ten simulated dollars. The game continues to
    play until the user looses all of his/her cash. Every twenty hands the deck will be reshuffled.

(b) Why did we chose to make the program?
    Both of us enjoy playing card games and thought it would be fun to try to code a black jack
    game. Black jack was a great option because we were able to use many tools and methods we
    learned in class.
    
(c) This program runs relatively easily. The main functions calls the function deal_hand that
    retrieves the first twocards for the user and dealer while removing the specific cards from
    the deck list. The code then checks to see if a user has a black jack and the dealer does not.
    If the user was not delt a black jeack, the user has to input if he/she would like to double
    down with their hand. If they decide to double down they are delt one more card and then the
    dealer function is called to finish dealing the dealers hand. Doubling down means that the user
    is waging $4 for that hand instead of $2. If the user doesn't double down, the player_options
    function is called, which asks the user if they want to hit or stand repeatedly for the hand
    unter they say stand or the card count is above 21. Next the function results is called, which
    prints to let the user know if they won or lost the hand and also adds or subtracts money to
    the users account.
"""


def deal_hand(deck):
    """This function accepts a list, the deck of cards, as a parameter. The function returns
    the hand delt from the deck and the deck without those cards."""
    
    hand = []
    for i in range(2):
        x = random.randint(0, len(deck) - 1)
        card = deck.pop(x)
        hand.append(card)
    return [hand, deck]

def dealer(dealer_hand, deck):
    """This fucntion accepts two lists, dealers hand and the deck of cards. The function
    returns the new deck and new dealer hand after it is greater than or equal to 21."""
    
    print()
    print("The dealer is showing: " + str(dealer_hand[0]) + " and " + str(dealer_hand[1]))
    while hand_total(dealer_hand) < 17:
        x = random.randint(0, len(deck) - 1)
        card = deck.pop(x)
        dealer_hand.append(card)
        print()
        print("Dealer draws: " + str(card))
    return [dealer_hand, deck]

def player_option(player_hand, deck, bet):
    """This function takes three parameters, a list comprised of the users hand, a list containing
    the deck of cards, and an integer for the bet amount. The function will prompt the user to either
    hit or stand with their hand and returns the new hand."""
    
    count = hand_total(player_hand)
    print("Your hand count right now is " + str(count))
    if bet == 4:
        x = random.randint(0, len(deck) - 1)
        card = deck.pop(x)
        player_hand.append(card)
        print("You draw: " + str(card))
        count = hand_total(player_hand)
        print("Your hand count is now " + str(count) + ".")
    else:
        while count < 21:
            print()
            player_decision = input("Would you like to hit or stand? (h or s) ")
            if player_decision == "h":
                x = random.randint(0, len(deck) - 1)
                card = deck.pop(x)
                player_hand.append(card)
                print("You draw: " + str(card))
                count = hand_total(player_hand)
                print("Your hand count is now " + str(count) + ".")
            else:
                return [player_hand, deck]
    return [player_hand, deck]

def results(player_hand, dealer_hand, player_money, bet):
    """This function accepts four parameters. Two of the paraemters are lists for the
    player and dealers hands. The third parameter is an integer showing the amount of money
    left in the players account and the fourth is the bet (either $2 or $4).
    The function checks to see if the player won or lost the hand
    and adds/subtracts money accordingly."""
    
    player_count = hand_total(player_hand)
    dealer_count = hand_total(dealer_hand)
    if player_count > 21:
        player_money -= bet
    elif player_count > dealer_count and player_count <= 21:
        print("You won the hand.")
        player_money += bet
    elif dealer_count > player_count and dealer_count <= 21:
        print("You lost the hand.")                      
        player_money -= bet
    elif dealer_count > 21 and player_count < 21:
        print("You won the hand.")
        player_money += bet                     
    elif dealer_count == player_count:
        print("There is a draw. The count for both hands is " + str(player_count) + ".")
    return player_money
                          
def hand_total(hand):
    """This fucntion takes in a list containing either the users or the
    dealers hand. The function returns the count of the hand."""
    
    count = 0
    # an ace has to be at the back of the list 
    # need to know the count of the ace
    for i in range(len(hand)):
        if hand[i] == "A":
            hand.pop(i)
            hand.append("A")
    for card in hand:
        if card == "K" or card == "Q" or card == "J":
            count += 10
        elif card == "A":
            if count >= 11:
                count += 1
            else:
                count += 11
        else:
            count += card
    return count

def if_blackjack(hand):
    """This function accepts a list that contains the original hand that the
    player is delt. The function returns True or False if the hand is a black
    jack."""

    if "A" in hand:
        if "K" in hand or "Q" in hand or "J" in hand or 10 in hand:
            return True
        else:
            return False
    else:
        return False

def main():
    """This is the main function for this black jack program."""

    deck = [2, 3, 4, 5, 6, 7, 8, 9, 10, "J", "Q", "K", "A"] * 16
    print("Welcome to Matt and Sebastian's Black Jack game!")
    print("To start you will be given $10. Keep playing until your money runs out.")
    print()
    player_money = 10
    i = 0
    while player_money > 0:
        # the user is delt their hand
        player_hand = deal_hand(deck)
        deck = player_hand[1]
        player_hand = player_hand[0]
        # the dealer (computer) recieves both cards 
        dealer_hand = deal_hand(deck)
        deck = dealer_hand[1]
        dealer_hand = dealer_hand[0]
        
        print("You have been delt: " + str(player_hand[0]) + " and " + str(player_hand[1]))
        # only one of the dealers cards are shown
        print("The dealer is showing: " + str(dealer_hand[0]))
        print()
        # checking to see if there is a black jack
        if if_blackjack(player_hand) == True:
            if if_blackjack(dealer_hand) == False:
                player_money += 3
                print("You were delt a black jack!")
                print("You have $" + str(player_money) + " left in your account")
                print("------------------------------------------")
                print() 
        else:
            # if there isn't a black jack the user can double down on their turn
            # this is when you put down the amount of money down and are delt only one more card
            double_down = input("Would you like to double down on your bet? (y or n) ")
            if double_down == "y":
                bet = 4
            else:
                # anything besides "y" means they don't double down
                bet = 2
            # the user decides which to hit or stand with their hand
            player_hand = player_option(player_hand, deck, bet)
            deck = player_hand[1]
            player_hand = player_hand[0]
            # dealers hand gets fully delt 
            dealer_hand = dealer(dealer_hand, deck)
            deck = dealer_hand[1]
            dealer_hand = dealer_hand[0]
            # checking to see if the player won or lost money
            player_money = results(player_hand, dealer_hand, player_money, bet)
            print("You have $" + str(player_money) + " left in your account")
            print("------------------------------------------")
            print()
        # every twenty songs the four decks are put back together 
        i += 1
        if i % 20 == 0:
            deck = [2, 3, 4, 5, 6, 7, 8, 9, 10, "J", "Q", "K", "A"] * 16

if __name__ == "__main__":
   main()
