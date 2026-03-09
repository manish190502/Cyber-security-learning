import math


class Node:
    def __init__(self,data):
        self.data = data 
        self.next = None 

node_1 = Node(10)
node_2 = Node(20)
node_3 = Node(30)
node_4 = Node(40)
node_5 = Node(50)
node_1.next = node_2
node_2.next = node_3
node_3.next = node_4
node_4.next = node_5

#Brute force
# header = node_1
# counter = 0
# while header :
#     counter+=1
#     header = header.next
# print(counter)
# middle = math.ceil((counter)/2)
# print(middle)

# new_counter =1
# header = node_1
# while new_counter!= middle:
#     new_counter+=1
#     header = header.next
# print(header.data)    

#optimal solution
slow = node_1
fast = node_1
while fast.next and fast.next:
    slow=slow.next
    fast = fast.next.next
print(slow.data)    