# List of winter activities
activities = ["snowball fight", "build a snowman", "skiing", "sledding", "ice skating"]

# Points system for activities
points = [10, 15, 20, 12, 18]

# Function to display activities
def display_activities():
    print("Welcome to Winter Wonderland!")
    print("Choose an activity from the list below:")
    for i, activity in enumerate(activities):
        print(f"{i + 1}: {activity} ({points[i]} points)")

# Function to calculate points earned
def calculate_points(choice, bonus):
    if 1 <= choice <= len(activities):
        activity_points = points[choice - 1]
        total_points = activity_points + bonus
        print(f"You chose {activities[choice - 1]} and earned {activity_points} points.")
        print(f"Bonus points: {bonus}")
        return total_points
    else:
        print("Invalid choice. You earned 0 points.")
        return 0

# Main game loop
def start():
    total_score = 0
    bonus = 5  # Bonus points for each activity
    
    # Loop for three rounds
    for round_num in range(1, 4):
        print(f"\nRound {round_num}:")
        display_activities()
        
        # User input for activity choice
        try:
            user_choice = int(input("Enter the number of your chosen activity: "))
        except ValueError:
            print("Invalid input. Please enter a number.")
            user_choice = 0
        
        # Calculate points and update total score
        round_points = calculate_points(user_choice, bonus)
        total_score += round_points
    
    # Final message based on total score
    print("\nYour Winter Wonderland adventure is over!")
    if total_score >= 50:
        print(f"Amazing! You earned a total of {total_score} points. You're a winter adventurer! ❄️")
    else:
        print(f"You earned a total of {total_score} points. Keep practicing to master the winter activities! ☃️")

# Start the game
start()
