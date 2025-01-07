# Create Account class with 2 attributes - balance and account no.
# Create a method for debit, credit and printing balance. 
class Account:
    def __init__(self, bal, acc):
        self.balance = bal
        self.account_no = acc

    def debit(self, amount):
        self.balance -= amount
        print("Rs." ,amount, "was debited. New Balance is ",self.balance )

    def credit(self, amount):
        self.balance += amount
        print("Rs. ",amount, "was credited. New balance is", self.balance)


acc1 = Account(10000,6789)
acc1.debit(2000)
acc1.credit(3000)