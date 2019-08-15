class Account():
    def __init__(self, number, owner, balance, rate):
        self.owner = owner.name
        self.number = number
        self.balance = balance.value
        self.currency = balance.currency
        self.rate = rate/100

    def deposit(self, amount):
        self.balance = self.balance + amount.value

    def withdraw(self, amount):
        #add valid denoms logic here
        sum = Money('RM', amount)
        if sum.value:
            self.balance = self.balance - sum.value
            return sum.value

    def set_rate(self, new_rate):
        self.rate = new_rate/100

    def show_balance(self):
        print(f"{self.currency} {self.balance}")

    def accrue_interest(self, years):
        self.balance = self.balance*(1+self.rate)**years

class Money():
    valid_denoms = (100, 50, 20, 10, 5, 1)
    def __init__(self, currency, value):
        self.currency = currency
        copy = value
        for denom in self.valid_denoms:
            if copy >= denom:
                copy = copy - (copy//denom)*denom
        if copy == 0:
            self.value = value
        else:
            print("Not a valid denomination. Please try again.")
            self.value = 0

    def __str__(self):
        return f"{self.currency} {self.value}"

class Holder():
    def __init__(self, name):
        self.name = name

amar = Holder('Amar')

sum = Money('RM',9001)

amar_account = Account(545, amar, sum, 6)

breakpoint()