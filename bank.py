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
cashtaken = Bank("icici", 234567890, 22337766) 
cashtaken2 = Bank("hdfc", 662987669, 99269671)

print(cashtaken.name)
print(cashtaken.pin)
print(cashtaken.cardnumber)
print(cashtaken2.name)
print(cashtaken2.pin)
print(cashtaken2.cardnumber)