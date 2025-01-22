import random

def start():
    deck = [
        "Ace of Hearts", "2 of Hearts", "3 of Hearts", "4 of Hearts",
        "5 of Hearts", "6 of Hearts", "7 of Hearts", "8 of Hearts",
        "9 of Hearts", "10 of Hearts", "Jack of Hearts", "Queen of Hearts", "King of Hearts"
    ]

    correct_card = select_deck(deck)
    guess = input("Guess a card from a deck of cards: ")
    attempts = check(guess, correct_card)

    print(f"You lose, after {attempts} attempts. The correct card was: {correct_card}")

def select_deck(deck):
    return random.choice(deck)

def check(guess, correct_card):
    tries = 0
    while tries < 3:
        if guess == correct_card:
            print(f"Congratulations! You guessed the correct card '{correct_card}' in {tries} tries.")
            break
        elif guess == "":
            print("So sad that you quit.")
            break
        else:
            guess = input("Incorrect, Try again: ")
        tries += 1
    return tries

# Start the game
start()
