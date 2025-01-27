def replace_vowels(string):
    vowels = ['a', 'e', 'i', 'o', 'u']
    for i in range(len(string)):
        if string[i] in vowels:
            string = string[:i] + '1' + string[i+1:]
    return string

# get user input
user_string = input("Enter a string: ")

# replace vowels with numbers
new_string = replace_vowels(user_string)

# print the modified string
print("Modified string:", new_string)
