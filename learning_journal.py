# import PyPDF2
# from gtts import gTTS 
# import os
# def countdown(n):
#      if n <= 0:
#           print('Blastoff!')
#      else:
#           print(n)
#           countdown(n-1)
# # Function that counts up from a negative number
# def countup(n):
#      if n >= 0:
#           print(n)
#           print('BlastUp!')
#      else:
#           print(n)
#           countup(n+1)

# number = int(input("Input a number: "))
# if number < 0: 
#     countup(number)
# elif number > 0:
#     countdown(number)
# elif number == 0:
#     print("You can't do a countdown with this number")


# acceptNumberForCountDown()



# def hypoteneus(a,b):
#      h = a**2 + b**2
#      print(h, "sum of the product of 'a' and 'b'")
#      dist = h ** 0.5
#      print(dist, "is the length of the hypoteneus")
#      return dist

# # print(hypoteneus(3,4))
# # print(hypoteneus(2,3))
# # print(hypoteneus(6,5))





# def open_pdf_file(page):
#      pdfFile = open('test_material.pdf', "rb") #hard-coding a specific book into the program
#      pdfReader = PyPDF2.PdfFileReader(pdfFile) #reading the pdffile
#      pageToRead = pdfReader.getPage(page).extractText() # picking a particular page to read   
#      # print(pdfReader.getPage(page).extractText(), "Content of the page argument") 
#      return pageToRead


# def read_text():
#      language = 'en-US' #selecting language to use
#      speech = gTTS(text = open_pdf_file(303), lang = language, slow = False) #calling the open_pdf_file with 303 as an argument
#      speech.save("voice.mp3") #saving the text as an MP3 to the file system
#      # os.system("start voice.mp3")


# read_text()

# def traversal():
#      prefixes = 'JKLMNOPQ'
#      suffix = 'ack'
#      for letter in prefixes:
#           word = letter + suffix
#           if(word == "Oack"):
#                word = "Ouack" #re-assigning the generated to a new word
#           elif(word == "Qack"):
#                word = "Quack" #re-assigning the generated to a new word
#           print(word)

# # traversal()


# # name1 = "hannah"
# # print(name1[5:])

# # name2 = "sinzu"
# # print(name2[0:len(name2) -1])

# # name3 = "basketmouth"
# # print(name3[6: len(name3)])

# n = 10
# while n != 1:
#     print (n,)
#     if n % 2 == 0: # n is even
#         n = n // 2
#     else: # n is odd
#         n = n * 3 + 1

# def subroutine( n ):
#     while n > 0:
#         print (n,)
#         n = n - 1

# subroutine(10)
animal_shellter = {
  "Teddy": ["dog",4,"male"],
  "Elvis": ["dog",1,"male"],
  "Sheyla": ["dog",5,"female"],
  "Topic": ["hamster",3,"male"],
  "Kuzya": ["cat",10,"male"],
  "Misi": ["cat",8,"female"],
}


print(animal_shellter.items())


# def invert(d):
#   inverse = dict()
#   for key in d:
#     val = d[key]
#     for item in val:
#       if item not in inverse:
#         inverse[item] = [key]
#       else:
#         inverse[item].append(key)
#   return inverse 





# def invert_file_content():
#     with open("dict.txt") as file_content:
#          inverted_file = invert(dict(eval(file_content.read())))
#          string_inverted_file = str(inverted_file)
#          write_to_file(string_inverted_file)

# def write_to_file(file):
#     new_file = open("inverted_dict.txt", "w")
#     new_file.write(file)

# # invert_file_content()


# fin = open('dict.txt')
# for line in fin:
#     print(type(fin))
#     print(type(line))
#     word = line.strip()
#     print(type(word))
#     print(word)



try:
    fin = open('answer.txt')
    fin.write('Yes')
except:
    print('No')
print('Maybe')



n = 10
while n != 1:
    print (n,end=' ')
    if n % 2 == 0:        # n is even
        n = n // 2
    else:                # n is odd
        n = n * 3 + 1



mylist = ["now", "four", "is", "score", "the", "and seven", "time", "years", "for"]
a=0
while a < 7:
    print (mylist[a],)
    a += 2

mylist = [ [2,4,1], [1,2,3], [2,3,5] ]
a=0
b=0
total = 0
while a <= 2:
    while b < 2:
        total += mylist[a][b]
        b += 1
    a += 1
    b = 0 
print (total)

index = "Ability is a poor man's wealth".find("w")
print(index)



while True:

    while 1 > 0:

        break

    print("Got it!")

    break


# def recurse(a):
#     if (a == 0):
#         print(a)
#     else:
#         recurse(a) 

# recurse(1)


mylist = [ [2,4,1], [1,2,3], [2,3,5] ]
total = 0
for sublist in mylist:
    total += sum(sublist)
print(total) 

