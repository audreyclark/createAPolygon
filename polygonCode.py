#Audrey Clark

import turtle

wn = turtle.Screen()
polygon = turtle.Turtle()

print("Welcome to Create a Polygon! Answer the following prompts to create fantastic drawings. You can exit by clicking on the screen")

playGame = True
while (playGame):
    #taking in number of sides the shape will have
    side = int(input("How many sides would you like your polygon to have?"))

    #taking in number of times the shape should repeat
    repeat = int(input("How many times would you like your polygon to repeat?"))

    #taking in the color of the shape
    color = input("What color would you like your polygon to be?")
    realColor = False
    while(not(realColor)):
        try:
            polygon.color(color);
            realColor = True
        except turtle.TurtleGraphicsError:
            color = input("Sorry, that's an incorrect color value. Try again: ")

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

wn.exitonclick() #allowing user to exit if the program stops responding
