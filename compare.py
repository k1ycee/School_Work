def compare(x,y):
    if x < y:
        return -1
    elif x > y:
        return 1
    elif x == y:
        return 0


def distance(x1, x2, y1, y2):
    x = (x1+x2)**2
    y = (y1+y2)**2
    print(x+y)
    dist = (x+y)**0.5
    return dist;


# print(distance(2,2,2,2))




def areBracketsBalanced(expr): 
    stack = [] 
  
    # Traversing the Expression 
    for char in expr: 
        if char in ["(", "{", "["]: 
  
            # Push the element in the stack 
            stack.append(char) 
        else: 
  
            # IF current character is not opening 
            # bracket, then it must be closing. 
            # So stack cannot be empty at this point. 
            if not stack: 
                return False
            current_char = stack.pop() 
            if current_char == '(': 
                if char != ")": 
                    return False
            if current_char == '{': 
                if char != "}": 
                    return False
            if current_char == '[': 
                if char != "]": 
                    return False
  
    # Check Empty Stack 
    if stack: 
        return False
    return True

# areBracketsBalanced(["(", "[", "("])


def factorial(n):
    if n == 0:
        return 1
    else:
        for i in range(n):
            facto = n * factorial(n-1)
        return facto


print(factorial(5))