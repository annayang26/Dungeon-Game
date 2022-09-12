'''shapes.py
Anna Yang
2021 Spring 
CS151: visual media
lab09: this file is to create a parent Shape class and many child classes
'''

import turtle_interpreter
import lsystem
import time


class Shape:
    def __init__(self, distance=100, angle=90, color=(0, 0, 0),bgcolor = (0.1, 0.1, 0.44),lsysString=''):
        '''Shape constructor

        Parameters:
        -----------
        distance: float. Distance in pixels to go when moving the turtle forward
        angle: float. Angle in degrees to turn when turning the turtle left/right
        color: tuple of 3 floats. Default turtle pen color
        lsysString: str. The L-system string of drawing commands to draw the shape
            (e.g. made up of 'F', '+', '-', ...)
        '''

        # Create instance variables for all the parameters
        self.distance = distance
        self.angle = angle
        self.color = color 
        self.lsysString = lsysString
        self.bgcolor = bgcolor

        # Create an instance variable for a new TurtleInterpreter object
        self.terp = turtle_interpreter.TurtleInterpreter(bgColor = self.bgcolor)


    def getTI(self):
        ''' to get the TurtleInterpreter object
        
        return:
        --------
        the turtleinterpreter object 
        '''
        return self.terp 

    def getString(self):
        ''' to get the shape's L-system string
        
        return:
        --------
        the lsysString
        '''

        return self.lsysString

    def setColor(self, c):
        ''' to set the shape's color

        parameter:
        -----------
        c: tuple of 3 floats. the new pencolor of the terp
        '''
        self.color = c 

    def setDistance(self, dist):
        ''' to set the shape's edge distance

        parameter:
        -----------
        dist: float. the new edge distance of the shape
        '''
        self.distance = dist 

    def setAngle(self, a):
        ''' to set the turning angle of the shape

        parameter:
        -----------
        a: float. the new turning angle of the shape
        '''
        self.angle = a 

    def setString(self, s):
        ''' to set the L-system string

        parameter:
        ----------
        s: str. the new l-system string to draw in the shape
        '''
        self.lsysString = s 
    
    def draw(self, x_pos, y_pos, scale=1.0, heading=90):
        '''Draws the L-system string at the position `(x, y)` = `(x_pos, y_pos)` with the turtle
        facing the heading `heading`. The turtle drawing distance is scaled by `scale`.
        '''
        self.terp.goto(x_pos, y_pos, heading)
        self.terp.setColor(self.color) 
        self.terp.drawString(self.lsysString, self.distance * scale, self.angle)

class Square(Shape):
    def __init__(self, distance=100, color=(0, 0, 0), fill=False):
        ''' to draw a square
        
        parameters:
        ------------
        distance: int. the basic of unit of movement
        color: tuple. the color to fill
        fill: boolean. if true, fill the shape
        '''
        # Create a variable for the L-system string that would draw a square.
        squ_str = 'F-F-F-F'

        # if the fill parameter is true, concatenate the { and } characters
        # to the beginning and end of the L-system string,
        # updating the value of the L-system string.
        if fill:
            squ_str = "{" + squ_str + "}"

        # Call the parent's constructor, passing along values for all its parameters.
        super().__init__(distance=distance, angle = 90, color = color, lsysString=squ_str)

class PacMan(Shape):
    def __init__(self, distance = 100, fillColor = (1.0, 1.0, 0),angle= 30, fill = False):
        ''' circle constructor: can draw a pac-man (when angle is greater than 0) or a circle (when angle is 0)

        parameters:
        --------------
        distance: float. the radius of the pac-man/circle
        fillColor: tuple. the color to fill the pac-man
        fill: boolean. if True, fill the pac-man with color
        angle: int. how large the mouth of the pac-man might be
        penColor: boolean. if True, fill the color
        '''
        # the string that will draw a circle if angle = 0, or a pac-man if angle > 0
        pac_str = 'bY'
        
        # if fill is true, then the circle/pac-man will be filled 
        if fill:
            pac_str = "{" + pac_str + "}"
        
        # to call a shape constructor
        super().__init__(distance, angle, fillColor, lsysString = pac_str)

class Ghost(Shape):
    def __init__(self, distance =20, color= 'blue', penWidth = 1 , fill=False):
        ''' Ghost constructor: an octopus-shaped ghost

        parameter:
        -----------
        distance: float. the radius of the ghost head
        color: tuple. the fill color of the ghost body
        fill: boolean. if True, then fill the ghost with some color
        penWidth: int. the pen size
        '''
        # the string that will draw ghost
        ghost_str = 'b[HG]'
        
        # if fill is true, then the circle/pac-man will be filled 
        if fill:
            ghost_str = "{" + ghost_str + "}"

        # to draw the eyes
        ghost_str = ghost_str + 'E'
        
        # to call a shape constructor
        super().__init__(distance, angle=180, color = color, lsysString = ghost_str)

        # to set the pen width
        self.terp.turt.pensize(penWidth)

