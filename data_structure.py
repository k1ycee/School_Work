import string
import PyPDF2
from gtts import gTTS 
import os



def open_pdf_file(page):
     pdfFile = open('test.pdf', "rb")
     pdfReader = PyPDF2.PdfFileReader(pdfFile) 
     pageToRead = pdfReader.getPage(page).extractText() 
     newPageWord = ""
     for word in pageToRead:
         if word not in string.punctuation:
             newPageWord = newPageWord + word
             
     return newPageWord


def read_text():
     language = 'en-US' #selecting language to use
     speech = gTTS(text = open_pdf_file(303), lang = language, slow = False) #calling the open_pdf_file with 303 as an argument
     speech.save("voice.mp3") #saving the text as an MP3 to the file system
     # os.system("start voice.mp3")


# read_text()
# print("jskhfsjdlfjsdhiiuvnfdjvfejh, sjiuihfihjv,sisihdish,".strip(string.punctuation))


# print(os.path.isfile("test.pdf"))

def check_for_file():
     file_name = str(input("Input file name: "))
     try:
          file = open(file_name)
          file == os.path.isfile("test.pdf")
     except IOError as error:
          print(error)
          
def check_inaccessible_path():
     path = str(input("Input file path: "))
     try:
          file = open(path, 'w')
          print(file)
     except PermissionError as error:
          print(error)

def check_read_only():
     path = str(input("Input file path: "))
     try:
          file = open(path)
     except IsADirectoryError as error:
          print(error)

check_for_file()
check_inaccessible_path()
check_read_only()