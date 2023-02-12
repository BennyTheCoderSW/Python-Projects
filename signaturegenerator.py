#Project to make a signature generator gui

import tkinter as tk

#Build Root
root = tk.Tk()
root.title("Signature Generator")
root.geometry("500x500")

#Build Labels
label1 = tk.Label(root, text="Greeting: ", anchor="w")
label2 = tk.Label(root, text="Name: ", anchor="w")
label3 = tk.Label(root, text="Position: ", anchor="w")
label4 = tk.Label(root, text="Phone Number: ", anchor="w")
label5 = tk.Label(root, text="Email: ", anchor="w")
label6 = tk.Label(root, text="", anchor="w")

#Place Labels
label1.place(x=50, y=50)
label2.place(x=50, y=75)
label3.place(x=50, y=100)
label4.place(x=50, y=125)
label5.place(x=50, y=150)
label6.place(x=100, y=400)

#Build Textboxes
textbox = tk.Entry(root)
textbox.place(x=200, y=50)
textbox2 = tk.Entry(root)
textbox2.place(x=200, y=75)
textbox3 = tk.Entry(root)
textbox3.place(x=200, y=100)
textbox4 = tk.Entry(root)
textbox4.place(x=200, y=125)
textbox5 = tk.Entry(root)
textbox5.place(x=200, y=150)

#Function for Generating a signature
def on_button_click():
    textbox.get()
    textbox2.get()
    textbox3.get()
    textbox4.get()
    textbox5.get()
    label1.config(text="")
    label2.config(text="")
    label3.config(text="")
    label4.config(text="")
    label5.config(text="")
    label6.config(text="Your Signature has been saved in the signature.txt file")
    textbox.config(state=tk.DISABLED)
    textbox2.config(state=tk.DISABLED)
    textbox3.config(state=tk.DISABLED)
    textbox4.config(state=tk.DISABLED)
    textbox5.config(state=tk.DISABLED)
    with open("signature.txt", "a") as file:
        file.write("\n")
        file.write(textbox.get())
        file.write("\n" + textbox2.get())
        file.write("\n" + textbox3.get())
        file.write("\n" + textbox4.get())
        file.write("\n" + textbox5.get())
        file.write("\n")

#Function for resetting the fields
def on_button_click2():
    label1.config(text="Greeting: ")
    label2.config(text="Name: ")
    label3.config(text="Position: ")
    label4.config(text="Phone Number: ")
    label5.config(text="Email: ")
    label6.config(text="")
    textbox.config(state=tk.NORMAL)
    textbox2.config(state=tk.NORMAL)
    textbox3.config(state=tk.NORMAL)
    textbox4.config(state=tk.NORMAL)
    textbox5.config(state=tk.NORMAL)

#Build Buttons  
button = tk.Button(root, text="Generate Signature", command=on_button_click)
button.place(x=200, y=300)
button2 = tk.Button(root, text="Reset", command=on_button_click2)
button2.place(x=100, y=300)

#main loops for gui
root.mainloop()