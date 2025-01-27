def calculate_grade(student_name, homework_score, quiz_score, test_score):
    """This function calculates the final grade of a student based on their homework, quiz, and test scores."""
    grade = 0.3 * homework_score + 0.2 * quiz_score + 0.5 * test_score
    if grade >= 90:
        letter_grade = "A"
    elif grade >= 80:
        letter_grade = "B"
    elif grade >= 70:
        letter_grade = "C"
    elif grade >= 60:
        letter_grade = "D"
    else:
        letter_grade = "F"
    print(f"{student_name}'s final grade is {letter_grade}")

# The main program starts here
student_list = ["Alice", "Bob", "Charlie", "David", "Eve"]
for student in student_list:
    homework_score = float(input(f"Enter {student}'s homework score: "))
    quiz_score = float(input(f"Enter {student}'s quiz score: "))
    test_score = float(input(f"Enter {student}'s test score: "))
    calculate_grade(student, homework_score, quiz_score, test_score)

def attendance(student_name, attendance_array):
    """This function checks student's attendance"""
    if student_name in attendance_array:
        print(f"{student_name} was present today")
    else:
        print(f"{student_name} was absent today")

attendance_list = ["Alice", "Bob", "Charlie", "David"]
attendance("Bob", attendance_list)
