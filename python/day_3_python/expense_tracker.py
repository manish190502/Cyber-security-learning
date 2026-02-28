class Expense:
    def __init__(self,item,cost):
        self.item = item
        self.cost = cost
    def __str__(self) -> str:
        return (f"This item -> {self.item} , costs -> {self.cost}")

class ExpenseTracker():
    def __init__(self):
        
        self.tracker = []

    def add_expenses(self,item,cost):
        expense = Expense(item,cost)
        self.tracker.append(expense)
        
        
    def total_expense(self):
        # total = sum(exp.cost for exp in self.tracker)
        total =sum(map(lambda exp : exp.cost ,self.tracker))
        print(total)
    def __str__(self):
        return "\n".join(map(lambda x : str(x),self.tracker))

new_Expense = ExpenseTracker()
new_Expense.add_expenses("coffee",10)
new_Expense.add_expenses("gym",20)
new_Expense.total_expense()

print(new_Expense)

