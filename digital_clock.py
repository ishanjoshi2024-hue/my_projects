import tkinter as tk   #gui library- create window, button etc
from time import strftime   

root = tk.Tk()  # root- creats a window
root.title("Digital Clock")

def time():
    string= strftime('%H:%M:%S %p\n%D')
    label.config(text=string) #config- change the properties of label
    label.after(1000,time)

label = tk.Label(
root,
font=('calibri', 35, 'bold'),
background= 'black', 
foreground= 'white'
) 

label.pack(anchor='center')  #pack- arrange elements inside window

time()

root.mainloop()