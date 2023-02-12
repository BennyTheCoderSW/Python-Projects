import random
import tkinter as tk
from datetime import date

#create arrays for elements
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
numbers = ['1','2','3','4','5','6','7','8','9']
special = ['!', '@', '#', '$', '%', '^', '&', '*', '(', ')',]

#shuffle algo for arrays
random.shuffle(alphabet)
random.shuffle(numbers)
random.shuffle(special)

#define variable for print
letters = (alphabet[0].upper()+alphabet[1]+alphabet[2]+alphabet[3]+alphabet[4].upper()+alphabet[5]+alphabet[6]+alphabet[7]+alphabet[8]+alphabet[9])
numbersout = (numbers[0]+numbers[1]+numbers[2]+numbers[3]+numbers[4])
special = (special[0]+special[1]+special[2])
variables = (letters+numbersout+special)
variables2 = str(variables)

#Print output to a text file
with open("user.txt", "a") as file:
    file.write("\n" + variables2)
    today = date.today()
    currentday = str(today)
    file.write("\n" + currentday)
    file.write("\n")