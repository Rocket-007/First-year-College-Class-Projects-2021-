userName = input("Hello! K-Tech Industrues! \n\nUsername: ") 
password = input("Password: ") 

count = 0 
count += 1 


while userName == userName and password == password: 

    if count == 3: 
        print("\nThree Username and Password Attempts used. Goodbye") 
        break 

    elif userName == 'kenneth' and password == 'blue': 
        print("Welcome! ") 
        break 

    elif userName != 'kenneth' or password != 'blue': 
        print("Your Username and Password is wrong!")
        userName = input("\n\nUsername: ") 
        password = input("Password: ") 
        count += 1 
        continue 
"""
    elif userName == 'kenneth' and password != 'blue': 
        print("Your Password is wrong!") 
        userName = input("\n\nUsername: ") 
        password = input("Password: ")
        count += 1 

    elif userName != 'kenneth' and password == 'blue': 
        print("Your Username is wrong!") 
        userName = input("\n\nUsername: ") 
        password = input("Password: ") 
        count += 1 
        continue  
"""