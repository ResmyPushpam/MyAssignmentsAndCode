import Random
def number_guessing_game():
    random_number=Random.generate_random_number()
    number_to_guess= random_number.generate_random_number()
    attempts = 0
    max_attempts = 10
    print ("Welcome to the Number Guessing Game!")
    print ("You have 10 attempts to guess a number between 1 and 100.")
    print("Let's begin!")
    while attempts < max_attempts:
        try:
            user_guess = int(input("Enter your guess: "))
            attempts += 1
            if user_guess < 1 or user_guess > 100:
                print("Please guess a number within the range of 1 to 100.")
                continue
            if user_guess < number_to_guess:
                print("Too low!")
            elif user_guess > number_to_guess:
                print("Too high!")
            else:
                print(f"Congratulations! You've guessed the number {number_to_guess} in {attempts} attempts.")
                break
        except ValueError:
            print("Invalid input. Please enter a number.")
    else:
        print(f"Sorry, you've used all {max_attempts} attempts. The number was {number_to_guess}.")
