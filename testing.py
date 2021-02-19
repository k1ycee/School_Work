def likes(names):
    length = len(names)
    if length <= 0:
        return "no one likes this"
    elif length >0 and  length<= 1:
        for i in range(length): 
            return names[i] + " likes this"
    elif length > 0 and  length<=2:
        for i in range(length):
            return names[i]  +  " and " +names[i]  + " like this"
    elif length > 0 and  length<=3:
        for i in range(length):
            return names[i] + " , " +names[i] + " and " +names[i]  + " like this"
    elif length > 3:
        for i in range(length):
            name = names[i] + " , " + names[i]
            return name + " and " + str(length) + " others like this"
        


print(likes(['Alex', 'Jacob', 'Mark']))