import tkinter as tk
import subprocess
import time

window = tk.Tk()
window.title("String-Mass System")
window.geometry("1000x800+500+0")

input_window = tk.Toplevel(window)
input_window.title("Inputs")
input_window.geometry("400x600+0+0")

m_label = tk.Label(input_window,text="Mass(kg):")
m_label.grid(column=0,row=0)
m_entry = tk.Entry(input_window)
m_entry.grid(column=1,row=0)

k_label = tk.Label(input_window,text="k(N/m):")
k_label.grid(column=0,row=1)
k_entry = tk.Entry(input_window)
k_entry.grid(column=1,row=1)

b_label = tk.Label(input_window,text="b(kg/s):")
b_label.grid(column=0,row=2)
b_entry = tk.Entry(input_window)
b_entry.grid(column=1,row=2)

x0_label = tk.Label(input_window,text="x(0):")
x0_label.grid(column=0,row=3)
x0_entry = tk.Entry(input_window)
x0_entry.grid(column=1,row=3)

xv0_label = tk.Label(input_window,text="x'(0):")
xv0_label.grid(column=0,row=4)
xv0_entry = tk.Entry(input_window)
xv0_entry.grid(column=1,row=4)

window.mainloop()