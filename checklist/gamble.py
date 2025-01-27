import random

# Game variables
money = 100
game_over = False

# Array of possible game outcomes
outcomes = ["win", "lose", "draw"]

# Function to play the game
def play_game():
    global money
    print(f"You have ${money} to bet.")
    bet = int(input("How much would you like to bet? "))
    
    if bet > money:
        print("You don't have enough money to make that bet.")
    else:
        money -= bet
        outcome = random.choice(outcomes)
        
        if outcome == "win":
            money += bet * 2
            print(f"Congratulations! You won ${bet}.")
        elif outcome == "lose":
            print(f"Sorry, you lost ${bet}.")
        else:  # outcome == "draw"
            money += bet
            print(f"The game is a draw. You get your bet of ${bet} back.")

# Main game loop
while not game_over:
    play_game()
    
    if money <= 0:
        print("You're out of money! Game over.")
        game_over = True
    else:
        play_again = input("Would you like to play again? (yes/no) ").strip().lower()
        if play_again == "no":
            print(f"Thanks for playing! You're leaving with ${money}.")
            game_over = True
