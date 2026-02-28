class toDo:
    def __init__(self,):
        self.newArray=[]

    
    def add_to_list(self,assignment,priority):
        self.newArray.append((priority,assignment))

    def printToDoList(self):
        sorted_tasks = sorted(self.newArray,key=lambda task:task[1])  
        print("Your To-Do List:")
        for task, priority in sorted_tasks:
            print(f"Assignment = {task} | Priority = {priority}") 
        
l1 = toDo()
l1.add_to_list("food",1)
l1.add_to_list("gym",2)
l1.printToDoList()



        