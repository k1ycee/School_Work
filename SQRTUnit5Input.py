import math

#Part 1
def my_sqrt(a): #Pass on any number as an argument.
    x = a #This variable initializes x.
    while True: #Encapsulated from Section 7.5 my_sqrt example, remains unchanged for an accurate test_sqrt output.
        y = (x + a/x) / 2.0
        if x == y:
            break
        x = y
    return y

#Part 2
def test_sqrt(a): #Must pass on any number as an argument. The result may be the same but at least it would not cause any errors.
    while 26 > a: #Enables printing up to 25 a values. Should it be 25 > a, then it will print 24 a values.
        diff = my_sqrt(a) - math.sqrt(a)
        print('a =', a, '| my_sqrt(a) =', my_sqrt(a), '| math.sqrt(a) =', math.sqrt(a), '| diff =', abs(diff))
        a = a + 1 #Increments the print statement until 25 a values.




test_sqrt(26)