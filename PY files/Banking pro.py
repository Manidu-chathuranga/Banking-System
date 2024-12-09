#python banking sys

def show_balance(balance):
    print(f"Your balance is ${balance:.2f}")

def deposit():
    amount = float(input("Enter an amount to be deposited:"))
    
    if amount < 0:
        print("That's  not a valid amount")
        return 0
    else:
        return amount

def withdraw(balance):
    amount = float(input("Enter an amount to withdraw:"))  # Corrected prompt
    
    if amount > balance:  # Check if there are sufficient funds
        print("Insufficient funds")
        return 0
    elif amount < 0:  # Check if the amount is valid
        print("Amount must be greater than 0")
        return 0
    else:  # Valid withdrawal
        return amount

def main():
    balance = 0
    is_running = True

    while is_running:
        print("*********************")
        print("   Banking Program")
        print("*********************")
        print("   1.Show Balance")
        print("   2.Deposit")
        print("   3.Withdraw")
        print("   4.Exit")
        print("*********************")
        
        choice = input("Enter your choice (1-4):")
        
        if choice == '1':
            show_balance(balance)
        elif choice == '2':
            balance += deposit()
        elif choice == '3':
            balance -= withdraw(balance)
        elif choice == '4':
            is_running = False
        else:
            print("****************************")
            print("That is not a valid choice")
            print("****************************")
if __name__== '__main__':
    main()

    
print("Thank you! have a nice day!")
    
    
    
    