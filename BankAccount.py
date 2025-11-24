class Account:
    def __init__(self, bal, acc):
        self.balance = bal
        self.acoount_no = acc

    #Debit Method  
    def debit(self, amount):
        self.balance -= amount
        print("Rs.", amount, "was debited")
        print("Total Balance = ", self.get_balance())

    def credit(self, amount):
        self.balance += amount
        print("Rs.", amount, "was credited")
        print("Total Balance = ", self.get_balance())    

    def get_balance(self):
        return self.balance

acc1 = Account(10000 , 12345)
# print(acc1.balance)
# print(acc1.acoount_no)
acc1.debit(1000)
acc1.credit(2500)

