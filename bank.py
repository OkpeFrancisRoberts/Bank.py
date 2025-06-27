account = {
    "password": "18",
    "username": "Filency",
    "balance": 100000
}

def login():
    print("Welcome to CBN bank")
    password = input("Enter your password: ")
    username = input("Enter your username: ")

    if password == account["password"] and username == account["username"]:
        print("Login successful\n")
        return True
    else:
        print("Incorrect password or username\n")
        return False

def check_balance():
    print(f"Your account balance is ₦{account['balance']}\n")

def deposit():
    try:
        amount = int(input("How much do you want to deposit?: ₦"))
        if amount <= 0:
            print("Invalid amount\n")
        else:
            account["balance"] += amount
            print(f"₦{amount} deposited successfully. New balance is ₦{account['balance']}\n")
    except ValueError:
        print("Please enter a valid number.\n")

def withdraw():
    try:
        amount = int(input("How much do you want to withdraw?: ₦"))
        if amount <= 0:
            print("Invalid amount\n")
        elif amount > account["balance"]:
            print("Insufficient funds\n")
        else:
            account["balance"] -= amount
            print(f"₦{amount} withdrawn successfully. New balance is ₦{account['balance']}\n")
    except ValueError:
        print("Please enter a valid number.\n")

def goodbye():
    print("Exited successfully.")
    print("Thank you for using our bank!")

def menu():
    while True:
        print("------ Select an option below ------")
        print("1. Check account balance")
        print("2. Deposit money")
        print("3. Withdraw money")
        print("4. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            check_balance()
        elif choice == "2":
            deposit()
        elif choice == "3":
            withdraw()
        elif choice == "4":
            goodbye()
            break
        else:
            print("Invalid option. Please try again.\n")

# Start the app
if login():
    menu()
