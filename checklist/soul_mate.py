def soulmate_check(crush_age, birth_year):
    current_year = 2024
    result = crush_age - birth_year
    result += current_year
    
    print(f"If you see the age of your crush and your age then you are soulmates: {result}")

# Get user input
crush_age = int(input("Enter the age of your crush followed by 2 zeros (e.g., for age 18, enter 1800): "))
birth_year = int(input("Enter the year you were born (e.g., for 2007, enter 2007): "))

# Call the function
soulmate_check(crush_age, birth_year)
