'''
The Cup Game
Sticky Keys
October 2022
Version: 1.0.0
'''

#import randon to generate a randon nubmer
import random

print("What Cup Do You Think The Ball Is Under?")
print("1, 2, or 3?")

choice = int(input("Choice: "))

#generate a random number from 1 to 3 
randomCup = random.randint(1,3)

if choice == randomCup:
    print("You Got It!")
else:
    print("Sorry Try Again!")