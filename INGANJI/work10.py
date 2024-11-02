import random

def number_guessing_game():
   
    number_to_guess = random.randint(1, 100)
    attempts = 0
    
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")
    
    while True:
        try:
           
            guess = int(input("Enter your guess: "))
            attempts += 1

            
            if guess < 1 or guess > 100:
                print("Please guess a number between 1 and 100.")
            elif guess < number_to_guess:
                print("Too low! Try again.")
            elif guess > number_to_guess:
                print("Too high! Try again.")
            else:
                print(f"Congratulations! You guessed the correct number in {attempts} attempts.")
                break

        except ValueError:
            print("Invalid input. Please enter a valid number.")


if __name__ == "__main__":
    number_guessing_game()
print("1.Inganji fiscal clovis,2.Isingizwe luckyson,3.Kirabo lucille,4,Gasore boris")
