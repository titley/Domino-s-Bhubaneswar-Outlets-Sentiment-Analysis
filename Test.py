import random
print("Welcome to the GAME !!! 🔥🔥🔥🔥🔥")
print("0 is for stone\n1 is for paper\n2 is for scissor\n")

# Get the user's choice as an integer
try:
    user_choice = int(input("Enter 0 for stone, 1 for paper, or 2 for scissor: "))
    
    # Check if the input is valid
    if user_choice not in [0, 1, 2]:
        print("Invalid choice! Please enter 0, 1, or 2.")
        exit()
except ValueError:
    print("Invalid input! Please enter a number.")
    exit()

# Generate the computer's choice (0, 1, or 2)
computer_choice = random.randint(0, 2)

# Messages for wins
computer_wins_message = "Computer wins"
user_wins_message = "User wins"

# Display the choices
print(f"Your choice: {user_choice}, Computer's choice: {computer_choice}")

# Determine the outcome of the game
if user_choice == computer_choice:
    print("DRAW 😔")
elif (user_choice == 0 and computer_choice == 1) or \
     (user_choice == 2 and computer_choice == 1) or \
     (user_choice == 1 and computer_choice == 2):
    print(computer_wins_message)
elif (user_choice == 1 and computer_choice == 0) or \
     (user_choice == 2 and computer_choice == 0) or \
     (user_choice == 0 and computer_choice == 2):
    print(user_wins_message)

