import tkinter
# Let's create the Tkinter window
window = tkinter.Tk()
window.title("GUI")

# creating a function called DataCamp_Tutorial()
def fn():
    tkinter.Label(window, text = "GUI with Tkinter!").pack()

tkinter.Button(window, text = "Click Me!", command = fn).pack()


#You will create three different functions for three different events
def left_click(event):
    tkinter.Label(window, text = "Left Click!").pack()

def middle_click(event):
    tkinter.Label(window, text = "Middle Click!").pack()

def right_click(event):
    tkinter.Label(window, text = "Right Click!").pack()

window.bind("<Button-1>", left_click)
window.bind("<Button-2>", middle_click)
window.bind("<Button-3>", right_click)
window.mainloop()