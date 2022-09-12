'''asteroids.py
Anna Yang
CS151: visual media
Spring 2021
lab10: the file is to create the Game class
credit to Brian Marks on changing the Turtle shape. available at 
https://blog.trinket.io/using-images-in-turtle-programs/.
'''
import home
import turtle_interpreter
import turtle
import random

class Game:
    def __init__(self, speed = 20, angle = 10, numEnemies = 5, radar = 30, image = 'rocketship.gif'):
        ''' to create the Game object'''
        # to set the background with the scene created 
        home.testHome()

        # to show the screen
        self.screen = turtle_interpreter.TurtleInterpreter().getScreen()

        # to make a player
        self.image = image
        self.player = self.makePlayer(self.image)

        # to set up instance variables for speed and turning angle
        self.speed = speed
        self.angle = angle

        # to set a max and minimum boundary that the enemies can move
        self.left_max = -300
        self.up_max = 300
        self.right_max = 300
        self.bottom_max = -300

        # to make some enemies
        self.enemies = self.makeEnemies(numEnemies)

        # to set up a collision radius between the player and the enemy 
        self.radar = radar

        # to set up all the control buttons and events once the object is made
        self.setupEvents()

    def play(self):
        '''Turns the tracer animations on (but speeds up animations) and starts the main game loop.
        '''
        # Call the tracer method on your `Screen` instance variable,
        # passing in True as the parameter to turn animations on.
        self.screen.tracer(True)

        # Call the listen method on your `Screen` instance variable
        # so that keyboard presses are not registered as events
        self.screen.listen()

        # Call the mainloop method on your `Screen` instance variable.
        self.screen.mainloop()

    def makePlayer(self, image):
        ''' to create a main player

        parameter:
        -----------
        image: str. change the turtle shape to the image
        
        return:
        --------
        a turtle object
        '''

        # to create a turtle object as the main player
        player = turtle.Turtle()

        # to register the 'rocketship.gif' as the new turtle shape 
        self.screen.register_shape(image)

        # to change the turtle shape to the pic
        player.shape(image)

        # to pick the pen up and set it heading to the north
        player.penup()
        player.setheading(90)

        # to return the turtle
        return player

    def up(self):
        ''' to control the player to go forward'''
        # to move forward
        self.player.forward(self.speed)

    def down(self):
        ''' to control the player to go backward'''
        # to move backward
        self.player.backward(self.speed)

    def left(self):
        ''' to control the player to turn left'''
        # to turn left
        self.player.left(self.angle)

    def right(self):
        ''' to control the player to turn right'''
        # to turn right
        self.player.right(self.angle)

    def setupEvents(self):
        ''' to set up the events when the user presses the key'''
        # use the keys to control the rocketship/player
        self.screen.onkeypress(self.up, 'w')
        self.screen.onkeypress(self.down, 's')
        self.screen.onkeypress(self.right, 'd')
        self.screen.onkeypress(self.left, 'a')

        # ask the enemies to move randomly every 50 msec
        self.screen.ontimer(self.moveEnemiesRandomly, 50)

        # to check if the player has collided with any enemy
        self.screen.ontimer(self.checkForCollisions, 50)

        # the screen will close if the user press 'q'
        self.screen.onkeypress(turtle.bye, 'q')

    def placeEnemyRamdonly(self, turt):
        ''' move the turtle object to random coordinates within the enemy boundary'''

        # to move the enemy to random places within the coundary
        turt.goto(random.uniform(self.left_max, self.right_max), random.uniform(self.bottom_max, self.up_max))

    def makeEnemies(self, n):
        ''' create some enemies'''
        # to create a list to hold all the enemies
        enemies = []

        # to make n enemies
        for i in range(n):
            # change their shapes to square
            enemies.append(turtle.Turtle(shape = 'square'))

            # change their pencolor
            enemies[i].pencolor(random.random(), random.random(), random.random())

            # to pick up the pen
            enemies[i].penup()
            
            # place each randomly on the screen
            self.placeEnemyRamdonly(enemies[i])

        # to return the list
        return enemies

    def moveEnemiesRandomly(self):
        ''' to move enermies randomly'''

        # to set a random offset 
        offset = 10

        # to move each enemy in the list
        for enemy in self.enemies:
            # record the current position
            x_cor = enemy.xcor()
            y_cor = enemy.ycor()

            # move the enemy with a random offset
            enemy.goto(x_cor + random.randint(-offset,offset), y_cor + random.randint(-offset,offset))

        # to ask the enemy to move every 50 msce
        self.screen.ontimer(self.moveEnemiesRandomly, 50)

    def checkForCollisions(self):
        ''' to check for collision between the player and the enemy'''
        # to check every enemy
        for enemy in self.enemies:
            # to record the current position of the player and the enemy
            player_x = self.player.xcor()
            player_y = self.player.ycor()
            enemy_x = enemy.xcor()
            enemy_y = enemy.ycor()

            # if their distance is smaller than the distance set up by the self.radar
            # then the program will print BOOM! and move the collided enemy to another place
            if abs(player_x - enemy_x) < self.radar and abs(player_y - enemy_y) < self.radar:
                print('BOOM!!!')
                self.placeEnemyRamdonly(enemy)

        # to check every 50 msec
        self.screen.ontimer(self.checkForCollisions, 50)

if  __name__ == '__main__':
    game = Game()
    game.play()