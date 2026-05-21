import random

def play_game():
    """
    Function to play the Rock Paper Scissors game.
    Allows multiple rounds and tracks user and computer choices.
    """
    options = ["rock", "paper", "scissors"]
    
    print("--- Rock Paper Scissors Game ---")
    
    while True:
        # User input
        user_choice = input("Enter your choice (rock/paper/scissors) or 'quit' to exit: ").lower()
        
        if user_choice == 'quit':
            print("Thanks for playing!")
            break
            
        if user_choice not in options:
            print("Invalid choice! Please choose rock, paper, or scissors.")
            continue
            
        # Computer random choice
        computer_choice = random.choice(options)
        print(f"Computer chose: {computer_choice}")
        
        # Determine winner
        if user_choice == computer_choice:
            print("It's a tie!")
        elif (user_choice == "rock" and computer_choice == "scissors") or \
             (user_choice == "scissors" and computer_choice == "paper") or \
             (user_choice == "paper" and computer_choice == "rock"):
            print("You win!")
        else:
            print("Computer wins!")
        
        print("-" * 20)

if __name__ == "__main__":
    play_game()
