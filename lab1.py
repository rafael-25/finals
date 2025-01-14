import random

# Pre-implemented Helper Functions
def pick_random_word(file_path="words.txt"):
    """
    Reads a list of words from a file and selects one at random.

    :param file_path (str): The path to the text file containing the list of words.
    :return (str): A randomly selected word from the file.
    """
    # DO NOT EDIT THIS FUNCTION
    with open(file_path, "r") as file:
        words = file.read().splitlines()
    return random.choice(words).lower()

def check_valid_word(word, file_path="wordlist.txt"):
    """
    Checks if the given word exists in the wordlist.

    :param word (str): The word entered by the player.
    :param file_path (str): The path to the text file containing the valid words.
    :return (bool): True if the word exists in the wordlist, False otherwise.
    """
    # DO NOT EDIT THIS FUNCTION
    with open(file_path, "r") as file:
        words = file.read().splitlines()
    return word.lower() in words

# Task 1: Validate and Get Player's Guess
def get_player_guess():
    """
    Requests an input from the user and re-requests a guess until the guess is valid.
    A valid guess is a five-character string containing only letters and is a valid word.

    :return (str): A valid 5-letter word entered by the player.
    """
    while True:
        word = input("Enter a valid 5-letter word: ")

        if len(word) != 5:
            print("Invalid guess. Please enter a valid 5-letter word.\n")

        elif not word.isalpha():
            print("Invalid word! Your guess must contain only letters.\n")

        elif not check_valid_word(word):
            print("Invalid word! That word is not in the wordlist.\n")
        else:
            return word

# Task 2: Check if the Player has Won
def has_won(secret, guess):
    """
    Checks if the player's guess matches the secret word. If the guess matches,
    this function should break the loop in the main game.

    :param secret (str): The secret word to be guessed.
    :param guess (str): The word entered by the player.
    :return (bool): True if the guess matches the secret word, False otherwise.
    """
    return secret == guess

# Task 3: Generate Feedback for the Player's Guess
def give_feedback(secret, guess):
    """
    Generates feedback for a guessed word:
        - 🟩 for correct letter in the correct position
        - 🟨 for correct letter in the wrong position
        - ⬜ for incorrect letter

    :param secret (str): The secret word to be guessed.
    :param guess (str): The word entered by the player.
    :return (str): A string of emoji symbols representing feedback for the guess.
    """
    feedback = ""

    for i in range(5):
        letter = guess[i]
        if secret[i] == letter:
            feedback += '🟩'
        elif guess[i] in secret:
            feedback += '🟨'
        else:
            feedback += '⬜'

    return feedback

# Task 4: Display the Game State
def display_game_state(guess, feedback):
    """
    Displays the guessed word along with its feedback in the format:
    <GUESS> | <FEEDBACK>

    :param guess (str): The guessed word entered by the player.
    :param feedback (str): The emoji feedback string corresponding to the guess.
    :return (None): Displays the current game state.
    """
    print(f"{guess.upper()} | {feedback}")

# Task 5: Main Game Loop
def play_wordle(secret):
    """
    The main game loop for the Woordle Clone. Allows the player to guess the secret word
    within a limited number of attempts, provides feedback, and tracks progress.

    :param secret (str): The secret word to be guessed.
    :return (None): Manages the game flow and displays win/lose messages.
    """
    # print(secret)
    print("Welcome to the Woordle Clone!")
    print("Can you solve the word of the day?\n")
    secret = 'asset'
    MAX_ATTEMPTS = 6
    attempts = 0
    green, yellow, gray = set(), set(), set()
    while attempts < MAX_ATTEMPTS:
        guess = get_player_guess()

        feedback = give_feedback(secret, guess)

        display_game_state(guess, feedback)

        if has_won(secret, guess):
            break
        else:
            attempts += 1
            print(f"{MAX_ATTEMPTS - attempts} guesses left.")
            print()

    if has_won(secret, guess):
        print("Congrats! You've solved today's challenge!")
    else:
        print(f"Game Over! The word was: {secret}")

# Entry Point of the Script
if __name__ == "__main__":
    secret_word = pick_random_word()
    play_wordle(secret_word)
