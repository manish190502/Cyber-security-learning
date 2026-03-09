# The Scenario: The JSON/Code Validator
# Imagine you are writing a tool that validates if a piece of code or a JSON object is 
# formatted correctly. You need to check if every opening bracket (, [, { has a corresponding
#  and correctly ordered closing bracket ), ], }.


def popinout(data):
    stack=[]
    for i in data :
                 
        if i=="(" or i == "[" or i=="{":
            stack.append(i)
            continue
        if i == ")" or i == "]" or i == "}":
            # SAFETY CHECK: If stack is empty and we see a closer, it's unbalanced
            if not stack:
                return False
            
        if i == ")" and stack[-1]=="(":
            stack.pop()
        elif i == "]" and stack[-1] == "[":
            stack.pop()
        elif i == "}" and stack[-1] == "{":
            stack.pop()
        else:
            return False 
    if len(stack) !=0:
        return False                   
    return True

data = "([{}])"        
answer = popinout(data)        
print(answer)