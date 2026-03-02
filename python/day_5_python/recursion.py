#1. Sum of a List
# Write a recursive function recursive_sum(n) that takes a 
# positive integer n and returns the sum of all numbers from 1 to n.


def recursive_sum(n):
    if n == 1 :
        return 1
    return n+recursive_sum(n-1)    

answer = recursive_sum(10)
print(answer)

# 2. Reverse a String
# Write a recursive function reverse_string(s) 
# that takes a string and returns it reversed.

# Hint: The base case is an empty string or a single character. 
# The recursive step is last_character + reverse_string(everything_else).

def recursive_string(s):
    if s == "":
        return ""
    return s[-1]+ recursive_string(s[:-1:])

rs = recursive_string("hello")
print(rs)

#3. Fibonacci Sequence

def fib(n):
    if n==0:
        return 0
    elif n==1:
        return 1
    return fib(n-1)+fib(n-2)

answer = fib(10)
print(answer)