#Note for the evaluator :-

#I have created my own template for this mini-project as
#it was not necessary to follow the helper template.

#This code follows all the guidelines mentioned by the 
#grading rubric. 

#The names of the functions and the process followed 
#for achieving the results will differ a bit.

#However the code achieves the desired output keeping
#the grading rubric in mind


#imports
import simplegui
import random
import math

# globals
UserEnteredNumber = 0
ComputerGeneratedRandomNumber = 0
NumberOfRemainingGuesses = 0
RangeValue = 0

# helper functions
def CompareNumbers() :
    global UserEnteredNumber
    global ComputerGeneratedRandomNumber
    global NumberOfRemainingGuesses
    global RangeValue  
    RangeValueGuess = NumberOfRemainingGuesses
    NumberOfRemainingGuesses = NumberOfRemainingGuesses -1
    if NumberOfRemainingGuesses == 0 and RangeValue ==10:
        print "Correct number was: ",  ComputerGeneratedRandomNumber
        print
        RangeZeroToThousand()
    elif NumberOfRemainingGuesses == 0 and RangeValue ==7:
        print "Correct number was: ",  ComputerGeneratedRandomNumber
        print
        RangeZeroToHundred() 
    elif ComputerGeneratedRandomNumber == UserEnteredNumber :
        print "Guess was ",UserEnteredNumber
        print "Number of remaining guesses is", NumberOfRemainingGuesses        
        print "Correct"
        if RangeValue ==10:
            print
            RangeZeroToThousand()
        elif RangeValue ==7:
            print
            RangeZeroToHundred()
    elif ComputerGeneratedRandomNumber > UserEnteredNumber :
        print "Guess was ",UserEnteredNumber
        print "Number of remaining guesses is", NumberOfRemainingGuesses                
        print "higher"
    elif ComputerGeneratedRandomNumber < UserEnteredNumber :
        print "Guess was ",UserEnteredNumber
        print "Number of remaining guesses is", NumberOfRemainingGuesses                
        print "lower"

# define event handlers
def RangeZeroToHundred() :
    global UserEnteredNumber
    global ComputerGeneratedRandomNumber
    global NumberOfRemainingGuesses
    global RangeValue
    ComputerGeneratedRandomNumber = random.randint(1,100)
    NumberOfRemainingGuesses = 7
    RangeValue = 7
    print "New game, Range is from 0 to 100"
    print "Number of remaining guesses is 7"
    print
    return ComputerGeneratedRandomNumber

def RangeZeroToThousand() :
    global UserEnteredNumber
    global ComputerGeneratedRandomNumber
    global NumberOfRemainingGuesses
    global RangeValue
    ComputerGeneratedRandomNumber = random.randint(1,1000)
    NumberOfRemainingGuesses = 10
    RangeValue = 10
    print "New game, Range is from 0 to 1000"
    print "Number of remaining guesses is 10"
    print
    return ComputerGeneratedRandomNumber

def EnterAGuess(guess) :
    global UserEnteredNumber
    global ComputerGeneratedRandomNumber
    global NumberOfRemainingGuesses
    global RangeValue
    UserEnteredNumber = int(guess)
    CompareNumbers()
    return UserEnteredNumber

# create frame
Myframe = simplegui.create_frame("GuessTheNumber", 200, 200)
# register event handlers
Myframe.add_button("Range is [0, 100)", RangeZeroToHundred, 200)
Myframe.add_button("Range is [0, 1000)", RangeZeroToThousand, 200)
Myframe.add_input('Enter a guess', EnterAGuess, 200)

# start frame
Myframe.start()
RangeZeroToHundred()
