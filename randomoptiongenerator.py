import random
import tkinter as tk

#This GUI Generates a random option from five inputs

#create the GUI

# 1x root
root = tk.Tk()
root.title("5 Choices GUI")
root.geometry("500x500")

# 5x textboxes
textbox1 = tk.Entry(root)
textbox1.place(x=200, y=50)
textbox2 = tk.Entry(root)
textbox2.place(x=200, y=100)
textbox3 = tk.Entry(root)
textbox3.place(x=200, y=150)
textbox4 = tk.Entry(root)
textbox4.place(x=200, y=200)
textbox5 = tk.Entry(root)
textbox5.place(x=200, y=250)

# 6x labels
label1 = tk.Label(root, text="1st Choice: ", anchor="w")
label2 = tk.Label(root, text="2nd Choice: ", anchor="w")
label3 = tk.Label(root, text="3rd Choice: ", anchor="w")
label4 = tk.Label(root, text="4th Choice: ", anchor="w")
label5 = tk.Label(root, text="5th Choice: ", anchor="w")
label6 = tk.Label(root, text="", anchor="w")
label1.place(x=50, y=50)
label2.place(x=50, y=100)
label3.place(x=50, y=150)
label4.place(x=50, y=200)
label5.place(x=50, y=250)
label6.place(x=200, y=350)

#method for button click
def on_button_click():
    option1 = textbox1.get()
    option2 = textbox2.get()
    option3 = textbox3.get()
    option4 = textbox4.get()
    option5 = textbox5.get()
    control_list = [option1, option2, option3, option4, option5]
    random.shuffle(control_list)
    choice = control_list[3]
    textbox1.config(state=tk.DISABLED)
    textbox2.config(state=tk.DISABLED)
    textbox3.config(state=tk.DISABLED)
    textbox4.config(state=tk.DISABLED)
    textbox5.config(state=tk.DISABLED)
    label6.config(text=choice)
    
#1x button
button = tk.Button(root, text="Get Your Answer!", command=on_button_click)
button.place(x=200, y=300)

#main loop
root.mainloop()