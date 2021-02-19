#This is a simple fizzbuzz algorithm 
#It takes in any number and checks if th number is divivsible by 3,5 or 15 
#if it is divisible by 3 it prints fizz,
#if is is divisible by 5 it prints buzz,
#if it is divisible by 15 it prints fizzbuzz

def fizzbuzz(number):
    for i in range(number):
        if i%15 == 0:
            print("fizzbuzz")
        if i%3 == 0:
            print("fizz")
        if i%5 == 0:
            print("buzz")


