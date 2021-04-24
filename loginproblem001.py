




#program to specifically detect error password or error username. 
#ctto-----kenny, RockEt🚀 



userName="root"
password="root"


In_userName = input("\n\nUsername: ") 
In_password = input("Password: ") 


attempt = 1


while True:#userName == userName and password == password: 

    if attempt == False: 
        print(1-1)

    elif In_userName == userName and In_password == password: 
        print()
        print("--Username correct!")
        print("--Password correct!")
        print("ACCESS GRANTED! ") 
        break 


    elif In_userName != userName and In_password != password: 
        print()
        print("--Username incorrect!")
        print("--Password incorrect!")
        print("ACCESS DENIED! ")

        In_userName = input("\n\nUsername: ") 
        In_password = input("Password: ") 
        attempt += 1 


    elif In_userName == userName and In_password != password: 
        print()
        print("--Username correct!")
        print("--Password incorrect!")
        print("ACCESS DENIED! ")

        In_userName = input("\n\nUsername: ") 
        In_password = input("Password: ")
        attempt += 1 


    elif In_userName != userName and In_password == password:  
        print()
        print("--Username incorrect!")
        print("--Password correct!")
        print("ACCESS DENIED! ")

        In_userName = input("\n\nUsername: ") 
        In_password = input("Password: ") 
        attempt += 1 



    print("\n"+str(attempt)+" attempts used") 