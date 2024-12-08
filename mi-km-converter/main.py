from tkinter import *

# creating the main window
window = Tk()
window.minsize(width=300, height=150)
window.title("Mi-Km Converter")

# creating labels
app_label = Label(text="mi to km converter".title(),font=("Arial", 15,))
app_label.grid(column=0, row=0)

converted_km = 0
# what happens when button get clicked
def confirm_clicked():
    global converted_km
    converted_km = round(float(user_input.get())*1.6,1)
    result_label.config(text=str(converted_km))

# creating buttons
my_button = Button(text="confirm", command=confirm_clicked)
my_button.grid(column=0, row=4)

# creating entry
user_input = Entry(width=10)
user_input.insert(END,string="0")
user_input.grid(column=0, row=2)
km_label = Label(text="Mi")
km_label.grid(column=1, row=2)

result_label = Label(text=0)
result_label.grid(column=0, row=3)

result_km = Label(text="Km")
result_km.grid(column=1, row=3)


# main loop of the program
window.mainloop()