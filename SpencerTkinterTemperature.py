import tkinter as tk
from tkinter import messagebox


window = tk.Tk()

def GetTemp():
    numOne = entry.get()
    finalNum = float((float(numOne) - 32) * (5/9))
    messagebox.showinfo("Degrees Celcius", finalNum)

inputOne = tk.Label(window, text="Enter a temperature in Fahrenheit.",bg="black", fg="white")
inputOne.pack(fill=tk.X,pady=10)

entry = tk.Entry(window,bg="white",fg="black")
entry.pack(ipadx=10,pady=10)

button = tk.Button(text="Click to calculate", fg="red", command=GetTemp)
button.pack(fill=tk.X,pady=10)

window.mainloop()
