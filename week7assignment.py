def histogram(s):
     d = dict()
     for c in s:
          if c not in d:
               d[c] = 1
          else:
               d[c] += 1
     return d 


alphabet = "abcdefghijklmnopqrstuvwxyz"   


def get_values(duplicate):
    values = []
    for key, value in duplicate.items():
        values.append(value)
    return check_for_duplicate(values)


def check_for_duplicate(value):
    if max(value) > 1:
        return True
    else:
        return False


def has_duplicates():
    test_dups = ["zzz","dog","bookkeeper","subdermatoglyphic","subdermatoglyphics"] 
    for duplicate in test_dups:
        duplicate_hist = histogram(duplicate)
        if get_values(duplicate_hist):
            print(duplicate, "has duplicates")
        else: 
            print(duplicate, "has no duplicates")



# has_duplicates()
# check_for_duplicate()

# function missing_letters(abc) => new_string = defghijklmnopqrstuvwxyz ,
# 

def missing_letters(letters):
    all_letters_dict = histogram(alphabet)
    # for word in test_miss:
    #     for letters in word:


def get_letters():
    test_miss = ["zzz","subdermatoglyphic","the quick brown fox jumps over the lazy dog"] 
    letter_list = []
    for word in test_miss:
        print(word)
    return word


print(get_letters())