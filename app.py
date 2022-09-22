from banking_pkg import account


def atm_menu(name):
    print("")
    print("          === Automated Teller Machine ===          ")
    print("User: " + name)
    print("------------------------------------------")
    print("| 1.    Balance     | 2.    Deposit      |")
    print("------------------------------------------")
    print("------------------------------------------")
    print("| 3.    Withdraw    | 4.    Logout       |")
    print("------------------------------------------")


# task2
print("          === Automated Teller Machine ===          ")
user = input("Enter name to register: ")
pin = input("Enter PIN: ")
balance = 0
print(user + " has been registered with a starting balance of", "$" + str(balance))

# task3
print("          === Automated Teller Machine ===          ")
while (True):
    print("LOGIN")
    name_to_validate = input("Enter Name: ")
    pin_to_validate = input("Enter Pin: ")
    if name_to_validate == user and pin_to_validate == pin:
        print("Login successful! ")
        break
    else:
        print("Invalid credentials!")

# task4
while (True):
    atm_menu(user)
    option = input("Choose an option: ")
    if option == "1":
        account.show_balance(balance)
    elif option == "2":
        balance = account.deposit(balance)
        account.show_balance(balance)
    elif option == "3":
        balance = account.withdraw(balance)
        account.show_balance(balance)
    elif option == "4":
        account.logout(user)
        break
