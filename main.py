def get_user_guess():
    while True:
        try:
            guess=int(input("enter your guess(1-100):"))
            if 1<=guess<=100:
                return guess
            else:
                print("please enter a number between 1 and 100.")
        except ValueError:
            print("invalid input! please enter a number.")      
import random
def generate_random_number():
    return random.randint(1,100)
def play_game():
    print("welcome to the number guessing game!")
    random_number=generate_random_number()
    attempts=0
    while True:
        guess=get_user_guess()
        attempts+=1
        if guess < random_number:
            print("too low! try again.")
        elif guess>random_number:
            print("too high! try again.") 
        else:
            print("congratulations! you guessed the number in {attempts} attempts.")
            break       
    
