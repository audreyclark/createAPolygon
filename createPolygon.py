#Audrey Clark

import turtle

wn = turtle.Screen()
polygon = turtle.Turtle()
wn.exitonclick() #allowing user to exit if the program stops responding

class createPolygon(object):

    def start(sides, repeat, color):
        print("Drawing your shape now!")
        for j in range(repeat):
            for i in range(side):
                polygon.left((360/side)) #calculating angles by dividing 360 by number of sides
                polygon.forward(50)
            polygon.left((360/repeat))
        if(input("Would you like to create another polygon? (y/n)") != "y"):
            playGame = False
        else:
            print("Thanks for a great game!")
