# Importing required modules
import random
import time
from os import path
from os import system

# Setting console color and title
# Defining possible characters
system('color 3')
system("title "+'Phone Numbers by Scott')
numList = "0123456789"
idList = ["086", "096", "097", "098", "032", "033", "034", "035", "036", "037", "038", "039", "091", "094", "083", "084", "085", "081", "082", "089", "090", "093", "070", "079", "077", "076", "078", "092", "056", "058", "099", "059"]
password = "123456"

amount = int(input("Nhap so luong so dien thoai can tao: "))

# Generate random number
def randNum():
    num = random.randint(0,9)
    return(str(num))

# Generate random id
def randID():
    ID = random.choice(idList)
    return(ID)

# Create number and password
def NumGen():
    numID = randID()
    num = "" + numID
    while len(num) < 10:
        randnum = randNum()
        num += randnum
    result = num + ":" + password
    return(result)

# Create new file if already exists
def File():
    name = "phonecombo.txt"
    x = 1
    while path.exists(name):
        name = "phonecombo(" + str(x) + ").txt"
        x = x + 1
    return name

f = open(File(),"w+")

# Write numbers to file   
for i in range(amount):
    number = NumGen()
    f.write(number + "\n")
    print(i," . ",number)
    #time.sleep(0.0005)

f.close()
