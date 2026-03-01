

# # 🔥 PYTHON LAMBDA NOTES (Structured & Clean)

# ---

# ## 1️⃣ Basic Lambda Syntax

# ```python
# # Lambda syntax:
# # lambda arguments : expression

# # Normal function
# def square(x):
#     return x * x

# # Lambda equivalent
# square_lambda = lambda x: x * x

# print(square_lambda(5))

# # Output:
# # 25
# ```

# ---

# ## 2️⃣ Lambda with map()  → Transform Every Element

# ```python
# # map(function, iterable)
# # Applies function to every element

# numbers = [2, 4, 6, 8]

# squares = list(map(lambda x: x**2, numbers))
# print(squares)

# # Output:
# # [4, 16, 36, 64]
# ```

# ---

# ### Example: Convert to Uppercase

# ```python
# names = ["manish", "rahul", "amit"]

# upper_names = list(map(lambda x: x.upper(), names))
# print(upper_names)

# # Output:
# # ['MANISH', 'RAHUL', 'AMIT']
# ```

# ---

# ## 3️⃣ Lambda with filter() → Keep Matching Elements

# ```python
# # filter(function, iterable)
# # Keeps elements where condition returns True

# numbers = [5, 12, 7, 18, 3, 20]

# greater_than_10 = list(filter(lambda x: x > 10, numbers))
# print(greater_than_10)

# # Output:
# # [12, 18, 20]
# ```

# ---

# ### Example: Filter Words by Length

# ```python
# words = ["cat", "elephant", "dog", "tiger"]

# long_words = list(filter(lambda x: len(x) >= 4, words))
# print(long_words)

# # Output:
# # ['elephant', 'tiger']
# ```

# ---

# ## 4️⃣ Lambda with sorted() → Custom Sorting

# ```python
# # sorted(iterable, key=lambda x: something)

# students = [("Manish", 90), ("Rahul", 85), ("Amit", 95)]

# # Sort by marks (second element)
# sorted_students = sorted(students, key=lambda x: x[1])
# print(sorted_students)

# # Output:
# # [('Rahul', 85), ('Manish', 90), ('Amit', 95)]
# ```

# ---

# ### Reverse Order (Descending)

# ```python
# sorted_students_desc = sorted(students, key=lambda x: x[1], reverse=True)
# print(sorted_students_desc)

# # Output:
# # [('Amit', 95), ('Manish', 90), ('Rahul', 85)]
# ```

# ---

# ## 5️⃣ Sorting a Dictionary by Value

# ```python
# prices = {"coffee":120, "tea":80, "milk":60, "juice":150}

# # items() gives (key, value) pairs
# sorted_prices = sorted(prices.items(), key=lambda x: x[1])
# print(sorted_prices)

# # Output:
# # [('milk', 60), ('tea', 80), ('coffee', 120), ('juice', 150)]
# ```

# ---

# ## 6️⃣ Lambda with max() → Find Highest Value

# ```python
# students = {
#     "101": {"name":"Manish","marks":90},
#     "102": {"name":"Rahul","marks":85},
#     "103": {"name":"Amit","marks":95}
# }

# # x = ('101', {'name': 'Manish', 'marks': 90})
# # x[1]['marks'] gives the marks

# top_student = max(students.items(), key=lambda x: x[1]["marks"])
# print(top_student)

# # Output:
# # ('103', {'name': 'Amit', 'marks': 95})
# ```

# ---

# ### Print Clean Output

# ```python
# roll, info = max(students.items(), key=lambda x: x[1]["marks"])

# print(f"Top Student: {info['name']} scored {info['marks']}")

# # Output:
# # Top Student: Amit scored 95
# ```

# ---

# ## 7️⃣ Lambda with sum() → Sum of Squares

# ```python
# numbers = [1, 2, 3, 4]

# sum_of_squares = sum(map(lambda x: x**2, numbers))
# print(sum_of_squares)

# # Output:
# # 30
# ```

# (1² + 2² + 3² + 4² = 30)

# ---

# # 🧠 Key Concepts Summary

# | Function          | Purpose                     |
# | ----------------- | --------------------------- |
# | `map()`           | Transform every element     |
# | `filter()`        | Keep matching elements      |
# | `sorted()`        | Rearrange elements          |
# | `max()` / `min()` | Compare and find best/worst |
# | `sum()`           | Add values together         |

# ---

# # 🧠 Mental Model for Lambda

# When using:

# ```python
# lambda x: x[1]
# ```

# Always ask:

# 1. What is `x`?
# 2. What structure am I receiving? (tuple? dict? number?)
# 3. What part do I want to compare or transform?

# ---

# # ⚠ When NOT to Use Lambda

# * If logic is long
# * If multiple lines are needed
# * If readability suffers

# Use normal `def` instead.

# ---

