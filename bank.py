class Bank():
    def __init__(self, name, pin, cardnumber):
        self.name = name
        self.pin = pin
        self.cardnumber = cardnumber

    def CashWithdrawl(self):
        print("2000")

    def BalanceEnquiry(self):
        print("payed")

# Define some cars
cashtaken = Bank("ICICI", 234567890, 22337766) 
cashtaken2 = Bank("HDFC", 662987669, 99269671)

print("card1")
print(cashtaken.name)
print("pin:",cashtaken.pin)
print("card number:",cashtaken.cardnumber)
print(" ")
print("Card2")
print(cashtaken2.name)
print("pin:",cashtaken2.pin)
print("card number:",cashtaken2.cardnumber)

