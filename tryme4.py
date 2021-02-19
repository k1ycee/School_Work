#Assignment to show the nesting of multiple fuctions and also the use of functions. 
#Also the creating of custom functions.
def new_line():

    print('.')

def three_lines():

    new_line()

    new_line()

    new_line()

def nine_lines():
    three_lines()
    three_lines()
    three_lines()


def clear_screen():
    new_line()
    three_lines()
    nine_lines()

print("Printing Nine Lines \n")
#Calling the print nine_lines function
nine_lines()
print("\n Calling Clear Screen \n")
#Calling the print clear_screen function
clear_screen()
