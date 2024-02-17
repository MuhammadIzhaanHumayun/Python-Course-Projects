def greet_person(person, message="Hello"):
    print(f"{person} says: {message}")

# Get user input for person
user_person = input("Enter a person's name: ")

# Get user input for message or use default
user_message = eval(input("Enter a greeting message (or press Enter for default): "))
 # Default greeting message

# Call the function with user input
greet_person(user_person, user_message)
