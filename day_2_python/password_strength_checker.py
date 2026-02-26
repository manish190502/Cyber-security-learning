import re
password = input("Enter a password ")

#our password needs atleast one occurance of a special character , Upper case ,a lowercase and a digit 
pattern = r"(?=.*[0-9])(?=.*[A-Z])(?=.*[a-z])(?=.*[^\d\w])"
if (re.search(pattern,password)):
    print("Matched")
else:
    print("notmatched")    
