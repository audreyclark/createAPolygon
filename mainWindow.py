#test appjar

from appjar import gui
import turtle


app = gui("Main Window", "400x200")

app.addLabel("title", "Create a Polygon")
app.setLabelBg("title", "purple")

#number of sides
app.addLabelSpinBoxRange("Number of Sides", 1, 12)

#repeat the shape
app.addLabelSpinBoxRange("Number of Repeats", 1, 360)

#TODO: design to repeat the shape in (circle, line, zig-zag)

#pen color
app.addLabelEntry("Pen Color") #TODO: Catch bad input

def press(button):
    if button == "Quit":
        app.stop()
    else:
        sides = app.getSpinBox("Number of Sides")
        repeat = app.getSpinBox("Number of Repeats")
        color = app.getEntry("Pen Color")

app.addButtons(["Submit", "Quit"], press)

app.go() #don't put any code after this line
