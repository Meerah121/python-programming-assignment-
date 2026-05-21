import random

def guess_number():
    """
    Game where the computer picks a random number between 1 and 100
    and the user tries to guess it.
    """
    number_to_guess = random.randint(1, 100)
    attempts = 0
    
    print("--- Number Guessing Game ---")
    print("I have selected a number between 1 and 100. Can you guess it?")
    
    while True:
        try:
            guess = int(input("\nGuess a number: "))
            attempts += 1
            
            if guess < number_to_guess:
                print("Too low!")
            elif guess > number_to_guess:
                print("Too high!")
            else:
                print(f"Correct! You guessed the number in {attempts} attempts.")
                break
        except ValueError:
            print("Please enter a valid integer.")

if __name__ == "__main__":
    guess_number()
