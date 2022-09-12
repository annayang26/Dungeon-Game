'''home.py
Anna Yang
CS151: visual media
Spring 2021
Project 09: this file is to create a scene representing home
'''
from shapes import Shape
import shapes

class Stool(Shape):
    def __init__(self, distance = 25, angle = 30, length = 6, color= 'brown', fill= False):
        ''' to create a stool

        parameters:
        -----------
        distance: int. the radius of the stool and the length of the legs (would time 4 when draw the circle)
        angle: int. the angle to draw the chair back (would time 2 when actually the circle)
        length: int. similar to scale. how long the chair leg will be 
        color: str. the color name string to fill the chair back
        fill: boolean. if True, fill the stool with color
        '''

        # the l system string of the stool
        # the seat part: 2bH++cD0F + 02FF + 02F+++F
        # the leg part: [---5DDD[0FF] + D*length] + [---5DDD + D*length]
        stool_str = '2bH++cD0F[---5DDD[0FF]' + length * 'D' + ']02FF[---5DDD' + length *'D' + ']02F+++F'

        # if fill is true, fill the chair back with color
        if fill:
            stool_str = '{' + stool_str + '}'

        # to call the parent class
        super().__init__(distance, angle, color, bgcolor= 'white',lsysString = stool_str)

class Light(Shape):
    def __init__(self, distance = 10 , angle = 45, length = 30, color= 'grey', fill= False):
        ''' to draw some lighting

        parameters:
        -----------
        distance: int. the radius of the light and the length of the lightbulb (would time 4 when draw the circle)
        angle: int. the angle to draw the light bulb (would time 2 when actually the circle)
        length = int. the length of the cord connecting to the lightbulb
        color: str. the color name string to fill the lamp cover
        fill: boolean. if True, fill the light with color
        '''
        # the lsystem string of the light
        light_str = 'D--cFFFcFcFFFcHF'

        # if fill is true, then fill the color
        if fill:
            light_str = '{' + light_str + '}'        
        
        # finally add the cord connecting the light
        light_str = 'b'+ length*'D' + light_str + 'b'+ length * 'F'
        
        # to call the Shape constructor to draw the light
        super().__init__(distance, angle, color, bgcolor= 'white',lsysString = light_str)

