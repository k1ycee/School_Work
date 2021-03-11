# def any_lowercase1(s):
#      for c in s:
#           if c.islower():
#                return True
#           else:
#                return False


# # 2

# def any_lowercase2(s):
#      for c in s:
#           if 'c'.islower():
#                return 'True'
#           else:
#                return 'False'


# # 3

# def any_lowercase3(s):
#      for c in s:
#         flag = c.islower()
#      return flag


# # 4

# def any_lowercase4(s):
#      flag = False
#      for c in s:
#           flag = flag or c.islower()
#      return flag


# # 5

# def any_lowercase5(s):
#      for c in s:
#           if not c.islower():
#                return False
#      return True




# print(any_lowercase1("Oh my God, you killed Kenny"))
# print(any_lowercase2("Oh my God, you killed Kenny"))
# print(any_lowercase3("Oh my God, you killed Kenny"))
# print(any_lowercase4("Oh my God, you killed Kenny"))
# print(any_lowercase5("Oh my God, you killed Kenny"))

# Adds "done" to the list
# def add_done(listed):
#      listed.append("done")
#      return listed


# print(add_done([1, 2, 3,4]))

sentence = "This is a test statement woohoo"

def manipulate_string():
     split_tense = sentence.split(" ")
     split_tense.pop()
     del split_tense[1]
     split_tense.remove("test")
     split_tense.sort()
     split_tense.extend(["well", "modified now though"])
     split_tense.append("just stuff")
     split_tense[1] = "is a"
     new_sentence = " ".join(split_tense)
     print(new_sentence)

# manipulate_string()
# 

nested_list = ["Mahalo folks", 3, 5, 6, ["Sunflower", "Lillies", "Ixhora"]]
multiplied_list = [4, "lmao", "lol"] * 3
new_nested_list = nested_list[1:]

def add_letters(letter_list):
     word = ""
     for letter in letter_list:
          word += letter;
     return word

def remove_words(letter_list):
     letters = []
     for letter in letter_list:
          if len(letter) <= 1:
               letters.append(letter)
     return letters

# print(nested_list)
# print(multiplied_list)
# print(new_nested_list)
# print(remove_words(["wahala", "a", "b", "ginger", "p", "pi"]))
# print(add_letters(["a","l","o","h","a"]))




mylist = ["now", "four", "is", "score", "the", "and seven", "time", "years", "for"]
print(" ".join(mylist[1::2]))

mylist = [ [2,4,1], [1,2,3], [2,3,5] ]
total = 0
for sublist in mylist:
    total += sum(sublist)
print(total) 


mylist = [ [2,4,1], [1,2,3], [2,3,5] ]
a=0
total = 0
while a < 3:
    b = 0
    while b < 2:
        total += mylist[a][b]
        b += 1
    a += 1
print(total)

mylist = ["now", "four", "is", "score", "the", "and seven", "time", "years", "for"]
print(" ".join(mylist[1::2]))

mylist = ["now", "four", "is", "score", "the", "and seven", "time", "years", "for"]
a=0
while a < 8:
    print(mylist[a],)
    a = a + 2


