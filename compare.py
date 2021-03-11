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
        facto = n * factorial(n-1)
        return facto


def fibonacci(n):
    if n == 0:
        return 0;
    elif n == 1:
        return 1
    else:
        # print(n + "")
        return fibonacci(n - 1) + fibonacci(n-2)



# print(fibonacci(20))

def b(z):
    prod = a(z, z)
    print(z, prod)
    return prod
def a(x, y):
    x = x + 1
    return x * y
def c(x, y, z):
    total = x + y + z
    print(total)
    square = b(total)**2
    return square


x = 1
y = x + 1
print(c(x, y+3, x+y))