class Maze(Shape):
    def __init__(self, distance=100, angle=90, color = (0.1, 0.1, 0.44), penColor = (0.9, 0.9, 0.98)):
        ''' to draw a maze

        parameters: 
        -----------
        distance: int. the basic unit of movement
        angle: the turning angle of the maze, usually 90
        color: tuple. the color of the background
        penWidth: int. the pen size 
        penColor: tuple. the color of the pen. 

        '''
        # to make the lsystem string of the maze
        maze_str = '5FF-[++F[F+F[F+F]-F]-F[+FF[+F[--FF]-F]]-F-FF[F+F+FFFF+F]-F+F[FF+F+F]-F[+F-F]FF[+FFF-F-FF]]F-FF[F[+F-F+FF]FF-FF-F[+FF-FF]F-F-F]-F2'
        
        # to call the parent class constructor
        super().__init__(distance= 100, angle=90, color = penColor, lsysString=maze_str)
        
class Dot(Shape):
    def __init__(self, distance=1, color='yellow', fill = False):
        ''' to draw some dots in the maze

        parameters:
        -------------
        distance: int. the radius of the dot
        color: str. the pen color of the dot
        '''
        # the lsystem string of a dot/circle
        dot_str = 'c'

        # if fill is True, then fill in the color
        if fill:
            dot_str = '{' + dot_str +'}'

        # to call the parent constructor
        super().__init__(distance = distance, angle = 180,  color = color, lsysString=dot_str)

def testShape():
    ''' to test drawing the objects'''
    # to create the objects
    # the maze
    maze = Maze()

    # two pac-mans
    pac_man = PacMan(angle = 45, distance = 80)
    pac_man2 = PacMan(fill = True)

    # two ghosts
    ghost1 = Ghost(distance = 20, color = 'pink', fill = True)
    ghost2 = Ghost(distance = 25)

    # two dots
    dot1 = Dot(distance = 3, color = 'red', fill = True)
    dot2 = Dot(distance=1)

    # to draw the objects
    # the maze as the background
    maze.draw(0,0, heading = 0)

    # the pac-mans
    pac_man.draw(-100, -100)
    pac_man2.draw(-100, 100)

    # the ghosts
    ghost1.draw(0, -100)
    ghost2.draw(0, 100)

    # two dots
    dot1.draw(100, -100)
    dot2. draw(100, 100)

    # change the title of the screen
    maze.terp.screen.title('testShape')

    # the screen will close when the user clicks
    maze.getTI().hold()

def shapes():

    ''' to make the objects
    returns:
    -----------
    maze, pac_man, dots, ghost1, ghost2, ghost3
    '''

    # to make the shape objects 
    # the maze 
    maze = Maze()
    
    # to make some dots 
    dots = []
    for i in range(100):
        dots.append(Dot(1, 'yellow', fill=True))    
    
    # the pac-man    
    pac_man = PacMan(distance=20, angle = 60, fill = True)
    
    # three ghosts with different sizes and colors
    ghost1 = Ghost(distance= 20,fill=True, penWidth = 5, color = 'purple')
    ghost2 = Ghost(distance= 25,fill=True, penWidth = 1,color= 'green')
    ghost3 = Ghost(distance= 15,fill=True, penWidth = 3, color = 'yellow')
    
    # to return the objects created
    return maze, pac_man, dots, ghost1, ghost2, ghost3

def staticScene(maze, pac_man, dots, ghost1, ghost2, ghost3):
    ''' to draw the pac-man game (static)

    parameters:
    ------------
    maze: object. a maze object
    pac_man: object. a PacMan object
    dots: list. a list of dot objects
    ghost1: object. a ghost object
    ghost2: object. a ghost object
    ghost3: object. a ghost object
    '''

    # to draw the objects 
    maze.draw(-100,0, heading=0)

    # to draw some dots
    for x in range(10):
        for y in range(10):
            dots[x+y].draw(-430 + x*100, 430 - y*100)

    # to draw a pac-man and three ghosts
    pac_man.draw(-20, -250)
    ghost1.draw(-20,-50)
    ghost2.draw(20,-50)
    ghost3.draw(60, -50)

    # the screen will close when the user clicks
    maze.getTI().hold()

