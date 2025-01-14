class BankAccount:
    def __init__(self):
        self.__balance = 0
    def deposit(self, amount):
        self.__balance += amount
        return self.__balance
    def withdraw(self, amount):
        if amount > self.__balance:
            return "Insufficient balance"
        else:
            self.__balance -= amount
            return self.__balance
    def checkBalance(self):
        return self.__balance
b = BankAccount()
print("Balance:", b.checkBalance())
print("Deposit:", b.deposit(1000))
print("Balance:", b.checkBalance())
print("Withdraw:", b.withdraw(500))
print("Balance:", b.checkBalance())
print("Withdraw:", b.withdraw(600))
print("Balance:", b.checkBalance())