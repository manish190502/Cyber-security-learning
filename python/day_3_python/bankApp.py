class Transaction:
    def __init__(self,amount,type):
        self.amount = amount
        self.type = type

    def __str__(self):
        return f"All transactions:\n -> {self.amount} was {self.type}"

class Account:
    def __init__(self,name):
        self.name = name
        self.balance = 0
        self.transactions = []
    def deposit_money(self,amount,name):
        self.transactions.append(Transaction(amount,"deposit"))
        self.balance +=amount
        # print(list(x.amount for x in self.transactions))
    def withdraw_money(self,amount,name):
        if amount > self.balance:
            print("You do not have sufficient balance to withdraw this much . ")
            return

        self.transactions.append(Transaction(amount,"withdraw"))
        self.balance-=amount
    def total_balance(self):
        print(f"The total Balance is {self.balance}")   
    def view_all_transaction(self):
        print(list((x.amount,x.type) for x in self.transactions))     

p1 = Account("manish")
p1.deposit_money(100,"manish")  
p1.withdraw_money(20,"manish")      
p1.total_balance()
p1.view_all_transaction()