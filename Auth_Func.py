import random

database = {
    1321380112: ['Evans', 'Vare', 'egvare', 'evanspd', 0]
}


def init():
    print('Welcome to Max Bank')

    have_account = int(input("Do you have an account with us: 1 (Yes) 2 (No) \n"))

    if have_account == 1:

        login()
    elif have_account == 2:

        register()
    else:
        print("Invalid option selected")
        init()


def login():
    print("******* Login *******")

    account_number_from_user = int(input("Please enter you account number \n"))
    password = input("Enter Your password \n")

    for account_number, user_details in database.items():
        if account_number == account_number_from_user:
            if user_details[3] == password:
                bank_operation(user_details)

                print('Invalid account or password')
    login()


def register():
    print("******* Register *******")

    email = input("Please Enter Your email address \n")
    first_name = input("Enter your first name \n")
    last_name = input("Enter your last name \n")
    password = input("Please create a password \n")

    account_number = generate_account_number()

    database[account_number] = [first_name, last_name, email, password, 0]

    print("Your Account has been created successfully")
    print("=== ==== ===== ==== ===")
    print("Your account number is: %d" % account_number)
    print("=== ==== ===== ==== ===")

    login()


def bank_operation(user):
    print("Welcome %s %s" % (user[0], user[1]))

    selected_option = int(input(
        'Please select an option: (1) withdrawal (2) deposit (3) Balance (4) Complaint (5) Logout (6) Exit \n'))

    if selected_option == 1:

        withdrawal_operation(user)
    elif selected_option == 2:

        deposit_operation(user)
    elif selected_option == 3:

        balance(user)
    elif selected_option == 4:

        complaint()
    elif selected_option == 5:

        logout()
    elif selected_option == 6:

        exit()
    else:

            print("Selected Option is Invalid")
            bank_operation(user)


def balance(user):
    print("Current balance")
    return user["data"][4]


def update_balance(user, amount):
    print("Add or subtract balance")
    current_balance = balance(user)
    new_balance = current_balance + amount
    user_details = database[user["account_no"]]
    user_details[4] = new_balance
    user["data"] = user_details
    return user


def withdrawal_operation(user):
    print("Withdrawal")
    user_balance = balance(user)
    print("Current balance is:{}".format(user_balance))

    amount = int(input('Enter Amount to withdraw \n'))
    if user_balance >= amount:
        user = update_balance(user, -amount)
        print("New balance is:{}".format(balance(user)))
    else:
        print("Insufficient funds")


def deposit_operation(user):
    amount = int(input('Enter Amount to deposit \n'))
    update_balance(user, amount)
    print("\n Amount deposited:", amount)
    print("New balance is: {}".format(balance(user)))


def complaint():
    print("Enter Complaint")


def generate_account_number():
    return random.randrange(1111111111, 9999999999)


def get_current_balance(user_details):
    return user_details[4]


def logout():
    login()


init()
