#This is a commandline appointment creator
#Application use is to make a file to be copy and pasted to a sticky note to track appointments
#Will update applcation if information to write to a sticky note directly is found

#Prompt user for input
appointment = input("Please enter your appointment type: ")
location = input("Please enter location of appointment: ")
time = input("Please enter time of appointment: ")
date = input("Please enter date of appointment: ")



#Print input to a textfile
with open("appointments.txt", "a") as file:
    file.write(appointment)
    file.write("\n" + location)
    file.write("\n" + time)
    file.write("\n" + date)
    file.write("\n")