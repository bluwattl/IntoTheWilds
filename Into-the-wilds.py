import time
import random
import pygame
import sys
import os
pygame.init()
pygame.mixer.init()
pygame.mixer.music.load(os.path.join("audio" , "music.ogg"))
pygame.mixer.music.play(loops=-1)
print("INTO THE WILDS: A TEXT ADVENTURE")
def backstory():
    print("YOU LIVE IN 36TH CENTURY TOKYO, WHERE THE WORLD IS IN PANIC.")
    time.sleep(3)
    print("THERE ARE HUMAN-PANDA HYBRIDS, WHO THE NORMAL HUMANS HATE.")
    time.sleep(3)
    print("AS THE CITY BEGAN TO DISLIKE THESE CREATURES, THE OLDER ONES RETREATED TO THE BAMBOO FORESTS.")
    time.sleep(3)
    print("YOU ARE ONE OF THESE HYBRIDS. HOWEVER, YOU DID NOT LEAVE THE CITY.")
    time.sleep(3)
    print("YOU NEED TO TAKE ALL OF THE REMAINING HYBRIDS TO THE GROVES.")
    time.sleep(3)
def countdown():
    print("YOUR MISSION BEGINS...")
    time.sleep(1)
    print("5")
    time.sleep(1)
    print("4")
    time.sleep(1)
    print("3")
    time.sleep(1)
    print("2")
    time.sleep(1)
    print("1")
    time.sleep(1)
print("DO YOU WANT BACKSTORY? y/n")
bsyn = input()
if bsyn == "y":
    backstory()
    countdown()
if bsyn == "n":
    countdown()
region = 1
rtextdisplayed = False
alwaysCommands = ["reset", "inventory", "goals", "combat", "mute", "unmute"]
inventory = []
fight = []
fightCorrect = []
combat1done = False
battling = 0
currentEnemy = ""
#                   1                                                                                                                                2                                                                                                                   3                                                                                                              4                                                                                                            5                                                                         6
regionalText = ["", "You are standing in your house. On your left is the door outside. In front of you is a television. Behind you is the kitchen.", "You are in a dark alleyway. There is a path, stretching right and left. You can also see the door to your house.", "You are in your kitchen. Behind you is the living room. There are a few knives on a rack above the counter.", "You are at a crossroads. There is an e-post on one corner. Opposite, on another corner, there is a clock.", "You reach a dead end. There is a man, asleep, on his balcony. <return>", "", "", "", "", "", ""]
def combat(difficulty):
    pygame.mixer.stop()
    pygame.mixer.music.load(os.path.join('audio', "battle.ogg"))
    pygame.mixer.music.play()
    battling = 1
    fight = []
    difficulty += 1
    fightChecker = ""
    for i in range(1, difficulty):
        fightadd = random.randint(1,4)
        if fightadd == 1:
            fightadd = "W"
        elif fightadd == 2:
            fightadd = "A"
        elif fightadd == 3:
            fightadd = "S"
        else:
            fightadd = "D"
        fight.append(fightadd)
        i += 1
    for i in range(1, difficulty):
        print(fight[i - 1])
        fightchecker = input()
        time.sleep(0.5)
        if fightchecker == fight[i-1]:
            fightCorrect.extend("y")
            if len(fightCorrect) > 4:
                print("You vanquished "+ currentEnemy +"!")
                pygame.mixer.fadeout(1)
                time.sleep(1)
                pygame.mixer.music.load(os.path.join("audio" , "music.ogg"))
                pygame.mixer.music.play(loops=-1)
                break
        else:
            print("Wrong")
            pygame.mixer.fadeout(1)
            time.sleep(1)
            battling = 0
            pygame.mixer.music.load(os.path.join("audio" , "music.ogg"))
            pygame.mixer.music.play(loops=-1)
            break
    
            
