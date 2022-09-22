def show_balance(balance):
    balance = float(balance)
    print("Current balance is: $" + str(balance))


def deposit(balance):
    amount = float(input("Enter amount to deposit: $"))
    balance = balance + amount
    return balance


def withdraw(balance):
    amount = float(input("Enter amount to withdraw: $"))
    balance = balance - amount
    return balance


def logout(user):
    print("Goodbye", user)
