import random

# function to calculate the total value of a hand
def hand_value(hand):
    total = 0
    aces = 0
    for card in hand:
        if card == 'A':
            total += 11
            aces += 1
        elif card in ['J', 'Q', 'K']:
            total += 10
        else:
            total += int(card)
    # adjust for aces if total is over 21
    while total > 21 and aces > 0:
        total -= 10
        aces -= 1
    return total

# function to play a hand of blackjack
def play_hand():
    # create a deck of cards
    deck = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A'] * 4
    random.shuffle(deck)
    # create empty hands for the player and the dealer
    player_hand = []
    dealer_hand = []
    # deal two cards to the player and two cards to the dealer
    player_hand.append(deck.pop())
    dealer_hand.append(deck.pop())
    player_hand.append(deck.pop())
    dealer_hand.append(deck.pop())
    print("Player hand:", player_hand, "Total value:", hand_value(player_hand))
    print("Dealer hand:", dealer_hand[0], "X")
    # player's turn
    while True:
        choice = input("Do you want to hit or stand? ").lower()
        if choice == 'hit':
            player_hand.append(deck.pop())
            print("Player hand:", player_hand, "Total value:", hand_value(player_hand))
            if hand_value(player_hand) > 21:
                print("Bust! You lose.")
                return
        elif choice == 'stand':
            break
    # dealer's turn
    while hand_value(dealer_hand) < 17:
        dealer_hand.append(deck.pop())
    print("Dealer hand:", dealer_hand, "Total value:", hand_value(dealer_hand))
    if hand_value(dealer_hand) > 21:
        print("Dealer bust! You win.")
    elif hand_value(dealer_hand) > hand_value(player_hand):
        print("Dealer wins.")
    elif hand_value(dealer_hand) < hand_value(player_hand):
        print("You win!")
    else:
        print("It's a tie.")

# play a game of blackjack
play_hand()
