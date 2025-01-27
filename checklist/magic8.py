import random

# Function to greet the user
def greeting():
    name = input("Hello, I am Madame Franco, the best fortune teller in the world. What name would you like for me to call you? ")
    print(f"Hello {name}, I see you have a question.")
    print("I need you to think of ONE question, and I will tell you what the Crystal Ball said. Press Enter when you are ready.")
    input()  # Wait for the user to press Enter
    return name

# Function to select a random fortune
def get_fortune():
    random_words = [
        "Sorry, I don't see it happening at this time.",
        "Give it three months; it will happen.",
        "Go for it. Don't waste your time.",
        "I see money coming your way.",
        "You will get an important phone call soon."
    ]
    return random.choice(random_words)

# Function to provide the user with 3 lucky numbers
def lucky_num():
    numbers = [random.randint(1, 50) for _ in range(3)]  # Generate 3 random numbers between 1 and 50
    numbers.sort()  # Sort the numbers
    print(f"Your lucky numbers are: {', '.join(map(str, numbers))}")

# Main program logic
name = greeting()  # Call the greeting function to get the user's name
print("I am looking into my Crystal Ball, Ah...")

result = get_fortune()  # Call the get_fortune function
print(f"Well {name}, here is what the Crystal Ball said: {result}")

lucky_num()  # Call the lucky_num function
