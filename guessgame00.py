randomNumber=6

while True:
     guess=int(input("guess thenumber :  "))
     if randomNumber == guess:
         print("hurry! ")
         break
     else:
         print("loser")