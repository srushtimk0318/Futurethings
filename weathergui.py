import tkinter as tk

from weatherapi import fetch_weather
from tkinter.messagebox import showinfo


def fetchinfo():
    print("you clicked")
    cityname=strt1.get()
    
    result=fetch_weather(cityname)
    showinfo("wether report",result)    
    

window=tk.Tk()#tk->package and Tk->class


window.geometry('500x500')#def size by dimensions

window.title("Weather App")

lbl1=tk.Label(window,text="Enter city name",bg="cyan").place(x=50,y=100)#tk -> library, lbl->object of class Label

strt1=tk.StringVar()#to get inpput given->stringvar

t1=tk.Entry(window,textvariable=strt1).place(x=150,y=100)#textvariable->property, strt1->value, entry used to get value when we click on window

b1=tk.Button(window,text="Fetch weather info",command=fetchinfo).place(x=280,y=100)#command will define the class and used chick tyhe button then fetch the info by fetch weather info

window.config(bg="cyan")#changes the background color
window.mainloop()#display on box and keeps window active