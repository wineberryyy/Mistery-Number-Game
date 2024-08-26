import random

def mystery_number():
    print("Welcome to the Mystery Number game!")
    print("I'm thinking of a number between 1 and 100. Can you guess it?")
    
    # Computer chooses a random number
    secret_number = random.randint(1, 100)
    
    attempts = 0
    guessed_correctly = False
    
    while not guessed_correctly:
        # The player makes a guess
        guess = int(input("Enter your guess: "))
        attempts += 1
        
        # Check if the guess is correct
        if guess == secret_number:
            guessed_correctly = True
            print(f"Congratulations! You uncovered the mystery number in {attempts} attempts.")
        elif guess < secret_number:
            print("Too low! Try again.")
        else:
            print("Too high! Try again.")

if __name__ == "__main__":
    mystery_number()
