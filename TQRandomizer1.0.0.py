import random as rnd   
import sys

print ("***************************************")
print ("****Ultimate Titan Quest Randomizer****")
print ("***************************************")


while True: 
    TQAll = ("Nature","Warfare","Defense","Hunting","Earth","Storm","Rogue","Spirit","Dream","Rune")
    TQInt = ("Nature","Earth","Storm","Spirit","Dream","Rune")
    TQMelee = ("Warfare","Defense","Hunting","Rogue","Rune")
    TQChallenge = ("Hardcore","No Attributes","MI/Green Gear Only","Yellow Gear Only","No Backpack/Dropped Loot Only")

    print ("Please choose an action to take: ")
    print ("1 -- Randomize a Build")
    print ("2 -- Randomize a Magic based build")
    print ("3 -- Randomize a Melee type build")
    print ("4 -- Randomize a Build and a Challenge")
    print ("Q == Quit the application")
    print ("***************************************")
    userChoice = str(input())

    #Randomize a build with all masteries
    if userChoice == "1":
        print ("")
        print ("")
        print (f">>>> Your build will be {rnd.choice(TQAll)} and {rnd.choice(TQAll)} <<<<")
        print ("")
        print ("")
    
    #Randomize out of INT based masteries
    elif userChoice == "2":
        print ("")
        print ("")
        print (f">>>> Your build will be {rnd.choice(TQInt)} and {rnd.choice(TQInt)} <<<<")
        print ("")
        print ("")

    #Randomize out of STR based masteries
    elif userChoice == "3":
        print ("")
        print ("")
        print (f">>>> Your build will be {rnd.choice(TQMelee)} and {rnd.choice(TQMelee)} <<<<")
        print ("")
        print ("")
    
    #Randomize a build with a challenge to do
    elif userChoice == "4":
        print ("")
        print ("")
        print (f">>>> Your build will be {rnd.choice(TQAll)} and {rnd.choice(TQAll)} with the Challenge: {rnd.choice(TQChallenge)} <<<<")
        print ("")
        print ("")

    #Quit the App
    elif userChoice == "Q":
        print ("Thanks for using the Titan Quest Randomizer App")
        print ("NekoCode ©2019")
        sys.exit()
    #Exception for unknown input
    else: 
        print ("")
        print ("")
        print ("That is not a valid input. Please Try Again.")
        print ("")
        print ("")
