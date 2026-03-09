class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

# --- Setup ---
node1 = Node(100)
node2 = Node(200)
node3 = Node(300)
node4 = Node(400)
node5 = Node(505)

node1.next = node2
node2.next = node3
node3.next = node4
node4.next = node5

head = prev = current = nextNode =  node1

# # --- Scenario 1: Corrected Search ---
# print("--- Searching for 505 ---")
# current = head
# found = False
# while current is not None: # Check the node itself, not the 'next'
#     if current.data == 505:
#         found = True
#         break
#     current = current.next
# print(f"Is 505 present? {found}")


# # --- Scenario 2: Corrected Deletion (Deleting 300) ---
# print("\n--- Deleting 300 ---")
# target = 300
# current = head
# previous = None

# while current is not None:
#     if current.data == target:
#         if previous is None:
#             # Special Case: We are deleting the head!
#             head = current.next
#         else:
#             # The "Bridge": Link the previous node to the one AFTER current
#             previous.next = current.next
#         break
    
#     # This is the secret: 'previous' follows 'current' like a shadow
#     previous = current
#     current = current.next


#reversing a linkedlist
print("Final List Structure:")
current = head
while current:
    print(current.data, end=" -> ")
    current = current.next
print("None")

current = head.next
head.next = None
while current is not None:

    nextNode = current.next
    current.next = head
    head = current
    current = nextNode



# --- Verification ---
print("Final List Structure:")
current = head
while current:
    print(current.data, end=" -> ")
    current = current.next
print("None")


