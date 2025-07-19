account = {
  
  "fullname" : " ",
  "username" : " ",
  "password" : " ",
  "balance" : 0.0
}

#Homepage of the bank
def starting():
    while True:
        print("Welcome to CBN bank")
        print("=" * 50)
        print("What do want today?")
        print("1. Signup")
        print("2. Login")
        print("3. Logout")
    
        choice1 = input("Enter an option: ")
    
        if choice1 == "1":
            signup()
        elif choice1 == "2":
            if login():
                menu()
        elif choice1 == "3":
            logout()
            break
        else:
            print("incorrect input, enter frim option 1 to 3...")
        
#Signup and validation
def signup():
    print("Register an account with us today")
    print("-" * 30)
    name = input("What is your fullname?: ")
    username = input("Enter a username: ")
    password = input("Enter a password: ")
    
    account["fullname"] = name
    account["username"] = username
    account["password"] = password
    print(f"Registered successfully {account["fullname"]}")
    
#login and validation
def login():
    for attempts in range(3):
        print("\nLogin now")
        print("-" * 30)
        username = input("Enter your username: ")
        password = input("Enter your password: ")

        if username == account["username"] and password == account["password"]:
            print("Login successful!\n")
            return True
        else:
            print("Incorrect username or password. Try again.")

    print("Too many failed attempts. Please try again later.\n")
    return False

#check account balance and validation       
def balance():
    print(f"Your account balance is ₦{account["balance"]}")
    
#widrawal and validation
def withdraw():
    try:
        withdraw = float(input("How much do you want to withdraw? "))
        if withdraw > account["balance"]:
            print("Insufficiaent fund")
        elif withdraw <= 0:
            print("Amount must be above zero")
        else:
            account["balance"] -= withdraw
            print(f"You have successfully withdraw ₦{withdraw}, your new banance ₦{account["balance"]}")
    except ValueError as e:
           print("Error:", e)

#deposit and validation          
def deposit():
    try:
        deposit = float(input("How much do you want to deposit? "))
        if deposit <= 0:
            print("Amount must be above zero")
        else:
            account["balance"] += deposit
            print(f"You have successfully deposited ₦{deposit}, your new banance ₦{account["balance"]}")
    except ValueError as e:
           print("Error: ", e)
           
#logout and validation
def logout():
    print(f"{account["fullname"]}! you have succefully logout, good bye")
    
#App menu and narv
def menu():
    while True:
        print("What do you want today?")
        print("-" * 30)
        print("1. Check balance")
        print("2. Deposit money")
        print("3. Withdraw money")
        print("4. Logout")
        
        choice2 = input("Enter an option: ")
        
        if choice2 == "1":
           balance()
        elif choice2 == "2":
           deposit()
        elif choice2 == "3":
           withdraw()
        elif choice2 == "4":
           logout()
           break
        else:
           print("Incorrect input... try again")
           
#To run the program       
starting()        
