import turtle
from tkinter import messagebox, simpledialog, Tk

# Goal: Write a Python program that asks the user whether they want to
#       draw a triangle, square, or circle and then draw that shape.

if __name__ == '__main__':
    window = Tk()
    window.withdraw()
    
    # Make a new turtle
    shriya = turtle.Turtle()
    shriya.speed(20)
    # Ask the user what shape they want to draw and store it in a variable
    shape = simpledialog.askstring(title='shape', prompt='would you like to draw a triangle, square, or circle?')
    # Draw the shape requested by the user using if-elif-else statements
    if shape == 'triangle':
        for i in range(3):
            shriya.forward(100)
            shriya.right(120)
    elif shape == 'square':
        for i in range(4):
            shriya.forward(40)
            shriya.right(90)
    else:
        shriya.circle(15)
    # Call the turtle .done() method
