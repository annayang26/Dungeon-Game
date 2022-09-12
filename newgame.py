'''newgame.py
Anna Yang
CS151: visual media
Spring 2021
Project 10: design a video game
'''

import turtle_interpreter
import random
import turtle
from asteroids import Game

class Adventure(Game):

    # to make a global variable: player's health point
    player_HP = 50
    enemy_num = 5

    def __init__(self, speed =20, radar = 150, avatar = 0):
        ''' to make a new game
        in which, the user will control the avatar 
        to explore a cave and to collect the items necessary for pass the level
        there will also be some moving enemies, which the user can escape away
            or use the weapon/abilities collected to kill the enemy and get some money
        the avatar will also change as the player obtained certain items
        the goal is to save a friend who was lost

        NOTE: you can only have one weapon/ability

        parameters:
        -----------
        speed: int. how much distance the player can move with one press
        radar: int. how far away can the player detect the item or the enemy to detect the player
        avatar: int. 0-3, which avatar the player chose to use
        '''
        # to create a screen object
        self.screen = turtle_interpreter.TurtleInterpreter().getScreen()
        self.screen.bgpic('cave.gif')

        # to make a list for the images of the enemies and one for items
        self.avatar_list = ['girl.gif', 'boy.gif' ,'penguin.gif','kiwi.gif']
        enemies_image = ['spider.gif', 'mouse.gif', 'frog.gif', 'bear.gif', 'tiger.gif']
        item_image = ['apple.gif', 'money.gif', 'milk.gif']
        weapon_image = ['flame.gif', 'gun.gif', 'snowflake.gif']
        
        # to make a player with the avatar the user chooses
        self.player = self.makePlayer(self.avatar_list[avatar])
        
        # to make some enemies, items, weapons 
        # each is a dictionary with turtle object as the key
        # and corresponding name as the value
        self.enemies = self.makeEnemies(enemies_image)
        self.items = self.makeItems(item_image)
        self.weapons = self.makeWeapons(weapon_image)

        # make an instance variable for friend
        self.friend = self.makeAFriend()

        # one for map
        self.map = self.makeAMap()
        self.items[self.map] = 'map'

        # and one for flag
        self.exit = self.makeExit()
        self.items[self.exit] = 'flag'
        
        # make some recorder turtles on the screen to record HPs of the player and the enemies
        # as well as the event happened
        self.player_rec = self.makeRecorder(-380, 350)
        self.item_rec = self.makeRecorder(-380, 300)
        self.enemy_rec = self.makeRecorder(250, 350)
        self.narrator = self.makeRecorder(-380, -350)

        # to record the current player position 
        self.player_x = 0
        self.player_y = 0

        # to record the last enemy encountered
        self.curr_enemy = ''

        # the collision radius between the enemy and the player that will trigger the attack method
        self.radar = radar
        self.speed = speed

        # to make some instance variables for the bag and weapon
        self.bag = []
        self.weapon = ''  

        # to call the setupEvents method to play the game by pressing keys
        self.setupEvents()

    def moveUp(self):
        '''Moves the player up by `self.speed`
        '''
        self.player.setheading(90)
        self.player.forward(self.speed)

    def moveDown(self):
        '''Moves the player down up by `self.speed`
        '''
        self.player.setheading(270)
        self.player.forward(self.speed)

    def moveLeft(self):
        '''Moves the player left by `self.speed`
        '''
        self.player.setheading(180)
        self.player.forward(self.speed)
    
    def moveRight(self):
        '''Moves the player right by `self.speed`
        '''
        self.player.setheading(0)
        self.player.forward(self.speed)
    
    def makeEnemies(self, enemies_image):
        ''' to make some enemies
        
        parameters:
        ------------
        n: int. the number of enemies in the game
        enemies_image: list. a list of names of the pictures to use as the shapes of the enemy turtle

        return:
        --------
        a dict. keys are the enemy object and the value is a list of its name/identity and its HP
        '''

        # to create an empty to take enemies and a dict to hold the identity
        enemies = []
        identity = {}

        # to make enemies and change their shape to the image
        for i in range(5):
            # make turtle object
            enemies.append(turtle.Turtle())

            # change shape
            self.screen.register_shape(enemies_image[i])
            enemies[i].shape(enemies_image[i])

            # store identity
            identity[enemies[i]] = [enemies_image[i].replace('.gif', '')]

            # to give different enemies different HP
            # spide has the lowest
            if identity[enemies[i]][0] == 'spider':
                identity[enemies[i]].append(4)

            # the mouse has some more
            elif identity[enemies[i]][0] == 'mouse':
                identity[enemies[i]].append(4)

            # the bear has the most
            elif identity[enemies[i]][0] == 'bear':
                identity[enemies[i]].append(4)
            
            # the tiger has some too
            elif identity[enemies[i]][0] == 'tiger':
                identity[enemies[i]].append(4)
            
            # the frog has the second least
            else:
                identity[enemies[i]].append(4)

            # place these enemeis randomly on the screen
            self.placeEnemyRamdonly(enemies[i])

        # return the dictionary
        return identity
        
    def checkForCollisions(self):
        ''' to check for collision between the player and the enemy'''

        # to check every enemy
        for enemy, identity in self.enemies.items():
            # to record the current position of the player and the enemy
            enemy_x = enemy.xcor()
            enemy_y = enemy.ycor()

            encounter = False

            # if their distance is smaller than the distance set up by the self.radar
            # then the program will warn the player about the enemy
            if abs(self.player_x - enemy_x) < self.radar and abs(self.player_y - enemy_y) < self.radar:
                self.curr_enemy = identity[0]
                self.chase(enemy, self.player)
                encounter = True

            # if they are closer, the program will warn the player agin
            if self.radar/2 > abs(self.player_x - enemy_x) and self.radar/2 > abs(self.player_y - enemy_y):
                event = 'You were attacked by ' + identity[0] + ' :('
                self.recordEvents(self.narrator, event)
                self.loseBlood(identity[0], self.player)
            
            # if encountered, report that on the screen
            if encounter:
                
                event = 'You have encountered ' + identity[0] + ' !!!'
                self.recordEvents(self.narrator, event)

        # to check every 50 msec
        self.screen.ontimer(self.checkForCollisions, 50)
            
    def placeEnemyRamdonly(self, turt):
        ''' to place enemy randomly on several assigned places
        
        parameter:
        ----------
        turt: turtle object. the enemy that will be placed randomly on the screen
        '''

        # to set some fixed position where there will be enemies
        enemy_locations = [[-300, 200], [-40, 30], [-250, -300], [360, 150], [280, -180]]

        # to pick the pen up
        turt.penup()

        # to put it randomly at one of the position on the screen
        turt.goto(random.choice(enemy_locations)[0], random.choice(enemy_locations)[1])

    def checkPosition(self):
        ''' to check the position of the player'''
        # to check the player's position
        self.player_x = self.player.xcor()
        self.player_y = self.player.ycor()

        # to keep checking every 50 msec
        self.screen.ontimer(self.checkPosition, 50)

    def checkExit(self):
        ''' to check if the player and the friend have arrived at the exit/flag safely'''

        # to check the position of the exit
        exit_x = self.exit.xcor()
        exit_y = self.exit.ycor()

        # to check the position of the friend
        friend_x = self.friend.xcor()
        friend_y = self.friend.ycor()

        # if the friend has arrived at the flag or the player has reached the flag, the game is over
        if abs(friend_x - exit_x) < 20 and abs(friend_y - exit_y) < 20 or 'flag' in self.bag:
            self.endGame()

        # keep checking
        self.screen.ontimer(self.checkExit, 200)
              
    def chase(self, hunter, prey): 
        ''' the enemy/friend will move towards the player'''

        # set the enemy that is in the collision radius heading to the player
        hunter.setheading(hunter.towards(prey))

        # if it is the enemy chasing the player
        if hunter is self.enemies:
            # to check the identity of the enemy
            # and set them chase the player at different speed
            if hunter == 'tiger':
                hunter.forward(4)
            elif hunter == 'bear':
                hunter.forward(3)
            elif hunter == 'spider':
                hunter.forward(1)
            elif hunter == 'mouse':
                hunter.forward(2)
            else:
                hunter.forward(3)

        # else if it is bullet chasing the enemy (player shooting bullet to the enemy)
        else:
            hunter.forward(10)

    def makeItems(self, item_image):
        ''' to make items
        
        parameter:
        ------------
        item_image: list. a list of images that the turtle can change shape to
        
        return:
        --------
        a dict that contain the item/object as key and its name as value
        '''

        # to create an empty dict to hold both the things and identity
        things_dict = {}

        # to make the items
        for i in range(len(item_image)):
            item = turtle.Turtle()

            # to change the shape of the turtle object
            self.screen.register_shape(item_image[i])
            item.shape(item_image[i])

            # to add the thing and the name to the dictionary
            things_dict[item] = item_image[i].replace('.gif', '')

            # to place the item randomly 
            self.placeItems(item)

        # return the dictionary
        return things_dict

    def makeWeapons(self, weapon_image):
        ''' to make weapons
        
        parameter:
        ------------
        weapon_image: list. a list of images that the turtle can change shape to
        
        return:
        --------
        a dict that contain the weapon/object as key and its name as value
        '''

        # to create an empty dict to hold both the things and identity
        weapon_dict = {}

        # to make the weapons
        for i in range(len(weapon_image)):
            weapon= turtle.Turtle()

            # to change the shape of the turtle object
            self.screen.register_shape(weapon_image[i])
            weapon.shape(weapon_image[i])

            # to add the thing and the name to the dictionary
            weapon_dict[weapon] = weapon_image[i].replace('.gif', '')

            # to place the item randomly 
            self.placeItems(weapon)
        
        # to return the dictionary
        return weapon_dict

    def makeAFriend(self):
        ''' to make a friend object that the player need to save'''
        # to make a friend object
        friend = turtle.Turtle()

        # to change its shape to one of the avatar
        friend_shape = random.choice(self.avatar_list)
        self.screen.register_shape(friend_shape)
        friend.shape(friend_shape)

        # to place the friend object randomly
        self.placeItems(friend)

        friend.hideturtle()

        return friend

    def placeItems(self, turt):
        ''' to place different items randomly
        
        parameter:
        ----------
        turt: turtle object. the item that will be placed randomly on the map
        '''
        # to pick the pen up
        turt.penup()

        # to put it randoml
        turt.goto(random.uniform(-350, 350), random.uniform(-300, 300))

    def makeRecorder(self, x, y):
        ''' to make some turtle objects to record the blood of the player, the items the player collected
        the blood of the enemy that player is attacking
        
        parameters:
        -----------
        x: int. x cor where the recorder will stay
        y: int. y cor where the recorder will stay

        return:
        -------
        a turt object
        '''

        # to make a turtle object
        recorder = turtle.Turtle()

        # to pick up the pen
        recorder.penup()

        # to make it goto the top left of the screen
        recorder.goto(x, y)

        # to return the object
        return recorder

    def recordEvents(self, turt, event):
        ''' to record the blood of the player
        
        parameter:
        ------------
        turt: turtle object. to indicate which recorder to record
        event: str. the thing to write on the screen
        '''
        # to clear the number written
        turt.clear()
        turt.pencolor((1.0, 1.0, 1.0))

        # to write the current blood
        turt.write(event, font = ('Arial', 20, 'normal'))

        # to hide the turt
        turt.hideturtle()

    def makeBullets(self):
        ''' to make some bullets so that the player can attack the enemy
        
        return:
        ----------
        a turt object
        '''

        # its shape depends on the weapon/ability
        # flame
        if self.weapon == 'flame':
            bullet = turtle.Turtle()
            self.screen.register_shape('flame_bullet.gif')
            bullet.shape('flame_bullet.gif')

        # snowflake
        elif self.weapon == 'snowflake':
            bullet = turtle.Turtle()
            self.screen.register_shape('snowflake_bullet.gif')
            bullet.shape('snowflake_bullet.gif')
        
        # gun
        elif self.weapon == 'gun':
            bullet = turtle.Turtle()
            bullet.shape('circle')
        
        else: 
            event = "You don't have any weapon now. So... RUN!!!"
            self.recordEvents(self.narrator, event)

        # to pick up the pen and go to where the player is 
        bullet.penup()
        bullet.hideturtle()
        bullet.goto(self.player_x, self.player_y)
        bullet.showturtle()

        # to return the bullet 
        return bullet
                           
    def checkHP(self):
        ''' to check player HP'''

        # to record player's HP
        player_HP = 'Your HP: '+ str(Adventure.player_HP)
        self.recordEvents(self.player_rec, player_HP)

        # if the player has 0 HP, end the game
        if Adventure.player_HP <= 0:
            self.loseGame()

        # to keep checking
        self.screen.ontimer(self.checkHP, 500)

    def checkEnemyHP(self, turt):
        ''' to check enemy HP

        parameter:
        -----------
        turt: object. the enemy object
        '''

        # to get the enemy HP
        enemy_HP = self.enemies[turt][1]

        # if enemy has below zero HP, it disappear from the screen
        if enemy_HP <= 0:
            turt.hideturtle()
            turt.goto(500, 500)
            Adventure.enemy_num -= 1
            self.curr_enemy = ''

        # to display it on the screen
        enemy_HP = str(self.curr_enemy) + 'HP: ' + str(enemy_HP)

        # to record the enemy HP
        self.recordEvents(self.enemy_rec, enemy_HP)

    def checkBag(self):
        ''' to check the items in the bag every now and then'''

        # if there is something in the bag, show it on the screen
        if len(self.bag) > 0:
            thing = turtle.Turtle(shape= str(self.bag[-1] + '.gif'))
            thing.penup()
            thing.goto(-340 + (len(self.bag)-1) *100, 300)

    def loseBlood(self, attacker, victim):
        ''' the player might lose blood if gets too close the enemy
        or the enemy might lose blood if the player attacks the enemy
        
        parameter:
        ------------
        attacker: str. the name of the attacker (either bullet or enemy name)
        victim: str./turtle object. the name of the victim. either the player or the enemy
        '''

        # if the victim is the player
        # then based on the identity of the enemy, 
        # some HP will be deducted from player_HP
        if victim == self.player:
            # tiger is the most powerful enemy
            if attacker == 'tiger':
                Adventure.player_HP -= 4

            # followed by bear
            elif attacker == 'bear':
                Adventure.player_HP -= 3

            # then mouse
            elif attacker == 'mouse':
                Adventure.player_HP -= 2
            
            # spider and frog are the least 
            else:
                Adventure.player_HP -= 1

        # else if the player attacks the enemy
        elif victim == self.curr_enemy:
            for enemy_info in self.enemies.values():

                # then based on the weapon, the enemy will lose some HP
                if self.curr_enemy == enemy_info[0]:

                    # flame is the best 
                    if attacker == 'flame':
                        enemy_info[1] -= 3

                    # then the gun
                    elif attacker == 'gun':
                        enemy_info[1] -= 2
                    
                    # finally, the snow power
                    elif attacker == 'snowflake':
                        enemy_info[1] -= 1

    def attack(self):
        ''' to attack the enemy with the weapon/abilities the player now has
        '''
        # load in some bullets
        bullet = self.makeBullets()

        # to record who is your enemy now
        # attack it with the weapon you now have
        for enemy, identity in self.enemies.items():
            if self.curr_enemy == identity[0]:

                # to check the enemy position
                enemy_x = enemy.xcor()
                enemy_y = enemy.ycor()

                # to shoot the bullet to hit the enemy
                while abs(bullet.xcor() - enemy_x) > 2 and abs(bullet.ycor() - enemy_y) > 2:
                    self.chase(bullet, enemy)

                # every time the bullet hits the enemy, the enemy will lose some HP
                self.loseBlood(self.weapon, self.curr_enemy)

                # update enemy HP on the screen
                self.checkEnemyHP(enemy)
                
                # after the bullet hits, it disappear
                bullet.hideturtle()

    def collectItem(self):
        ''' to check for the distance between the player and the item and collect items'''
        # to collect the items encounter if the distance between the player and the item is close
        # to check through the item dictionary
        for item, name in self.items.items():

            item_x = item.xcor()
            item_y = item.ycor()

            # if they are sufficently close, add the item to the player's bag
            if abs(self.player_x - item_x) < self.radar/2 and abs(self.player_y - item_y) < self.radar/2:
                event = 'Hey! You just got a ' + name
                self.recordEvents(self.narrator, event)

                # add the item to teh bag
                self.bag.append(name)
                self.checkBag()

                # the item will disappear from it was collected
                item.hideturtle()

    def collectWeapon(self):
        ''' to check for the distance between the player and the item and collect items'''
        # to collect the items encounter if the distance between the player and the weapon is close
        # to check through the weapon dictionary
        for weapon, name in self.weapons.items():
            # to record the weapon position
            weapon_x = weapon.xcor()
            weapon_y = weapon.ycor()

            # if they are sufficently close, change the player's current weapon to the weapon
            if abs(self.player_x - weapon_x) < self.radar/2 and abs(self.player_y - weapon_y) < self.radar/2:
                event = 'Hey! You just got a ' + name + '\nyou can use this to attack the enemy!'
                self.recordEvents(self.narrator, event)
                self.weapon = name

    def makeAMap(self):
        '''to make a map so that the player can get to the maze'''

        # make a map object
        map = turtle.Turtle()

        # change the shape
        self.screen.register_shape('map.gif')
        map.shape('map.gif')

        # randomly place it on the map
        self.placeItems(map)

        # hide it until the player has killed 3 enemies
        map.hideturtle()

        # return the map
        return map

    def endGame(self):
        ''' to end the game'''
        # clean the screen
        self.screen.clear()

        # change the background pic
        self.screen.bgpic('GameOver.gif')

        # tell the use the game is over
        self.screen.textinput('Congratulations!!!', 'Yay!!!! You did it! \nYou saved your friend!!! \nThanks for playing! \nsee you next time ;)')

        # close the screen
        self.screen.bye()

    def loseGame(self):
        ''' when the player loses all the hp, end the game'''

        # clean the screen
        self.screen.clear()

        # change the background pic
        self.screen.bgpic('GameOver.gif')

        # tell the use the game is over
        self.screen.textinput('Game Over', ':((( \nYou and your friend will be lost in this cave forever...')

        # close the screen
        self.screen.bye()

    def useItem(self):
        ''' to use the item in the bag'''
        # if there are things in the bag, then the user can use the last thing collected
        if len(self.bag)>0:
            item = self.bag.pop()

            # if it is an apple, the HP will increase by 2
            if item == 'apple':
                Adventure.player_HP += 2
            
            # if it is milk, the HP will increase by 3
            elif item == 'milk':
                Adventure.player_HP += 4
            
            # if it is money, the HP will increase by 1
            elif item == 'money':
                Adventure.player_HP += 1
            
            # if it is a map, the player and the friend will find the exit
            elif item == 'map':
                self.exit.showturtle()

        # to tell the user what happened
        self.recordEvents(self.narrator, 'You don\'t have anything in your bag!!')

    def makeExit(self):
        ''' to make an exit of the maze
        
        return:
        --------
        a turt object
        '''
        # to make an exit turtle
        exit = turtle.Turtle()

        # change its shape
        self.screen.register_shape('flag.gif')
        exit.shape('flag.gif')

        # place the exit randomly on the screen
        exit.penup()
        exit.goto(350, random.choice([-350, 350]))

        # hide it until the user find the flag
        exit.hideturtle()

        # return the turtle object
        return exit

    def checkRemainingEnemy (self):
        ''' to check how many enemies are left'''

        # if there are only two enemies left on the screen, the map will show up
        if Adventure.enemy_num == 2:
            self.map.showturtle()

        # if the user has killed all the enemies, the friend will show up
        if Adventure.enemy_num == 0:
            self.friend.showturtle()
        
        # to keep chekcing 
        self.screen.ontimer(self.checkRemainingEnemy, 1000)

    def grabFriend(self):
        self.chase(self.friend, self.player)

    def setupEvents(self):
        ''' to set up the events when the user presses the key'''
        # use the keys to control the player
        self.screen.onkeypress(self.moveUp, 'w')
        self.screen.onkeypress(self.moveDown, 's')
        self.screen.onkeypress(self.moveRight, 'd')
        self.screen.onkeypress(self.moveLeft, 'a')

        # to attack enemy
        self.screen.onkeypress(self.attack, 'space')

        # to collect items, weapons
        self.screen.onkeypress(self.collectItem, 'o')
        self.screen.onkeypress(self.collectWeapon, 'p')

        # press i to use the item in bag
        self.screen.onkeypress(self.useItem, 'i')

        # press g to save your friend from the cave
        self.screen.onkeypress(self.grabFriend, 'g')

        # check the position of the player every 50 msec
        self.screen.ontimer(self.checkPosition, 100)

        # to check player's HP every 50 msec
        self.screen.ontimer(self.checkHP, 100)

        # to check if the player has collided with any enemy
        self.screen.ontimer(self.checkForCollisions, 50)

        # check the remaining enemies on the screen
        self.screen.ontimer(self.checkRemainingEnemy, 1000)

        # check if the player has saved the friend
        self.screen.ontimer(self.checkExit, 200)

        # the screen will close if the user press 'q'
        self.screen.onkeypress(turtle.bye, 'q')

def main():
    ''' to play the game'''
    # to give some description of the game and ask the user to input which avatar to use
    avatar = int(turtle.numinput('Welcome to Adventure!', 'Your friend was lost in this terrible cave.\nYou have to save your friend and find the way out!!! \nYou can collect item by pressing \'o\' \ncollect weapon by pressing \'p\' \nuse your current weapon by pressing \'space\' \nmove your character using \'w (up) s (down) a (left) d (right)\' \nNow, choose the avatar you want to control (by entering 0-3):'))
    
    # make a game object with the user input
    game = Adventure(avatar= avatar)

    # play the game
    game.play()

if __name__ == '__main__':
    main()

    


