# Write a Python program that asks the user for the radius of a circle.
# Next, ask the user if they would like to calculate the area or circumference of a circle.
# If they choose area, display the area of the circle using the radius.
# Otherwise, display the circumference of the circle using the radius.
from tkinter import messagebox, simpledialog, Tk
import tkinter as tk
import math

window = Tk()
window.withdraw()

radius = simpledialog.askinteger(title='radius', prompt='enter a radius of a circle')
answer = simpledialog.askstring(title='radius', prompt='would you like to calculate the area or circumference of a circle?')
if answer=='area':
    area=math.pi*radius*radius
    messagebox.showinfo(title='area', message=area)
if answer=='circumference':
    circumference=2*math.pi*radius
    messagebox.showinfo(title='circumference', message=circumference)
#Area = πr^2
#Circumference = 2πr
