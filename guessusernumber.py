import random

def computer_guess(x):
    low = 1
    high = x
    feedback = ''
    
    # Introduction prompt
    introduction = input("Hello! Would you like to play this game? (yes/no): ").lower()
    
    if introduction == 'no':
        print("Oh no, maybe next time. Have a great day!")
        return
    elif introduction == 'yes':
        print("Great! Let's get started!")
    else:
        print("Invalid input. Please start the game again.")
        return

    # Main game loop
    while feedback != 'c':
        if low != high:
            guess = random.randint(low, high)
        else:
            guess = low  # or high, since low == high

        feedback = input(f"Is {guess} too high (H), too low (L), or correct (C)? ").lower()

        if feedback == 'h':
            high = guess - 1
        elif feedback == 'l':
            low = guess + 1
        elif feedback == 'c':
            print(f"Yay! The computer guessed your number, {guess}, correctly!")
        else:
            print("Invalid input. Please respond with 'H', 'L', or 'C'.")

# Run the game
computer_guess(100)
