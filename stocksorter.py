import requests
import json
import tkinter as tk
from datetime import date

# Create the main window
root = tk.Tk()
root.title("Stock Sorter Application")
root.geometry("500x500")

# Create 7 labels
label1 = tk.Label(root, text="Enter Stock Name: ", anchor="w")
label2 = tk.Label(root, text="", anchor="w")
label3 = tk.Label(root, text="", anchor="w")
label4 = tk.Label(root, text="", anchor="w")
label5 = tk.Label(root, text="", anchor="w")
label6 = tk.Label(root, text="", anchor="w")
label7 = tk.Label(root, text="", anchor="w")

# Place the labels in the main window
label1.place(x=50, y=50)
label2.place(x=50, y=75)
label3.place(x=50, y=100)
label4.place(x=50, y=125)
label5.place(x=50, y=150)
label6.place(x=50, y=175)
label7.place(x=50, y=200)

# Create a text box
textbox = tk.Entry(root)
textbox.place(x=200, y=50)

#button for generating sotck info
def on_button_click():
    stock = textbox.get()
    char = str(stock)[0]
    url = ('https://query1.finance.yahoo.com/v10/finance/quoteSummary/'+ char +'?modules=financialData')
    headers = {'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36'}
    result = requests.get(url, headers=headers)
    data = result.text
    parse_json = json.loads(data)
    financial_data = parse_json["quoteSummary"]["result"][0]["financialData"]
    current_price = financial_data["currentPrice"]['fmt']
    mean_price = financial_data["targetMeanPrice"]['fmt']
    low_price = financial_data["targetLowPrice"]['fmt']
    buyrange = ("Your buy range is between: " + mean_price + " and " + low_price)
    sellrange = ("Your sell range is between: " + mean_price + " and " + current_price)
    currentpriceoutput = "Current Price: " + current_price
    averagepriceoutput = "Average Price: " + mean_price
    lowpriceoutput = "Low Price: " + low_price
    label1.config(text="")
    label2.config(text=textbox.get())
    label3.config(text=currentpriceoutput)
    label4.config(text=averagepriceoutput)
    label5.config(text=lowpriceoutput)
    label6.config(text=buyrange)
    label7.config(text=sellrange)
    textbox.config(state=tk.DISABLED)
    today = date.today()
    currentday = str(today)
    
    #write to a text file 
    # Open the file in write mode
    with open(stock + ".txt", "a") as file:
    # Write to the file
        file.write(stock)
        file.write("\n" + currentpriceoutput)
        file.write("\n" + averagepriceoutput)
        file.write("\n" + lowpriceoutput)
        file.write("\n" + buyrange)
        file.write("\n" + sellrange)
        file.write("\n")
        file.write(currentday)
        file.write("\n")


# Create reset button
button2 = tk.Button(root, text="Generate Stock Info!", command=on_button_click)
button2.place(x=200, y=300)

def on_button_click2():
    label1.config(text="")
    label2.config(text="")
    label3.config(text="")
    label4.config(text="")
    label5.config(text="")
    label6.config(text="")
    label7.config(text="")
    textbox.config(state=tk.NORMAL)
    
#Create Reset button   
button2 = tk.Button(root, text="Reset", command=on_button_click2)
button2.place(x=235, y=350)

# Start the GUI event loop
root.mainloop()








