def nested_conditional():
    number = 100
    if number <= 1000:
        if number >=100:
            print("This is a hundreth number")


# nested_conditional()


def chained_conditional(name):
    if name == "Luke":
        print("Hi " + name)
    else:
        print("There is no record of this Individual")


# chained_conditional("Luke")


def nested_conditional_fixed():
    number = 100
    if number <= 1000 and number >=100:
        print("This is a hundreth number")


nested_conditional_fixed()