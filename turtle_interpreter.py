'''turtle_interpreter.py
Anna Yang
CS151: visual media
proj08: classes
this file is to create a class for turtle instruction
'''
import turtle

import random

class TurtleInterpreter:

    # make the turt and screen global variables
    turt = turtle.Turtle()
    screen = turtle.Screen()
    
    def __init__(self, width=800, height=800, bgColor='white'):
        '''TurtleInterpreter constructor.
        Creates instance variables for a Turtle object and a Screen object with a particular window
        `width`, `height`, and background color `bgColor`.
        '''
        # Set the screen's height, width, and color based on the parameters
        TurtleInterpreter.screen.setup(width, height)

        TurtleInterpreter.screen.bgcolor(bgColor)

        # Turn the screen's tracer off.
        TurtleInterpreter.screen.tracer(0)

        # to hide the turtle
        TurtleInterpreter.turt.hideturtle()

    def setColor(self,c):
        ''' set the turtle's pen color to the color 'c'

        parameter:
        ----------
        c: str. color string name. the pen color of the turtle
        '''
        # to set the pen color
        TurtleInterpreter.turt.color(c) 

    def setWidth(self, w):
        ''' set the turtle's pen width to the int 'w'
        '''
        # to set the pen width
        TurtleInterpreter.turt.pensize(w) 

    def goto(self, x, y, heading= None):
        ''' create a goto function that places the turtle at (x,y) 
        and sets the heading to heading if the value of the heading parameter passed in is not None
        
        parameter:
        -----------
        x: int. x-coordinate of the position
        y: int. y-coordinate of the position
        heading: int. the head direction the turtle will be facing. by default, it is none
        '''

        # to go to the position
        TurtleInterpreter.turt.penup()
        TurtleInterpreter.turt.goto(x, y)
        TurtleInterpreter.turt.pendown()

        # to set the heading if the 'heading' parameter is not none
        if heading:
            TurtleInterpreter.turt.setheading(heading)
    
    def getScreen(self):
        ''' will return the screen object
        return:
        ----------
        the screen object
        '''
        return TurtleInterpreter.screen

    def getScreenWidth(self):
        ''' get the width of the screen
        
        return:
        ---------
        int. the width of the screen
        '''

        # to get the width
        return TurtleInterpreter.screen.window_width()

    def getScreenHeight(self):
        ''' get the height of the screen
        
        return:
        ---------
        int. the height of the screen
        '''

        # to get the width
        return TurtleInterpreter.screen.window_height()

    def hold(self):

        '''Holds the screen open until user clicks or presses 'q' key'''

        # Hide the turtle cursor and update the screen
        TurtleInterpreter.turt.hideturtle()
        TurtleInterpreter.screen.update()

        # Close the window when users presses the 'q' key
        TurtleInterpreter.screen.onkey(turtle.bye, 'q')

        # Listen for the q button press event
        TurtleInterpreter.screen.listen()

        # Have the turtle listen for a click
        TurtleInterpreter.screen.exitonclick()
    
    def drawString(self, lsysString, distance, angle):
        '''Interpret each character in an L-system string as a turtle command.

        Here is the starting L-system alphabet:
            F is forward by a certain distance
            + is left by an angle
            - is right by an angle

        Parameters:
        -----------
        lsysString: str. The L-system string with characters that will be interpreted as drawing
            commands.
        distance: distance to travel with F command.
        angle: turning angle (in deg) for each right/left command.
        '''
        # to create an empty list to store the current turtle state (position and heading)
        curr_pos = []

        # to create an empty list to hold the color state
        colorStack = []

        # Walk through the lsysString character-by-character and
        # have the turtle object (instance variable) carry out the
        # appropriate commands
        for char in lsysString:

            # if the char is F, the turtle moves forward
            if char == 'F':
                TurtleInterpreter.turt.forward(distance)

            # if the char is +, the turtle turns left
            elif char == '+':
                TurtleInterpreter.turt.left(angle)

            # if the char is -, the turtle turns right
            elif char == '-':
                TurtleInterpreter.turt.right(angle)

            # if the char is [, append the current position and heading to the list
            elif char == '[':
                curr_pos.append(TurtleInterpreter.turt.pos())
                curr_pos.append(TurtleInterpreter.turt.heading())
                
            # if the char is ], the turtle goes to the previous position with the saved heading 
            elif char == ']':
                prev_heading = curr_pos.pop()
                prev_pos = curr_pos.pop()
                self.goto(prev_pos[0], prev_pos[1], prev_heading)

            # to save the current turtle color state
            elif char == '<':
                colorStack.append(TurtleInterpreter.turt.color()[0])
            
            # to restore the previous turtle color state
            elif char == '>':
                TurtleInterpreter.turt.pencolor(colorStack.pop())

            # to have the turtle start filling
            elif char == "{":
                TurtleInterpreter.turt.begin_fill()

            # to have the turtle stop filling
            elif char == '}':
                TurtleInterpreter.turt.end_fill()

            # to set the turtle's color to green
            elif char == 'g':
                TurtleInterpreter.turt.color((0.49, 0.99, 0), (0.49, 0.99, 0))
            
            # to set the turtle's color to yellow (gold)
            elif char == 'y':
                TurtleInterpreter.turt.color('yellow','yellow')
            
            # to set the turtle's color to red (crimson)
            elif char == 'r':
                TurtleInterpreter.turt.color((0.86, 0.08, 0.24),(0.86, 0.08, 0.24))

            # to set the turtle's color to dark orange
            elif char == 'o':
                TurtleInterpreter.turt.color((1.0, 0.55, 0),(1.0, 0.55, 0))

            # to set the turtle's color to pink
            elif char == 'p':
                TurtleInterpreter.turt.color((1.0, 0.75, 0.8),(1.0, 0.75, 0.8))

            # to set the pencolor to black
            elif char == 'b':
                TurtleInterpreter.turt.pencolor('black')

            # to set the turtle's color to spring green
            elif char == 'n':
                TurtleInterpreter.turt.color('spring green', 'spring green')

            # to set the turtle's color to peru
            elif char == 'e':
                TurtleInterpreter.turt.color('peru', 'peru')
            
            # to draw a leaf at the current turtle position
            elif char == 'L':
                # # to fill the leave with color
                # TurtleInterpreter.turt.pencolor('green')

                #the shape of the leave
                TurtleInterpreter.turt.circle(distance,80)
                TurtleInterpreter.turt.left(100)
                TurtleInterpreter.turt.circle(distance,80)
                TurtleInterpreter.turt.left(140)
                TurtleInterpreter.turt.forward(distance)

                # the stem 
                # the upper stem
                TurtleInterpreter.turt.backward(distance/5)
                TurtleInterpreter.turt.right(45)
                TurtleInterpreter.turt.forward(distance/5)
                TurtleInterpreter.turt.backward(distance/5)
                TurtleInterpreter.turt.left(90)
                TurtleInterpreter.turt.forward(distance/5)
                TurtleInterpreter.turt.backward(distance/5)

                # the bottom stem
                TurtleInterpreter.turt.left(135)
                TurtleInterpreter.turt.forward(distance/4)
                TurtleInterpreter.turt.right(150)
                TurtleInterpreter.turt.forward (distance/4)
                TurtleInterpreter.turt.backward(distance/4)
                TurtleInterpreter.turt.right(90)
                TurtleInterpreter.turt.forward(distance/6)

            # to draw a berry (cherry) at the current turtle position
            elif char == 'B':
                # to speed up the drawing
                TurtleInterpreter.turt.speed(0)
                
                # to get the starting position of the turtle so that it can come back later
                x_corr = TurtleInterpreter.turt.xcor()
                y_corr = TurtleInterpreter.turt.ycor()
                heading = TurtleInterpreter.turt.heading()
                
                # to draw the cherry
                def cherry(facing = True):
                    ''' to draw a cherry with its stem
                    parameter:
                    facing: boolean. the direction the cherry face when drawing its stem. by default it's facing left
                    '''

                    #to draw the stem
                    # if the cherry faces the left 
                    if facing:
                        TurtleInterpreter.turt.pencolor('saddle brown')
                        TurtleInterpreter.turt.circle(distance/3, 150)
                        TurtleInterpreter.turt.setheading(180)

                        # to draw the cherry
                        TurtleInterpreter.turt.color('crimson', 'crimson')
                        TurtleInterpreter.turt.begin_fill()
                        TurtleInterpreter.turt.circle(distance/8)
                        TurtleInterpreter.turt.end_fill()
                    
                    # if the cherry grows toward the right
                    else: 
                        # draw the stem, but the turtle will draw in clockwise direction 
                        TurtleInterpreter.turt.pencolor('saddle brown')
                        TurtleInterpreter.turt.circle(distance/3, -150)
                        TurtleInterpreter.turt.setheading(180)

                        # to draw the cherry
                        TurtleInterpreter.turt.color('crimson', 'crimson')
                        TurtleInterpreter.turt.begin_fill()
                        TurtleInterpreter.turt.circle(distance/8)
                        TurtleInterpreter.turt.end_fill()

                # there will at least one cherry on the branch
                TurtleInterpreter.turt.setheading(150)
                cherry()

                # create a list that contain two facing options of the cherry (to the left or to the right)
                facing = [True, False]

                # 50% chance there will be two cherries 
                if random.random() >0.5:
                    self.goto(x_corr, y_corr, 160+angle)

                    # and randomly assign how the cherry grow (toward the right or the left)
                    cherry(random.choice(facing))

                # 30 % chance there will be a third cherry
                elif random.random() >0.7:
                    self.goto(x_corr, y_corr, 180+ angle)

                    # with random facing direction 
                    cherry(random.choice(facing))

                # return to the starting point, with the original heading 
                TurtleInterpreter.turt.penup()
                self.goto(x_corr, y_corr, heading)
                TurtleInterpreter.turt.pendown()

                TurtleInterpreter.screen.update()

            # to draw a flower bloosm at the current turtle position
            elif char == 'M':
                def pedal():
                    TurtleInterpreter.turt.circle (distance/2,80)
                    TurtleInterpreter.turt.left(120)
                    TurtleInterpreter.turt.forward (distance/3)
                    TurtleInterpreter.turt.right(120)
                    TurtleInterpreter.turt.forward(distance/3)
                    TurtleInterpreter.turt.left (120)
                    TurtleInterpreter.turt.circle(distance/2,80)

                TurtleInterpreter.turt.color('red', 'pink')
                TurtleInterpreter.turt.begin_fill()

                for i in range(5):
                    pedal()
                    TurtleInterpreter.turt.left(150)

                TurtleInterpreter.turt.end_fill()

            # to draw some buds
            elif char == 'A':

                TurtleInterpreter.turt.color('dark orange', 'dark orange')
                TurtleInterpreter.turt.begin_fill()
                TurtleInterpreter.turt.left(30)
                for i in range(3):
                    TurtleInterpreter.turt.forward(distance/4)
                    TurtleInterpreter.turt.right(60)
                TurtleInterpreter.turt.end_fill()
            
            # to mark the top of the plant
            elif char == 'T':
                TurtleInterpreter.turt.dot(1) 

            # the turtle move down
            elif char == 'D':
                TurtleInterpreter.turt.setheading(-90)
                TurtleInterpreter.turt.forward(distance)

            # fruit development 1
            elif char == 'C':
                TurtleInterpreter.turt.setheading(120)
                TurtleInterpreter.turt.color('orange red', 'orange red')
                TurtleInterpreter.turt.begin_fill()
                TurtleInterpreter.turt.forward(distance/3)
                TurtleInterpreter.turt.right(120)
                TurtleInterpreter.turt.forward(distance/3)
                for i in range(5):
                    TurtleInterpreter.turt.left(150-20*i)
                    TurtleInterpreter.turt.forward(distance/4)
                    TurtleInterpreter.turt.backward(distance/4)

                TurtleInterpreter.turt.setheading(-60)
                TurtleInterpreter.turt.forward(distance/3)
                TurtleInterpreter.turt.right(60)
                TurtleInterpreter.turt.forward(distance/3)

                TurtleInterpreter.turt.end_fill()

            # to mark the intersection 
            elif char == 'I':
                pass
            
            # set the heading to 90 degrees
            elif char == 'H':
                TurtleInterpreter.turt.setheading(90)
            
            # draw more branches and leaves
            elif char == 'O':
                TurtleInterpreter.turt.dot(1)

            # draw a bird
            elif char == "N":
                # to draw the wing of the bird
                x=TurtleInterpreter.turt.xcor()
                y = TurtleInterpreter.turt.ycor()
                TurtleInterpreter.turt.setheading(-45)
                TurtleInterpreter.turt.circle(distance*4,60)
                TurtleInterpreter.turt.left(125)
                TurtleInterpreter.turt.forward(distance*5)
                TurtleInterpreter.turt.setheading(100)

                # to draw the head and beak of the bird
                TurtleInterpreter.turt.circle(distance,135)
                TurtleInterpreter.turt.right(30)
                TurtleInterpreter.turt.forward(distance/2)
                TurtleInterpreter.turt.left(120)
                TurtleInterpreter.turt.forward(distance/2)
                TurtleInterpreter.turt.right(60)

                # to draw the rest of the body
                TurtleInterpreter.turt.circle(distance*4, 120)
                TurtleInterpreter.turt.right(30)
                TurtleInterpreter.turt.forward(distance*3)
                TurtleInterpreter.turt.circle(distance/5,170)
                TurtleInterpreter.turt.forward(distance*3)

                # to draw the eyes
                self.goto(x-distance, y+distance*2.5)
                TurtleInterpreter.turt.circle(distance/5)

            # NOTE: updated afterwards for Project09
            # to draw pac-man
            elif char == 'Y':
                # to record the position 
                x_cor = TurtleInterpreter.turt.xcor()
                y_cor = TurtleInterpreter.turt.ycor()
                
                # if the angle is zero, then this alphabet only draws a circle
                TurtleInterpreter.turt.setheading(90 + angle/2)
                TurtleInterpreter.turt.circle(distance, 360-angle)

                # if angle is greater than 0, then this will draw a pac-man
                # to draw the mouth
                if 0 < angle <= 30: 
                    TurtleInterpreter.turt.left(angle*3)
                elif angle > 30:
                    TurtleInterpreter.turt.left(90+angle/3)

                TurtleInterpreter.turt.forward(distance)
                TurtleInterpreter.turt.goto(x_cor, y_cor)

            # to draw some ghosts
            elif char == 'G':
                # to draw the body of the ghost
                TurtleInterpreter.turt.circle(distance,180)
                TurtleInterpreter.turt.forward(distance/2)

                # to draw the legs
                for i in range(4):
                    TurtleInterpreter.turt.circle(distance/4,180)
                    TurtleInterpreter.turt.left(180)
                TurtleInterpreter.turt.left(180)
                TurtleInterpreter.turt.forward(distance/2)

            # to draw the eyes of the ghost
            elif char == 'E':
                # define a function to draw eyes
                def eye():
                    TurtleInterpreter.turt.color('black', 'white')
                    TurtleInterpreter.turt.begin_fill()
                    TurtleInterpreter.turt.circle(distance/4)
                    TurtleInterpreter.turt.end_fill()
                    TurtleInterpreter.turt.color('black', 'black')
                    TurtleInterpreter.turt.begin_fill()
                    TurtleInterpreter.turt.circle(distance/8)
                    TurtleInterpreter.turt.end_fill()

                # to record the starting position
                x_cor = TurtleInterpreter.turt.xcor()
                y_cor = TurtleInterpreter.turt.ycor()

                # to draw the eyes
                for i in range(2):
                    self.goto(x_cor- distance *(i+1), y_cor+distance/3, -90)
                    eye()
            
            # to lift the pen up
            elif char == 'u':
                TurtleInterpreter.turt.penup()
            
            # to put the pen down
            elif char == 'd':
                TurtleInterpreter.turt.pendown()
            
            # to draw a circle
            elif char == 'c':
                TurtleInterpreter.turt.circle(distance*4, angle*2)
            
            # to set the heading towards east
            elif char == '0':
                TurtleInterpreter.turt.setheading(0)
            
            # to set the pensize to 5
            elif char == '5':
                TurtleInterpreter.turt.pensize(5)
            
            # to set the pensize to 2
            elif char == '2':
                TurtleInterpreter.turt.pensize(2)
            
            # Call the update method on the screen object to make sure
            # everything drawn shows up at the very end of the method
            # (remember: you turned off animations in the constructor)
            TurtleInterpreter.screen.update()
