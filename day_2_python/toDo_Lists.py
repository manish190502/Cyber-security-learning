class toDo:
    def __init__(self,assignment,priority):
        self.priority = priority
        self.assignment = assignment 

    toDo_Lists = {}
    def add_to_list(self):
        print(self.priority,self.assignment)

# l1 = toDo("gym",1)
# l1.add_to_list()
print("Welcome to my to do list app ")
if (bool(input("Are you a new Customer ?"))):
    name = input("Please tell us your name  0")

else:
    name = input ("Please tell us your name 1 ")    

assignment = input (" What work do you wnt me to put in the list ")
priority = int(input("What is the priority"))
toDo


        