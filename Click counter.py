import tkinter as tk
from tkinter import IntVar


def on_click(event):
    cc = counter.get()
    cc += 1
    counter.set(cc)
    if cc > 999999:
        on_reset(event)


def on_reset(event):
    counter.set(0)

app = tk.Tk()
app.title("Click Counter")
app.geometry("200x210")
app.resizable(width=False, height=False)

counter = IntVar(value=0)
label = tk.Label(master=app, textvariable=counter, width=10, font="Calibri 50 bold")
label.pack()

control_frame = tk.Frame(master=app, background='green', width=350, height=120)
control_frame.pack()

canvas = tk.Canvas(master=control_frame, width=350, height=120)
canvas.pack()

click = canvas.create_oval(30, 5, 125, 110, fill="green")
reset = canvas.create_oval(130, 60, 180, 110, fill="red")

canvas.tag_bind(click, "<1>", on_click)
canvas.tag_bind(reset, "<1>", on_reset)

text1 = canvas.create_text(77, 58, text="Click", fill='#FF5733', font=("Helvetica", 20, "bold"))
text2 = canvas.create_text(155, 85, text="Reset", fill="black", font=("Helvetica", 10, "bold"))

canvas.tag_bind(text1, "<1>", on_click)
canvas.tag_bind(text2, "<1>", on_reset)

app.mainloop()
