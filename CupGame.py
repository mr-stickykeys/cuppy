'''
The Cup Game
Sticky Keys
October 2022
Version: 1.1.0
'''

#import randon to generate a randon nubmer
import random

print("What Cup Do You Think The Ball Is Under?")
print("1, 2, or 3?")

score = 0

while True:
    
    #generate a random number from 1 to 3 
    randomCup = random.randint(1,3)
    
    choice = int(input("Choice: "))

    if choice == randomCup:
        print("You Got It!")
        score+=1
    else:
        print("Sorry Try Again!")
        break
    
print("Your Final Score Is: "+str(score))