def animation(maze, pac_man, dots, ghost1, ghost2, ghost3):
    ''' add animation by changing the location when drawing and update the screen
    
    parameters:
    ------------
    maze: object. a maze object
    pac_man: object. a PacMan object
    dots: list. a list of dot objects
    ghost1: object. a ghost object
    ghost2: object. a ghost object
    ghost3: object. a ghost object
    '''
    # set the sleep time and the distance for each stride
    sleeptime = 1
    stride = 10

    # to draw the animation of the pac-man and three ghosts moving
    # the pac-man reaches the bottom by the end
    for i in range(10):
        # to save time, i chnaged the background pic to the screen shot of the maze object
        maze.terp.screen.bgpic('PacMan.gif')

        # to draw the objects at different location for each iteration
        pac_man.draw(-20, -250-i*stride)
        ghost1.draw(-20-i*stride,-50)
        ghost2.draw(20,-50+i*stride)
        ghost3.draw(60 - i*stride, -50)
        
        # to free the animation for a while
        time.sleep(sleeptime)

        # then to clean the screen
        maze.terp.screen.clearscreen()

        # turn off the tracer to speed up the drawing
        maze.terp.screen.tracer(False)

        # to update the screen
        maze.terp.screen.update()

    # to record the ending position of each object
    ghost1_x = -20 - 10*stride
    ghost2_y = -50+ 10*stride
    ghost3_x = 60 - 10*stride   

    # to change the direction
    # the pac-man will show up on the top
    for i in range(12):
        # to save time, i chnaged the background pic to the screen shot of the maze object
        maze.terp.screen.bgpic('PacMan.gif')

        # to draw the objects at different location for each iteration
        pac_man.draw(-20, 400-i*stride)
        ghost1.draw(ghost1_x-i*stride,-50)
        ghost2.draw(20,ghost2_y+i*stride)
        ghost3.draw(ghost3_x - i*stride, -50)
        
        # to free the animation for a while
        time.sleep(sleeptime)

        # then to clean the screen
        maze.terp.screen.clearscreen()

        # turn off the tracer to speed up the drawing
        maze.terp.screen.tracer(False)

        # to update the screen
        maze.terp.screen.update()

    # to record the ending position of each object
    pac_man_y = 400 -12*stride
    ghost1_x -= 12*stride
    ghost2_y += 12*stride
    ghost3_x -= 12*stride

    # change the direction of the objects 
    for i in range(10):
        # to save time, i chnaged the background pic to the screen shot of the maze object
        maze.terp.screen.bgpic('PacMan.gif')

        # to draw the objects at different location for each iteration
        pac_man.draw(-20-i*stride, pac_man_y)
        ghost1.draw(ghost1_x-i*stride,-50)
        ghost2.draw(20,ghost2_y-i*stride)
        ghost3.draw(ghost3_x, -50+i*stride)
        
        # to free the animation for a while
        time.sleep(sleeptime)

        # then to clean the screen
        maze.terp.screen.clearscreen()

        # turn off the tracer to speed up the drawing
        maze.terp.screen.tracer(False)

        # to update the screen
        maze.terp.screen.update()

    pac_man_x = -20-10*stride
    ghost1_x -= 10*stride
    ghost2_y -= 10 *stride
    ghost3_y = -50 + 10*stride

    # ghost 1 reaches the left side of th screen, so it will show up on the right
    # ghost 3 catches pac-man, game over
    for i in range(10):
         # to save time, i chnaged the background pic to the screen shot of the maze object
        maze.terp.screen.bgpic('PacMan.gif')

        # to draw the objects at different location for each iteration
        pac_man.draw(pac_man_x, pac_man_y - i *stride)
        ghost1.draw(380,-50 + i*stride)
        ghost2.draw(20 - i*stride, ghost2_y)
        ghost3.draw(ghost3_x, ghost3_y + i*stride )
        
        # to free the animation for a while
        time.sleep(sleeptime)

        # then to clean the screen
        maze.terp.screen.clearscreen()

        # turn off the tracer to speed up the drawing
        maze.terp.screen.tracer(False)

        # to update the screen
        maze.terp.screen.update()

    # set the backgroud to the game after the screen has been cleared 
    maze.terp.screen.bgpic('PacMan.gif')

    # let the user know the animation is over
    print('GAME OVER!')
    maze.terp.turt.pencolor('white')
    maze.terp.turt.write('Game Over!!!', align = 'Center', font = ('Arial', 50, 'normal'))

    # the screen will close when the user clicks
    maze.getTI().hold()

if __name__ == '__main__':
    # to test the shapes
    testShape()

    # to make the objects
    # maze, pac_man, dots, ghost1, ghost2, ghost3 = shapes()

    ''' NOTE: this function will draw a static picture'''
    # staticScene(maze, pac_man, dots, ghost1, ghost2, ghost3)

    ''' NOTE: this function will draw an animation, 
    but there might be constant flickering of the screen 
    due to the clearscreen() that changes the background color between blue and white'''
    # animation( maze, pac_man, dots, ghost1, ghost2, ghost3)


