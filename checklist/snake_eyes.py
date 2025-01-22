import random

def start():
    greeting()
    count = roll_dice()  # Call the function to roll the dice and get the count
    print(f"It took you {count} times to get snake eyes.")

def greeting():
    print("Welcome to Snake Eyes")

def roll_dice():
    count = 0  # Initialize the counter for the number of rolls
    while True:  # Infinite loop to simulate repeated dice rolls
        roll_one = get_die()
        roll_two = get_die()
        count += 1  # Increment the roll counter
        
        # Print the rolled values
        print(f"Rolled: {roll_one} {roll_two}")
        
        # Check if both dice rolled 1 (snake eyes)
        if roll_one == 1 and roll_two == 1:
            break  # Exit the loop if snake eyes are rolled
    
    return count  # Return the number of rolls

def get_die():
    return random.randint(1, 6)  # Simulates a die roll (1-6)

# Start the program
start()
