import tkinter as tk
import Calculation



#Configuring the two windows
window = tk.Tk()
window.title("String-Mass System")
window.geometry("1100x800+400+0")

input_window = tk.Toplevel(window)
input_window.title("Inputs")
input_window.geometry("350x300+0+0")
input_window.config(padx=20,pady=20)

#Configuring the elements of the input windows
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

x0_label = tk.Label(input_window,text="x(0)(m):")
x0_label.grid(column=0,row=3)
x0_entry = tk.Entry(input_window)
x0_entry.grid(column=1,row=3)

xv0_label = tk.Label(input_window,text="x'(0)(m/s):")
xv0_label.grid(column=0,row=4)
xv0_entry = tk.Entry(input_window)
xv0_entry.grid(column=1,row=4)

start_button = tk.Button(input_window,text="start")
start_button.grid(column=1,row=5)
def button_pressed():
    m = float(m_entry.get())
    k = float(k_entry.get())
    b = float(b_entry.get())
    x0 = float(x0_entry.get())
    xv0 = float(xv0_entry.get())
    trial = Calculation.Calculation(m,k,b,x0,xv0)
    
start_button.config(command=button_pressed)



window.mainloop()