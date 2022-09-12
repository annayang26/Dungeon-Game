''' lsystem.py
Anna Yang
CS151: visual media
Lab08: classes
this lab is to practice design classes for representing and drawing L-system strings
'''

class Lsystem:
    def __init__(self, filename=None):
        '''L-system class constructor

        Parameters:
        -----------
        filename: str. Filename of the L-system text file with the base string and 1+ replacement rules
        '''
        # Create an instance variable for the base string
        self.base = ''

        # Create an instance variable for your replacement rules
        self.rules = []

        # Check if filename passed in (i.e. parameter is not None)
        # If so, read in the L-system from 'filename'
        if filename != None:
            self.read(filename)

    def __str__(self):
        ''' returns a nicely formatted string to indicate how the rule was implemented
        
        return:
        ---------
        a string
        '''
        
        return 'base: {self.base}\nrules: {self.rules}'.format(self = self)
        
    def getBase(self):
        ''' to get the base string instance variable

        return:
        --------
        the base string
        '''
        # return the base string 
        return self.base 
    
    def setBase(self, newBase):
        ''' to set a new base string

        parameter:
        -----------
        newBase: str. a new base string to replace the old one
        '''
        # to set a new base string 
        self.base = newBase

    def getRule(self, ruleIdx):
        ''' to get the rule sublist at index

        parameter:
        -----------
        ruleIdx: int. the index of the item that you want to get 

        return:
        --------
        the replace rule at the index desired
        '''

        # to get the rule sublist at index
        return self.rules[ruleIdx]

    def addRule(self, newRule):
        ''' to append a new replacement rule to the current list of replacement rules

        parameter:
        ----------
        newRule: 2 item list. a new replacement rule
        '''
        # to append the new rule
        self.rules.append(newRule)

    def numRules(self):
        '''returns the number of replacement rules currently in the L-system

        returns:
        ---------
        the number of item in the list
        '''
        # to return the length of the rule list 
        return len(self.rules)

    def read(self, filename):
        '''Reads the L-system base string and 1+ rules from a text file. Stores the data in the
        instance variables in the constructor in the format:

        base string: str.
            e.g. `'F-F-F-F'`
        replacement rules: list of 2 element sublists.
            e.g. `[['F', 'FF-F+F-F-FF']]` for one rule

        Parameters:
        -----------
        filename: str. Filename of the L-system text file with the base string and 1+ replacement
            rules
        '''
        # Open the file called filename
        fileInput = open(filename, 'r')

        # Read in the file line-by-line.
        line = fileInput.readline()
        
        while line != '':

            # to get rid of the new line character
            line = line.strip('\n')

            # to split the string into different items
            strList = line.split(' ')

            # if the first item is 'base', replace the old base string with the 2nd item
            if strList[0] == 'base':
                self.setBase(strList[1])

            # if the first item is 'rule', add that to the rule
            elif strList[0] == 'rule':
                self.addRule(strList[1:])

            line = fileInput.readline()
        
        # Close the file
        fileInput.close()

    def replace(self, currString):
        '''Applies the full set of replacement rules to current 'base' L-system string `currString`.

        Overall strategy:
        - Scan the L-system string left to right, char by char
        - Apply AT MOST ONE replacement rule to a matching character.
            Example: If the current char is 'F' and that matches a rule's find string 'F', apply
            that rule then move onto the next character in the L-system string (don't try to match
            more rules to the current char).
        - If no rule matches a rule find string, we just add the char as-is to the new string.

        Parameters:
        -----------
        currString: str. The current L-system base string.

        Returns:
        -----------
        newString: str. The base string `currString` with replacement rules applied to it.
        '''
        # to create an empty to string to hold the new string
        newString = ''

        # to scan the current string and apply the replace rule
        for char in currString: 

            # set a boolean to check if any rule applies
            found = False

            # check every rule
            for rule in self.rules:

                # if one rule applies, replace the char with the new rule and change the condition to True
                # end the for loop
                if char == rule[0]:
                    newString += rule[1]
                    found = True
                    break
            
            # if the condition is false, then add the original char to the string
            if found == False:
                newString += char

        # return the string 
        return newString
        
    def buildString(self, n):
        '''Starting with the base string, apply the L-system replacement rules for `n` iterations.

        You should NOT change your base string instance variable here!

        Parameters:
        -----------
        n: int. Number of times you go through the L-system string to apply the replacement rules.

        Returns:
        -----------
        str. The L-system string after apply the replacement rules `n` times.
        '''
        # the original string is the base string
        newStr = self.base

        # use the for loop to run n iterations
        for i in range(n):
            newStr = self.replace(newStr)
            
        # to return the L-system string
        return newStr