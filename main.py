# Programmers: Paige and Zain
# Course:  CS151, Dr. Zelalem Jembre Yalew
# Due Date: 10/16/24
# Lab Assignment: Lab5
# Problem Statement: Build a simulation of an ATM, where users can view their balance, deposit, or withdraw
# Data In: whether user wants to withdraw, deposit, view balance, or exit, how much money user wants to withdraw or
# deposit, if user has a coupon
# Data Out: account balance, and errors
# Credits: class resources

initial_balance = 1000
SENTINEL = 'e'
new_balance = 0
options =

while options != SENTINEL:
    options = input('Do you want to withdraw, deposit, view balance, or exit?')
    options = options.lower()
    if options == "w":
        withdraw_amount = int(input('Enter amount to withdraw: '))
        if withdraw_amount < 0:
            print("Cant input negative amount, try again.")
        else:
            new_balance = initial_balance - withdraw_amount
            print('Your new balance is', new_balance)
        if new_balance < 0:
            print("Warning: You will be charged 5% interest for going under $0.")
    elif options == 'd':
        deposit_amount = int(input('Enter amount to deposit: '))
        if deposit_amount < 0:
            print("Cant input negative amount, try again.")
        elif new_balance == deposit_amount + initial_balance:
            print(new_balance)
    elif options == 'v':
        print(new_balance)