class Table(Shape):
    def __init__(self, distance = 5 , angle = 45, width = 5, length = 80, leg = 50, color= 'gray', fill= False):
        ''' to create a long table

        parameters:
        -----------
        distance: int. the radius of the round corner of the table
        angle: int. the angle of the corner of the table
        width: int. the scale of the width side
        length: int. similar to scale. how long the chair leg will be 
        leg: int. the scale of the length of the leg times distance
        color: str. the color name string to fill the table back
        fill: boolean. if True, fill the table with color
        '''

        # the l system string of the stool
        # the table part: 
        table_str = 'bD' + 'c' + 'F'* (length//4)  + '[' +'D'*leg + '0'+ 'F' *(length//8)+'H' + 'F'*leg + ']0' + 'F'*(length//8) +'F' * (length//2) + '[' +'D'*leg + '0' +'F' *(length//8)+'H' + 'F'*leg + ']0' + 'F'*(length//8) +'F' * (length//4) +'c' +  'F' + 'c' + (length//4*5) * 'F' + 'c'


        # if fill is true, fill the table with color
        if fill:
            table_str = '{' + table_str + '}'

        # to call the parent class
        super().__init__(distance, angle, color, bgcolor= 'white',lsysString = table_str)

class Parallelogram(Shape):
    def __init__(self, distance=50, length = 14, width = 1, color='Beige', angle = 60,fill=False):
        ''' to draw a parallelogram
        parameter:
        -----------
        distance: int. the basid unit of movement
        length: int. the scale of the length (vertical) of the shape
        width: int. the scale of the width (horizontal) of the shape
        color: str. color str name. 
        angle: int. the angle of the shape.
        fill: boolean. if true, fill in the color
        '''

        # Create a variable for the L-system string that would draw a parallelogram.
        wall_str = 'F' * length + '-' + 'F' * width + (180-angle)//angle *'-' + 'D'*length + '-' + 'F'*width
        
        # if the fill parameter is true, concatenate the { and } characters
        # to the beginning and end of the L-system string,
        # updating the value of the L-system string.
        if fill:
            wall_str = "{" + wall_str + "}"

        # Call the parent's constructor, passing along values for all its parameters.
        super().__init__(distance=distance, angle = angle, color = color,bgcolor= 'white', lsysString=wall_str)

class CoffeeMachine(Shape):
    def __init__(self, distance=5, color='black', angle = 45,fill=False):
        ''' to draw a coffee machine

        parameters:
        -----------
        distance: int. the basid unit of movement
        color: str. color string name
        angle: the turning angle of the corner as well as used in drawing the circle
        fill: boolean. if true, fill in the color

        '''
        # Create a variable for the L-system string that would draw a square.
        cm_str = '0FFFFFFFFFFFFFFFF--FFFFFFFFFFFFFFFFFFF--FFFFFFFFFFFFFFFF--FFFFFFFFFFFFFFFFFFF'        
        
        # if the fill parameter is true, concatenate the { and } characters
        # to the beginning and end of the L-system string,
        # updating the value of the L-system string.
        if fill:
            cm_str = "{" + cm_str + "}"

        # add the coffee bean grinder on the top
        cm_str += '[--FFFFFFFFFFF++e{bFFF0cFFF[FF++FFFFFFFFFFFFFFDD]++FFFFFFFFFFFFFFDDDcDDD++FFFFFF}'

        # add the cup holder on the coffee machine
        cm_str += ']--FFF++5FF--FFFFFFFFFF--FF2'

        # Call the parent's constructor, passing along values for all its parameters.
        super().__init__(distance=distance, angle = angle, color = color, bgcolor= 'white',lsysString=cm_str)

class Logo(Shape):
    def __init__(self, distance=2, color='brown', angle= 108, fill=False):
        ''' to draw the logo of Starbucks

        parameters:
        -------------
        distance: int. the basic unit of the movement
        color: str. the color to fill
        angle: the turning angle of the shape
        fill: boolean. if true, fill the color
        '''
        # logo_str = '0<g{c}>HuFFFd'
        # the star part
        logo_str = '0FFFFFFFFFF++FFFFFFFFFF++FFFFFFFFFF++FFFFFFFFFF++FFFFFFFFFF'

        # the band
        logo_str += 'uDDDDDDDDd[[DD0FFFFFFFFFHFF]0FFFFFFFFF'

        # the R
        logo_str += ']uDDDDDD0FFd5DDDDDDDDDHFFF[-c]-FFFFFF2'


        super().__init__(distance = distance, angle = angle, color=color,bgcolor= 'white', lsysString=logo_str)

def testHome():
    ''' to create the scene in Starbucks'''
    # to create the objects 
    # the internal design of the cafe
    wall = Parallelogram(fill=True)
    ceiling = Parallelogram(angle = 90, length = 2, width = 12,fill=True)
    decor = Parallelogram(angle=90, length= 1, width = 11, color= 'black', fill=True)
    
    # to change the title
    wall.terp.screen.title('A Home outside Home')

    # the counter
    bar_top = Parallelogram(distance = 20,angle = 90, length =1, width = 20, color = 'Dim Gray', fill = True)
    bar_bottom = Parallelogram(angle = 90, length = 3, width = 8, color = 'Wheat', fill =True)

    # the cashier 
    bar_top1 = Parallelogram(distance = 20,angle = -60, length =1, width = 5, color = 'Dim Gray', fill = True)
    bar_bottom1 = Parallelogram(angle = -60, length = 3, width = 3, color = 'Wheat', fill =True)

    # to create the poster on the wall
    poster_frame = Parallelogram(distance = 10, length = 10, width = 6, color = 'Sandy Brown',angle = -60, fill = True)
    poster = Parallelogram(distance = 10, length = 8, width = 4, color = 'Green',angle = -60, fill = True)

    # the stools at the back of the table
    stool_back_list = []
    for i in range(2):
        stool_back_list.append(Stool(length =5, color = 'Dark Slate Blue',fill =True))

    # the hanging light
    light = Light()
    light1 = Light(length = 40, fill=True)
    light5 = Light(length = 38, color = 'Light Steel Blue', fill = True)
    
    # to make some coffee machines
    cm = CoffeeMachine(fill = True)

    # set one of the coffee machine to gray
    cm.setColor('gray')

    # to DRAW the objects 
    # the wall
    ceiling.draw(-400,300, heading = 90)  
    decor.draw(-430,340, heading = 90) 
    wall.draw(-400, -300, heading=90)

    # the coffee machine
    cm.draw(50,150, heading=0)       
    
    # the bar
    bar_top.draw(-100,55)
    bar_bottom.draw(-100, -100)

    # the cashier
    bar_top1.draw(393, 5)
    bar_bottom1.draw(435,-175)

    # the poster on the wall
    poster_frame.draw(390,230)
    poster.draw(380,240)

    # the back stools
    for i in range(len(stool_back_list)):
        stool_back_list[i].draw(-260 + i *140, 0, heading =0)

    # the hanging light
    light.draw(-300,350, scale = 0.6)
    light1.draw(-250, 350, scale = 0.4)
    light5.draw(40, 350, scale = 0.5)


if __name__ == '__main__':
    testHome()