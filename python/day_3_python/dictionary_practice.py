#LEVEL 1 

student = {"name":"manish",
           "age":23,
           "marks":90}
#assignment 1 
print(student["name"])
print(student["marks"])

#assignment 2 
student.setdefault("grade","A")
print(student)

#assignment 3
for k,v in student.items():
    print(f"{k}->{v}")


#LEVEL 2
#Count how many times each word appears using a dictionary.
sentence = "apple banana apple orange banana apple"
counting_dict = {}
sentence= sentence.replace(" ","")
for letter in sentence:
    counting_dict.setdefault(letter,0)
    counting_dict[letter]+=1
print(counting_dict)

#LEVEL 3
#Find Min / Max
prices = {"coffee": 120, "tea": 80, "milk": 60, "juice": 150}
cheapest_item = min (prices,key=prices.get)
print(f"cheapest item ->{cheapest_item} ,  cost of this item -> {prices[cheapest_item]}")

#explanation of this lambda function .
#when i use max function it takes the maximum but comapres it over the first element of the tuple .
# This tuple was created when we used prices.item. 
#to make this instead search the value instead of the key we write that lambda function x:x[1] which is the value part of the tuple
# print(max(prices.items(),key=lambda x :x[1]))


# Level 4: Advanced Dictionary Use

# Nested Dictionary

# Create a dictionary of students:

students = {
    "101": {
            "name": "Manish", 
            "marks": 90
            },
    "102": {
            "name": "Rahul",
            "marks": 85
            },
    "103": {
            "name": "Amit",
            "marks": 95
    }
}

#Print sum and average of marks
sum_array=[]
for k,v in students.items():
    # print(f"{k}->{v}")
    # print(students[k].get("marks"))
    sum_array.append(students[k].get("marks"))
print(sum(sum_array))
print(sum(sum_array)/len(sum_array))

# Print the name and marks of each student in a loop.
for k,v in students.items():
    print(f"roll no ->{k}")
    for k1,v1 in v.items():
        print(f"{k1}->{v1}")
      
        
