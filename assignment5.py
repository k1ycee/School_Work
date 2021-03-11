from tabulate import tabulate
from math import sqrt

def my_sqrt(a):
    x = 7
    while True:
        y = (x + a/x) / 2
        if y == x:
            break
        x = y
    return x




def test_sqrt(x):
    a = 1
    while a <= x:
        results = ("a = ",a,"|","my_sqrt(a) = ",my_sqrt(a),"|","sqrt(a) = ",sqrt(a),"|","diff =",abs(my_sqrt(a) - sqrt(a)))
        print(results)
        a = a + 1
test_sqrt(30)
