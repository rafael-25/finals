import random
import time

# Task 1: Deal Hand
def deal_hand(tile_bag):
    hand_size = 7
    hand = []
    tiles = list(tile_bag.keys())
    weights = list(tile_bag.values())
    for _ in range(hand_size):
        chosen_tile = random.choices(tiles, weights=weights)[0]
        hand.append(chosen_tile)
    return hand

# Task 2: Validate Word and Calculate Score
def is_valid_word(word, word_list):
    return word.upper() in word_list


def calculate_score(word, tile_values):
    score = 0
    for letter in word:
        letter = letter.upper()
        if letter in tile_values:
            score += tile_values[letter]
        elif letter == '_':  # Blank tile
            score += 0  # Blank tiles are worth 0
        else:
            return 0  # invalid character

    return score

# Task 3: Check Available Letters
def check_available_letters(hand, word):
    available_letters = hand[:]  # copies hand to available_letters
    for letter in word.upper():
        if letter in available_letters:
            available_letters.remove(letter)
        elif '_' in available_letters:
            available_letters.remove('_')
        else:
            return False  # Letter not available
    return True

# Task 4: Play Round
def play_round(player_num, hand, word_list, tile_values):
    print(f"Player {player_num}'s hand: {hand}")
    start_time = time.time()

    while True:
        word = input(f"Player {player_num}, enter your word (or type 'pass'): ")
        if word.lower() == 'pass':
            return 0, False

        elapsed_time = time.time() - start_time
        if elapsed_time > 60:
            print("Time's up!")
            return 0, False

        if is_valid_word(word, word_list):
            score = calculate_score(word, tile_values)
            if check_available_letters(hand, word):
                print(f"Word '{word}' is valid. Score: {score}")
                return score, True
            else:
                print("You don't have the letters to make that word.")
        else:
            print("Invalid word. Try again.")


# Task 5: Main Game Loop
def play_scrabble():
    player1_score = 0
    player2_score = 0

    for _ in range(5):  # Play 5 rounds
        player1_hand = deal_hand(tile_bag)
        score, valid = play_round(1, player1_hand, word_list, tile_values)
        player1_score += score if valid else 0

        player2_hand = deal_hand(tile_bag)
        score, valid = play_round(2, player2_hand, word_list, tile_values)
        player2_score += score if valid else 0

    print(f"Player 1 total score: {player1_score}")
    print(f"Player 2 total score: {player2_score}")

    if player1_score > player2_score:
        print("Player 1 wins!")
    elif player2_score > player1_score:
        print("Player 2 wins!")
    else:
        print("It's a tie!")


# Entry point
if __name__ == "__main__":
    # Dictionary to represent the number of tiles available for each letter in the game.
    tile_bag = {
        'A': 9, 'B': 2, 'C': 2, 'D': 4, 'E': 12, 'F': 2, 'G': 3, 'H': 2, 'I': 9, 'J': 1,
        'K': 1, 'L': 4, 'M': 2, 'N': 6, 'O': 8, 'P': 2, 'Q': 1, 'R': 6, 'S': 4, 'T': 6,
        'U': 4, 'V': 2, 'W': 2, 'X': 1, 'Y': 2, 'Z': 1, '_': 2
    }

    # Dictionary to represent the value of each tile in within the game.
    tile_values = {
        'A': 1, 'B': 3, 'C': 3, 'D': 2, 'E': 1, 'F': 4, 'G': 2, 'H': 4, 'I': 1, 'J': 8,
        'K': 5, 'L': 1, 'M': 3, 'N': 1, 'O': 1, 'P': 3, 'Q': 10, 'R': 1, 'S': 1, 'T': 1,
        'U': 1, 'V': 4, 'W': 4, 'X': 8, 'Y': 4, 'Z': 10, '_': 0
    }

    # Get a list of all of the valid words in the scrabble dictionary file.
    word_list = []
    with open('dictionary.txt', 'r') as f:
        # Add each word in the file to the list of words
        for line in f:
            # Uppercase for consistency
            word_list.append(line.strip().upper())

    play_scrabble()
