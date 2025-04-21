def show_balance():
    print (f" your balance is $ {balance:.2f}")
    

def deposit():
    amount = float(input ("enter an amount to be deposited"))
    
    if (amount<0):
        print("not valid")
        return 0
    else:
        return amount
def withdraw():
    amount = input("enter amount to be withdrawn")
    if amount>balance:
        print("insufficient funds")
    elif amount<0:
        print("amount must be greater than 0")
        return 0
    else:
        return amount

def main():

    balance =0
    is_running= True

    while is_running:
        print("banking program")
        print("1. show balance")
        print("2. deposit")
        print ("3 withdraw")
        print ("exit")

        choice= input ("enter you choice (1-4): ")

        if choice=='1':
            show_balance()
        elif choice=='2':
            balance+=deposit()
        elif choice=='3':
            balance-= withdraw()
        elif choice=='4':
        is_running = False   
        else:
            print("This is not a valid choice")
              
print ("thank you")