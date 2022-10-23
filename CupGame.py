'''
The Cup Game
Sticky Keys
October 2022
Version: 1.4.0
'''

#import random to generate a randon nubmer
import random

#function that will return the intructions of the game
def showInstructions():
    instructions = "\nA Ball Is Put Under A Random Cup.\nThe Cups Are Shuffled.\nFind The Ball.\n"
    print(instructions)

#function that is used inside of launchGame() to draw cups on the screen
def drawCups(numberOfCups):
    #all the follwing print statementts print the cups to the console
    print((("-"+("-"*3)+"-")+(" "*3))*numberOfCups)
    print(("|"+((" "*3)+"|")+(" "*3))*numberOfCups)
    print((("| "+ "$" + " |")+(" "*3))*numberOfCups)
    print((("|"+(" "*3)+"|")+(" "*3))*numberOfCups)

#function that will kick of the game with a specifc number of cups
def launchGame(numberOfCups):
    print("Welcome, Lets Begin.\n")
    
    #call drawCups() to draw a specific number of cups on the console 
    drawCups(numberOfCups)
    
    #gameState keeps track of the current game state
    # 1 = not game over
    # 0 = game over
    gameState = 1
    
    #keep track of the score
    score = 0
    
    while gameState == 1:
    
        #print out the score
        print("\nScore: "+str(score))
        #generate a random cup
        randCup = random.randint(1, numberOfCups)
        print(randCup)
        print("Enter \'0\' To Quit The Game.")
        print("Shuffling The Cups...")
        choice = int(input("Choose A Cup: "))
        if choice == randCup:
            print("\nCorrect!\n")
            score+=1
        elif choice == 0:
            print("\nEnding Game...\n")
            gameState == 0
            break
        else:
            print("\nIncorrect!\n")


#main entry point for the program 
print("Welcome To The Cup Game!\n 1. Play\n 2. Instructions\n 3. Quit\n")

choice = int(input("Choice: "))

while choice != 3:

    if choice == 1:
        mode = int(input("Easy or Hard Mode?\n1 = Easy\n2 = Hard\nMode = "))
        if mode == 1:
            launchGame(3)
        elif mode == 2:
            launchGame(5)
    elif choice == 2:
        showInstructions()
    elif choice == 3:
        break
    
    choice = int(input("\nChoice: "))
    
print("Thanks For Playing. Goodbye.")