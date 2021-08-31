class Bank():
    def __init__(self, name, pin, cardnumber):
        self.name = name
        self.pin = pin
        self.cardnumber = cardnumber

    def CashWithdrawl(self,amount):
        new_amount=50000-amount
        print("you have withdrawn amount "+str(amount) +". Your remaining balance is "+ str(new_amount))

    def BalanceEnquiry(self):
        print("balence 50k")

def main():
    name=input("enter the name of the bank: ")
    cardnumber=input("insert your card number: ")
    pin=input("enter your pin number: ")
    new_user=Bank(name, pin, cardnumber)
    print("chose your activity")

    print("Choose your activity ")
    print("1.Balance Enquriy   2.withdrawl")
    activity = int(input("enter activity number :- "))

    if (activity == 1):
        new_user.BalanceEnquiry()
    elif (activity == 2):
        amount = int(input("enter the amount:- "))
        new_user.CashWithdrawl(amount)
    else:
        print("enter a valid number")


if __name__ == "__main__":
    main()



