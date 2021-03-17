def list_example(val1, val2):
   combined = list(zip(val1, val2))
   for index, tuple_value in enumerate(combined):
       couple = []
       couple.append((index, tuple_value))
       print(couple)


list_example([2,3,4,5,32,2,23,], "dhuhakjkals")
# print(list_example())



def dict_example(val):
    if isinstance(val, str):
        print(len(val))
        dict_value = dict(zip(val, range(len(val))))
        for key, value in dict_value.items():
            print("Key " + key, "Value " + str(value))
    else: 
        print("This is not a string")





dict_example("1002020")