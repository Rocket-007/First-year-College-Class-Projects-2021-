# importing random module
import random
# generating random number
random_number = random. randint ( 1 , 100 )
# initializing no. of guess to 0
guess_count = 0
# running loop until user guess the random number
while True:
    # getting user input
    user_guessed_number = int ( input( " Enter a number in the range of 1 -100 : ") )
    # checking for the equality
    if user_guessed_number == random_number:
        print ("You have guessed the number in " + str(guess_count) + " guesses")
        # breaking the loop
        break
    elif user_guessed_number < random_number:
        print ( " Your number is low " )
    elif user_guessed_number > random_number:
        print ( " Your number is high" )
    # incrementing the guess count
    guess_count += 1