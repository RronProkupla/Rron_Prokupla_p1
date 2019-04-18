import socket
import string
import collections
import sys
import datetime
import random
from _thread import *

#Funksioni qe llogarite numrin e bashkëtingelloreve duke testuar secilen shkronje se a i takon bashketigelloreve.

def CountCon(text):
    n = 0
    consonantslist = set(['B', 'C', 'D', 'F', 'G', 'H', 'J', 'K', 'L', 'M', 'N', 'P', 'R', 'Q', 'S', 'T', 'V', 'W', 'X', 'Z'])
    textu = text.upper()
    for i in textu:
        if i in consonantslist:
            n = n + 1
    return n

#Funksioni qe gjeneron 7 numra random duke perdorur funksione te librarise random.

def randomNum():
    n = " "
    for i in range(7):
        n = n + " " + str(random.randint(1, 49))
    n = n
    return n

#Funksioni Fibonacci

def Fibonacci(number):
    x = 0
    y = 1
    for i in range(number - 1):
        t = x + y
        x = y
        y = t
    return y

#Funksioni qe ben enkriptimin me Caesar

def Caesar(text,key):

    upper = collections.deque(string.ascii_uppercase)

    upper.rotate(-key)

    upper = ''.join(list(upper))

    return text.translate(str.maketrans(string.ascii_uppercase, upper))

#Funksioni qe llogarit shndrrimin e disa njesive

def Convert(text):
    t = str(text[text.find(' ') + 1:])
    unit = str(t[0:t.find(' ')])
    try:
        number = int(t[t.find(' ') + 1:])
    except ValueError:
        return "You should write a number to convert!"
    if unit == "KILOWATTTOHORSEPOWER":
        return number * 1.341
    elif unit == "HORSEPOWERTOKILOWATT":
        return number / 1.341
    elif unit == "DEGREESTORADIANS":
        return number * 0.01745
    elif unit == "RADIANSTODEGREES":
        return number / 0.01745
    elif unit == "GALLONSTOLITERS":
        return number * 3.785
    elif unit == "LITERSTOGALLONS":
        return number / 3.785
    else:
        return "Unit is wrong or not supported!"

#Funksioni qe rendit fjalet nga e funda deri tek fjala e pare

def renditjafjaleve(x):
    y = x.split()
    z = []
    for i in y:
        z.insert(0, i)
    return " ".join(z)

#Funksioni qe rendit fjalet dhe shkronjat nga fundi tek fillimi

def renditjashkronjave(x):
  word = ""
  for i in x:
    word = i + word
  return word

#krijimi  i socket instances i cili pranon ipv4 dhe punon me protokolin TCP

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = ''
port = 12000

#s.bind() lidh socketin me adresen perkatese

try:
    s.bind((host, port))
except socket.error:
    print("Binding failed")
    sys.exit()
print("Server started in port:", str(port))
s.listen(10)
print("Server ready to accept requests!")

def clinetthread(c,addr):

    while 1:

        input = c.recv(128).decode('utf-8')
        inputu = input.upper()
        if not inputu:
            break
        elif inputu == "IPADRESA":
            answer = "IP adresa e klientit: " + str(addr[0])
        elif inputu == "NUMRIIPORTIT":
            answer = "Porti që është duke e përdorur klienti: " + str(addr[1])
        elif inputu[0:inputu.find(' ')] == "BASHKETINGELLORE":
            input2 = inputu[inputu.find(' ') + 1:]
            answer ="Teksti i pranuar përmbanë " + str(CountCon(input2)) + " bashkëtingëllore"
        elif inputu[0:inputu.find(' ')] == "PRINTIMI":
            answer = inputu[inputu.find(' ') + 1:]
        elif inputu == "EMRIIKOMPJUTERIT":
            ip = addr[0]
            answer ="Emri i klientit/kompjuterit është: " + str(socket.getfqdn(ip))
        elif inputu == "KOHA":
            answer = datetime.datetime.now().strftime("%d.%m.%Y %H:%M:%S %p")
        elif inputu == "LOJA":
            answer = randomNum()
        elif inputu[0:inputu.find(' ')] == "FIBONACCI":
            numb = int(inputu[inputu.find(' ') + 1:])
            answer = Fibonacci(numb)
        elif inputu[0:inputu.find(' ')] == "KONVERTIMI":
            answer = Convert(inputu)
        elif inputu == "?":
            answer = '''IPADRESA -> IPADRESA 
NUMRIIPORTIT -> NUMRIIPORTIT 
BASHKETINGELLORE -> BASHKETINGELLORE <space> input text
PRINTIMI -> PRINTIMI <space> input text
EMRIIKOMPJUTERIT -> EMRIIKOMPJUTERIT
KOHA -> KOHA
LOJA -> LOJA
FIBONACCI -> FIBONACCI <space> input number
KONVERTIMI -> KONVERTIMI <space> input unit <space> input number 
CAESAR -> CAESAR <space> input key(number) <space> input text
? -> To show server commands
RENDITFJALET -> RENDITFJALET <space> input text
RENDITSHKRONJAT -> RENDITSHKRONJAT <space> input text
'''

        elif inputu[0:inputu.find(' ')] == "CAESAR":
            t = str(inputu[inputu.find(' ') + 1:])
            a = str(t[t.find(' ') + 1:])
            b = int(t[0:t.find(' ')])
            answer = Caesar(a, b)

        elif inputu[0:inputu.find(' ')] == "RENDITFJALET":
            t = str(inputu[inputu.find(' ') + 1:])
            rez = renditjafjaleve(t)
            answer = rez
        elif inputu[0:inputu.find(' ')] == "RENDITSHKRONJAT":
            t = str(inputu[inputu.find(' ') + 1:])
            rez = renditjashkronjave(t)
            answer = rez

        else:
            answer = "Wrong input!"
        print(inputu, addr)
        c.send(str.encode(str(answer)))
    c.close()

while 1:
    c, addr = s.accept()
    print("Client connected %s with port %s" % addr)

    #funksioni nga libraria thread qe mundeson qasjen dhe pranimin e kerkesave nga disa klient njekohesisht
    start_new_thread(clinetthread, (c, addr))
s.close()



