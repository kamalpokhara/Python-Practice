class Bank:

    count = 0

    def __init__(self, account_holder, balance=0):
        self.name = account_holder
        self.__balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print(f"{amount} deposited. Total amount = {self.__balance}")

    def withdraw(self, amount):
        if amount <= self.__balance:
            print("Withdrawing")
            self.__balance -= amount
            print(f"{amount} is withdrawed, Remaining amount = {self.__balance}")

        else:
            print("Insufficient balance")

    def view__balance(self):
        print("The available balance", self.__balance)

    def __eq__(self, other):
        if self.name == other.name:
            return True
        return False


account1 = Bank("ram prasad", 500)  # Test deposit method
account1.deposit(200)  # Expected: balanc increases to 700

account1.withdraw(300)  # Expected: balanceecreases to 400
# Test withdraw method (invalidthdrawal)
account1.withdraw(1000)  # Expected: Insufficientu\nds message
# Test view__balance method

account1.__balance = 100000
account1.view__balance()  # Expected: prints currentbalance (400)
# Create another account to test multiple objects
account2 = Bank("Jane Smith", 1000)
account2.deposit(500)
account2.view__balance()  # Expected: 1500
# Delete accounts to trigger destructor


# if ac2 == ac1:
#     print("same")
