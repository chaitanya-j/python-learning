import bank
b = bank.Account('Chaitanya', 11000000, 'USA near Google Headquarters')
b.deposit(1000)

b.withdraw(50000)
print(b.__str__())
print(b.__repr__())
