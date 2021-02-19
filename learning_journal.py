def countdown(n):
     if n <= 0:
          print('Blastoff!')
     else:
          print(n)
          countdown(n-1)
# Function that counts up from a negative number
def countup(n):
     if n >= 0:
          print(n)
          print('BlastUp!')
     else:
          print(n)
          countup(n+1)

number = int(input("Input a number: "))
if number < 0: 
    countup(number)
elif number > 0:
    countdown(number)
elif number == 0:
    print("You can't do a countdown with this number")


acceptNumberForCountDown()