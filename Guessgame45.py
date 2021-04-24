

#python guess program : 150l assignment, pg45
#ctto-----RockEt🚀 
print("🚀")

import math
import random

SecretNumber=random.randint(1,100)
#print(SecretNumber)

Guess=int(input("Guess the secret number: "))

NumberOfGuesses=1

while True:#Guess != SecretNumber:
    if Guess == SecretNumber:
        print("You took "+str(NumberOfGuesses)+" guesses")
        break
    else:
        NumberOfGuesses += 1
        if Guess>SecretNumber:
            Guess=int(input("Guess a smaller number: "))
        else:
            Guess=int(input("Guess a larger number: "))
