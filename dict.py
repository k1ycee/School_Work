def histogram(s):
    d = dict()
    for c in s:
        if c not in d:
            d[c] = 1
        else:
            d[c] += 1
    return d

# print(histogram("ebelebe"))



def invert_dict(d):
    inverse = dict()
    for key in d:
        val = d[key]
        if val not in inverse:
            inverse[val] = [key]
        else:
            inverse[val].append(key)
    return 
    



def fibonacci(n):
    known = {0:0, 1:1}
    if n in known:
        return known[n]
    res = fibonacci(n-1) + fibonacci(n-2)
    known[n] = res
    return res

# print(fibonacci(9))
directory = {
    ('Cleese', 'John'): '08700 100 222',
    ('Chapman', 'Graham'):'08700 100 222',
    ('Idle', 'Eric'):'08700 100 222',
    ('Jones', 'Terry'):'08700 100 222',
    ('Gilliam', 'Terry'):'08700 100 222',
    ('Palin', 'Michael'): '08700 100 222'
}

for name, number in directory.items():
    # print(name, number)
    names = []
    names.append(name)
    for first, last in names:
        print(first + " "+ last)