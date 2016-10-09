#Audrey Clark Lab Time Tue @2pm
import turtle #importing the turtle library to use the drawing tool
wn = turtle.Screen() #creating screen to draw on
polygon = turtle.Turtle() #creating turtle to draw with
side = int(input("How many sides would you like your polygon to have?"))
#inputing an int value that will be used to calculate angles to make the polygon
for i in range(side):
    polygon.left((360/side)) #calculating angles by dividing 360 by number of sides
    polygon.forward(50)
wn.exitonclick() #allowing user to exit if the program stops responding