while True:
    if rtextdisplayed == False:
        print(regionalText[region])
        rtextdisplayed = True
    command = input()
    if command.lower() == "inventory":
        i = 0
        print(inventory)
    if command.lower() == "combat":
        combat(5)
        print(fight)
    if command.lower() == "mute":
        pygame.mixer.music.set_volume(0.0)
    if command.lower() == "unmute":
        pygame.mixer.music.set_volume(1.0)
        '''while i <= len(inventory):
            print(inventory[i])
            i = i + 1'''
    #print("region is:" + str(region))
    #print("command.lower() is:" + command.lower())
    #print("rtextdisplayed is:" + str(rtextdisplayed))
    #print("Checking region 1 loop")
    if region == 1 and rtextdisplayed:
        #print("Got inside region 1 loop")
        if command.lower() == "walk to door":
            print("Going north...")
            time.sleep(0.5)
            region = 2
            rtextdisplayed = False
        elif command.lower() == "walk to kitchen":
            print("Going west...")
            time.sleep(0.5)
            region = 3
            rtextdisplayed = False
        elif command.lower() == "use television":
            print("You turn on the televsion. There is a announcer, delivering the news.")
            time.sleep(3)
            print("Always be on the lookout for the Mutants.")
            print("The Mutants, eh? Is that what they're calling us?")
            time.sleep(3)
            print("Already 6 of the nasty creatures are locked up in the main police station in Tokyo.")
            print("Aha! So that's where I should start.")
            time.sleep(3)
            print("The news stops, to be replaced by a cartoon about a boy trying to become a 'Pokeyman Mister?' Or something like that.")
        elif command.lower() in alwaysCommands:
                ksdfhudshf = 1
        else:
            print("I didn't recognise that command!")
    #print("Checking region 2 loop")
    if region == 2 and rtextdisplayed:
        #print("Got inside region 2 loop")
        if command.lower() == "walk to door":
            print("Going south...")
            time.sleep(0.5)
            region = 1
            rtextdisplayed = False
        elif command.lower() == "walk left":
            print("Going west...")
            time.sleep(0.5)
            region = 4
            rtextdisplayed = False
        elif command.lower() == "walk right":
            print("Going east...")
            time.sleep(0.5)
            region = 5
            rtextdisplayed = False
        elif command.lower() in alwaysCommands:
            fdauhfkdsjhfksjhdf = 1
        else:
            print("I didn't recognise that command!")
    #print("Checking region 3 loop")
    #print("region is:" + str(region))
    #print("command.lower() is:" + command)
    #print("rtextdisplayed is:" + str(rtextdisplayed))
    if region == 3 and rtextdisplayed:
        #print("Got inside region 3 loop")
        if command.lower() == "pick up knife":
            print("You pick up the sharpest seeming knife.")
            time.sleep(0.5)
            inventory.insert(0, "Knife")
        elif command.lower() == "walk to living room":
            print("Going east...")
            time.sleep(0.5)
            region = 1
            rtextdisplayed = False
        elif command.lower() in alwaysCommands:
                sfhdkjfhkjhdf = 1
        else:
            print("I didn't recognise that command!")
    #print("Checking region 4 loop")
    if region == 4 and rtextdisplayed:
        #print("Got inside region 4 loop")
        if command.lower() == "look at e-post":
                print("It says:")
                time.sleep(2.5)
                print("E-POST: CNR HIGASHI & SHIBUYA")
                time.sleep(0.5)
                print("WEST: POLICE STATION, HOSPITAL, DAIGAKU HIGH SCHOOL.")
                time.sleep(0.5)
                print("NORTH: SHIBUYA LIBRARY, KOKUGAKUIN UNIVERSITY.")
                time.sleep(0.5)
                print("EAST: APARTMENTS.")
                time.sleep(0.5)
        elif command.lower() == "look at clock":
                print("The time is 1:37am.")
                time.sleep(0.5)
        elif command.lower() == "walk north":
                print("Where do you want to go?")
                wherenorth = input()
                if wherenorth.lower() == "kokugakuin university" or wherenorth.lower() == "university":
                    print("Going north...")
                    region = 9
                    time.sleep(0.5)
                    rtextdisplayed = False
                elif wherenorth.lower() == "shibuya library" or wherenorth.lower() == "library":
                    print("Going north...")
                    region = 10
                    time.sleep(0.5)
                    rtextdisplayed = False
                else:
                    print("You can't go there!")
        elif command.lower() == "walk east":
                print("Going east...")
                time.sleep(0.5)
                region = 2
                rtextdisplayed = False
        elif command.lower() == "walk west":
            print("Where do you want to go?")
            wherewest = input()
            if wherewest.lower() == "police station":
                print("Going west...")
                time.sleep(0.5)
                region = 6
                rtextdisplayed = False
            elif wherewest.lower() == "hospital":
                print("Going west...")
                time.sleep(0.5)
                region = 7
                rtextdisplayed = False
            elif wherewest.lower() == "high school" or wherewest.lower() == "daigaku high school":
                print("Going west...")
                time.sleep(0.5)
                region = 8
                rtextdisplayed = False
            else:
                print("You can't go there!")
        elif command.lower() in alwaysCommands:
                slfdijdifjsdlkfj = 1
        else:
                print("I didn't recognise that command!")
    if region == 5 and rtextdisplayed:
        if "Knife" in inventory and not combat1done:
            print("You sneak up to the balcony. Just as you jimmy the lock, the man wakes up, and attacks you!")
            currentEnemy = "MAN ON BALCONY"
            combat(3)
            combat1done = True
        else:
            print("Quickly, you run back to your apartment door.")
            print("Going west...")
            time.sleep(0.5)
            region = 2
            rtextdisplayed = False
        













































