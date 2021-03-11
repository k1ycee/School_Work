def is_power(a, b):
    if is_divisible(a,b):
        return True
    elif a or b == 1 or a == b:
        return False
    else:
        is_power(a,b)

def is_divisible(x, y):
    return x % y == 0


print("is_power(10, 2) returns: ", is_power(10, 2))
print("is_power(27, 3) returns: ", is_power(27, 2))
print("is_power(1, 1) returns: ", is_power(1, 1))
print("is_power(10, 1) returns: ", is_power(10, 1))
print("is_power(3, 3) returns: ", is_power(3, 3))



def print_n(s, n):
    if n <= 0:
        return
    print(s)
    print_n(s, n-1)