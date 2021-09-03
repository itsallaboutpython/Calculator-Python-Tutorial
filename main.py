import tkinter as tk
from playsound import playsound
import threading
from functools import partial

def beep_sound():
    playsound("beep.mp3")

def print_number(number):
    beep = threading.Thread(target=beep_sound)
    beep.start()
    output_textbox.configure(state=tk.NORMAL)
    output_textbox.insert(tk.END, str(number))
    output_textbox.configure(state=tk.DISABLED)

def evaluate():
    beep = threading.Thread(target=beep_sound)
    beep.start()
    expression = output_textbox.get()
    result = eval(expression)
    output_textbox.configure(state=tk.NORMAL)
    output_textbox.delete(0, len(expression))
    output_textbox.insert(tk.END, result)
    output_textbox.configure(state=tk.DISABLED)

def clear(event):
    output_textbox.configure(state=tk.NORMAL)
    output_textbox.delete(0, len(output_textbox.get()))
    output_textbox.configure(state=tk.DISABLED)

root = tk.Tk()
root.title("Calculator")
root.geometry("400x400")

root.bind("<Key-BackSpace>", clear)

root.grid_rowconfigure(0, weight=1)
root.grid_rowconfigure(1, weight=4)
root.grid_columnconfigure(0, weight=1)

output_frame = tk.Frame(root, width=400, height=100, background='red')
output_frame.grid(row=0, column=0, sticky=tk.NSEW)

button_frame = tk.Frame(root, width=400, height=300, background='green')
button_frame.grid(row=1, column=0, sticky=tk.NSEW)

for i in range(4):
    button_frame.grid_rowconfigure(i, weight=1)
    button_frame.grid_columnconfigure(i, weight=1)

output_textbox = tk.Entry(output_frame, font=("Calibri", 30), state=tk.DISABLED, disabledbackground='bisque', bg='bisque', fg='black')
output_textbox.pack(fill=tk.BOTH, expand=True)

button_one = tk.Button(button_frame, text="1", font=("Calibri", 20), width=6, bg="pink", fg="black")
button_one.configure(command=partial(print_number, 1))
button_one.grid(row=0, column=0, sticky=tk.NSEW)

button_two = tk.Button(button_frame, text="2", font=("Calibri", 20), width=6, bg="pink", fg="black")
button_two.configure(command=partial(print_number, 2))
button_two.grid(row=0, column=1, sticky=tk.NSEW)

button_three = tk.Button(button_frame, text="3", font=("Calibri", 20), width=6, bg="pink", fg="black")
button_three.configure(command=partial(print_number, 3))
button_three.grid(row=0, column=2, sticky=tk.NSEW)

button_four = tk.Button(button_frame, text="4", font=("Calibri", 20), width=6, bg="pink", fg="black")
button_four.configure(command=partial(print_number, 4))
button_four.grid(row=1, column=0, sticky=tk.NSEW)

button_five = tk.Button(button_frame, text="5", font=("Calibri", 20), width=6, bg="pink", fg="black")
button_five.configure(command=partial(print_number, 5))
button_five.grid(row=1, column=1, sticky=tk.NSEW)

button_six = tk.Button(button_frame, text="6", font=("Calibri", 20), width=6, bg="pink", fg="black")
button_six.configure(command=partial(print_number, 6))
button_six.grid(row=1, column=2, sticky=tk.NSEW)

button_seven = tk.Button(button_frame, text="7", font=("Calibri", 20), width=6, bg="pink", fg="black")
button_seven.configure(command=partial(print_number, 7))
button_seven.grid(row=2, column=0, sticky=tk.NSEW)

button_eight = tk.Button(button_frame, text="8", font=("Calibri", 20), width=6, bg="pink", fg="black")
button_eight.configure(command=partial(print_number, 8))
button_eight.grid(row=2, column=1, sticky=tk.NSEW)

button_nine = tk.Button(button_frame, text="9", font=("Calibri", 20), width=6, bg="pink", fg="black")
button_nine.configure(command=partial(print_number, 9))
button_nine.grid(row=2, column=2, sticky=tk.NSEW)

button_zero = tk.Button(button_frame, text="0", font=("Calibri", 20), width=6, bg="pink", fg="black")
button_zero.configure(command=partial(print_number, 0))
button_zero.grid(row=3, column=1, sticky=tk.NSEW)

button_plus = tk.Button(button_frame, text="+", font=("Calibri", 20), width=6, bg="pink", fg="black")
button_plus.configure(command=partial(print_number, "+"))
button_plus.grid(row=0, column=3, sticky=tk.NSEW)

button_minus = tk.Button(button_frame, text="-", font=("Calibri", 20), width=6, bg="pink", fg="black")
button_minus.configure(command=partial(print_number, "-"))
button_minus.grid(row=1, column=3, sticky=tk.NSEW)

button_multiply = tk.Button(button_frame, text="x", font=("Calibri", 20), width=6, bg="pink", fg="black")
button_multiply.configure(command=partial(print_number, "*"))
button_multiply.grid(row=2, column=3, sticky=tk.NSEW)

button_divide = tk.Button(button_frame, text="/", font=("Calibri", 20), width=6, bg="pink", fg="black")
button_divide.configure(command=partial(print_number, "/"))
button_divide.grid(row=3, column=3, sticky=tk.NSEW)

button_dot = tk.Button(button_frame, text=".", font=("Calibri", 20), width=6, bg="pink", fg="black")
button_dot.configure(command=partial(print_number, "."))
button_dot.grid(row=3, column=0, sticky=tk.NSEW)

button_equal = tk.Button(button_frame, text="=", font=("Calibri", 20), width=6, bg="pink", fg="black")
button_equal.configure(command=evaluate)
button_equal.grid(row=3, column=2, sticky=tk.NSEW)

root.mainloop()