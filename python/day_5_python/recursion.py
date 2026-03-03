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

#count vowels
def vowel_count(s):
    if s == "":
        return 0
    if s[0] in 'aeiou':
        return 1+vowel_count(s[1::])
    else  :
        return 0+vowel_count(s[1::])
print(vowel_count("hello"))

#Problem 1: The Countdown 🚀
# Write a function countdown(n) that prints the numbers from n down to 1, and then prints "Blast off!".

def countdown(n):
    if n==0 :
        print("Blast off")
        return 0
    print(n)
    return countdown(n-1)

countdown(3)

#Problem 2: Multiplying a List ✖️
# Write a function product_of_list(lst) that multiplies all the numbers in a list together.

def product_of_list(number_list):
    if not number_list:
        return 1
    return number_list[0]*product_of_list(number_list[1::])
answer = product_of_list([1,2,3,4])
print(answer)

# Problem 3: Power of a Number ⚡Write a function power(base, exp) that calculates
#  $base^{exp}$ without using the ** operator.

def power_of_number(base,power):
    if power == 0:
        return 1
    return base*power_of_number(base,power-1) 
print(power_of_number(2,3))

#binary search
#The Challenge: "Is the number in the list?"
#  Write a recursive function is_present(lst, target) that returns True if
#  the target is in the list, and False if it is not.

def is_present(lst , target ):
    n = len(lst)//2
    if not lst:
        return False
    if lst[n] == target:
        return True
    
    elif target < lst[n]:
        return is_present(lst[:n:],target)
    else:
        return is_present(lst[n+1::],target) 
    return False       


# print(is_present([1, 5, 8, 10], 8))
print(is_present([1, 5, 8, 10], 100))