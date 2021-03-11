i = 1
def is_divisible(a, b):  # here the function will check if the value of the variable a is dividable by the value of # b
    return a % b == 0


def is_power(a, b):
    global i
    print("step "+str(i)+" - value of a: "+str(a),"value of b: "+str(b) +" remainder: "+str(a%b)) #Here the function will print each step of the calculation, demonstrating our method to verify if a number is a power of another.
    i += 1
    if a == 1:
        return True
    if b == 1:
        return False
    if not is_divisible(a,b):  #Here the values will be passed to the function is_dividable as part of the recursion to verify if they still dividable.
        return False
    return is_power(a / b,b)   #Here as a part of the recursion the function will divide a by b and call the function again till they will not be dividable or the result will be 1.


print("is_power(10, 2) returns: ", is_power(10, 2))
i = 1
print("is_power(27, 3) returns: ", is_power(27, 3))
i = 1
print("is_power(1, 1) returns: ", is_power(1, 1))
i = 1
print("is_power(10, 1) returns: ", is_power(10, 1))
i = 1
print("is_power(3, 3) returns: ", is_power(3, 3))