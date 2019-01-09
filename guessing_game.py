#Python Web Development Techdegree
#Project 1 - Number Guessing Game
#Developer - Luke Fisher
#--------------------------------
#
import random
import sys

# Create a function called start_game which stores a random correct integer and prompts the user to guess until correct
def start_game():
    print("Welcome to the Number Guessing Game, player!")
    correct_number = random.randint(1,10)
    correct = False
    play_again = False
    high_score = 11
    number_of_guesses = 1

# while loop that contains the game logic, user input, and prompting the user if they would like to play the game again
    while not correct:
        
        try:
            random_number_guess = int(input("Please enter a number between and including 1-10: "))
            
            # condition if it is lower
            if random_number_guess > correct_number and random_number_guess <=10:
                print("It's lower!")
                number_of_guesses += 1
                continue
            
            # condition if it is higher    
            elif random_number_guess < correct_number and random_number_guess >=1:
                print("It's higher!")
                number_of_guesses += 1
                continue
            
            # condition if the user input is out of specified number range
            elif random_number_guess > 10 or random_number_guess <1:
                print("Oh no! You guessed out of range! Please try again.")
                number_of_guesses += 1
                continue
            
            # condition if the user input correctly guesses the number, then ask the user if they'd like to play again
            # if the user says yes, repeat the game logic with the high_score being displayed, and the number of guesses reset
            elif random_number_guess == correct_number:
                print("Congrats! You guessed correctly! It took you a total number of {} guesses.".format(number_of_guesses))
                
                play_again = input("Would you like to play again? (Y/N) ")
                
                if play_again.lower() == "y":
                    correct_number = random.randint(1,10)
                    if number_of_guesses < high_score:
                        high_score = number_of_guesses
                    print("Your high score is ", high_score)
                    number_of_guesses = 1
                    continue
                
                # if the user says no, then exit the game and display a shutdown message
                elif play_again.lower() == "n":
                    sys.exit("Thanks for playing! Shutting down...")
                
                # if the user types anything else other than y or n, display shutdown message    
                else:
                    sys.exit("Thanks for playing! Shutting down...")
            
            # condition if a anything other than a number was inputted        
            else:
                print("Please enter a numeric value!")
                number_of_guesses += 1
                continue
        
        # expect ValueError        
        except ValueError as err:
            print("Please use a numeric value! ")
            
    
if __name__ == '__main__':
    # Kick off the program by calling the start_game function.
    start_game()