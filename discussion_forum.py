#defining a function that takes an argument

def function_with_arguments(passed):
    print(passed)
#passed is a parameter "Lala Land" is an argument.
function_with_arguments("Lala Land")

#calling function_with_arguments with a value
function_with_arguments("Lala Land")
#calling function_with_arguments with a variable
age = "Sixty-Five"
function_with_arguments(age)
#calling function_with_arguments with an expression
sum_of_two_numbers = 45 + 3
function_with_arguments(sum_of_two_numbers)


# Function with a local variable 
x = 5
def multiplier(num):
    x = 4
    product = num*4 
    print(product)

# calling x a local variable of multiplier outside the function
print(x)
# Calling multiplier parameter outside the function
print(num)
multiplier(5)