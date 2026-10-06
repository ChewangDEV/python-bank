from art import logo
import random as r

USER_DETAILS = {}


def user_input():
    """This function is run and print the statements and take user inputs"""
    print("Welcome to the Python Bank!")
    print("What would you like to do?\n"
          "1. Create Account\n"
          "2. Login\n"
          "3. Exit")

    choice = int(input("Enter your choice (1/2/3):  "))

    print("\n"* 5)

    if choice == 1:
        create_account()
    elif choice == 2:
        log_in()
    elif choice == 3:
        print("Thank you for your time!")
        exit()
    else:
        print("Invalid choice")


def create_account():
    """After taking the user inputs the return choice will come here and create an account"""
    age = int(input("What is your age? "))

    if age < 18:
        print("You are not old enough to open an account.")
    else:
        name = input("Enter your name: ").title()
        generate_pin = int(input("Enter your PIN: "))

        storing_detail(name, age, generate_pin)


def storing_detail(user_name, user_age, generate_pin):
    """In here we store the details of the user. Coming from create account function"""
    name = str(user_name)
    age = int(user_age)
    generate_pin = int(generate_pin)

    # Generate a unique account number
    user_account_number = account_number_generator()

    # Store this user's details
    details = {
        "name": name,
        "age": age,
        "pin": generate_pin,
        "money": 0,
        "transaction_history": [],
    }

    # Add the user's details to the main dictionary
    USER_DETAILS[user_account_number] = details

    print(f"\nAccount created successfully!")
    print(f"Your account number is: {user_account_number} (Saved this Account number and remember you pin number)")
    print("\n" * 5)


def account_number_generator():
    """This function is used to generate a random account number. If same then generate again."""
    random_number = r.randint(100000, 999999)

    # Keep generating until we get a number that isn't already used
    while random_number in USER_DETAILS:
        random_number = r.randint(100000, 999999)

    return random_number

def log_in():
    print("\n" * 5)
    user_acc = int(input("Enter your account number: "))
    if user_acc in USER_DETAILS:
        user_pin = int(input("Enter your PIN: "))
        print("\n "* 5)
        if user_pin == USER_DETAILS[user_acc]["pin"]:
            is_login = True
            while is_login:
                print("Welcome to Python Bank!")
                print("What would you like to do?\n"
                      "1. Check Balance\n"
                      "2. Deposit\n"
                      "3. Withdraw\n"
                      "4. Transaction History\n"
                      "5. Exit")
                user_choice = int(input("Enter your choice (1/2/3/4/5): "))
                if user_choice == 5:
                    is_login = False
                else:
                    transactions(user_acc, user_choice)
        else:
            print("Invalid pin")

    else:
        print("Account number Not available")



def transactions(user_account,user_transaction):
    if user_transaction == 1:
        print(f"Your available balance is: ${USER_DETAILS[user_account]['money']}")
        print("\n" * 5)
    elif user_transaction == 2:
        user_deposit = int(input("Enter your deposit amount: $"))
        if user_deposit > 0:
            USER_DETAILS[user_account]['money'] += user_deposit
            USER_DETAILS[user_account]['transaction_history'].append(f"Deposit ${user_deposit}")
            print("\n" * 5)
        else:
            print("Negative Value Cannot Deposit")
    elif user_transaction == 3:
        user_withdraw = int(input("Enter your withdraw amount: $"))
        if user_withdraw > 0:
            if user_withdraw <= USER_DETAILS[user_account]['money']:
                USER_DETAILS[user_account]['money'] -= user_withdraw
                USER_DETAILS[user_account]['transaction_history'].append(f"Withdraw ${user_withdraw}")
                print("\n" * 5)
            else:
                print("Insufficient money")

        else:
                print("Negative Value Cannot Withdraw")
    elif user_transaction == 4:
        history = USER_DETAILS[user_account]["transaction_history"]

        print("\nTransaction History:")

        if history:
            for transaction in history:
                print(f"- {transaction}")
        else:
            print("No transactions yet.")
            
        print("\n" * 5)

    else:
        print("Invalid input")


print(logo)

bank_open = True

while bank_open:
    user_input()


