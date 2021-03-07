class Account:
    def __init__(self,name,balance,address):
        self.name = name
        self.balance = balance
        self.address = address

    def __str__(self):
        return f'Information - name:{self.name}, balance:{self.balance} and address:{self.address}'

    def __repr__(self):
        return {'name':self.name, 'balance':self.balance, 'address':self.address}

    def deposit(self,amount):
        self.balance = (self.balance + amount)
        print(self.balance)

    def withdraw(self,amount):
        self.balance = (self.balance - amount)
        print(self.balance)

    