import time
import random
import pygame
import sys
import os
pygame.mixer.init()
pygame.mixer.music.load(os.path.join("audio" , "music.ogg"))
pygame.mixer.music.play(loops=-1)
region = 1
rtextdisplayed = False
alwaysCommands = ["reset", "inventory", "goals", "combat", "mute", "unmute"]
inventory = []
fight = []
fightCorrect = []
combat1done = False
battling = 0
currentEnemy = ""
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
def askforbackstory():
    print("DO YOU WANT BACKSTORY? y/n")
    bsyn = input()
    if bsyn == "y":
        backstory()
        countdown()
        region = 1
    if bsyn == "n":
        countdown()
        region = 1
askforbackstory()
def died():
    print("You died...")
    time.sleep(1)
    print("Would you like to play again? y/n")
    playagain = input()
    if playagain.lower() == "y" or playagain.lower() == "yes":
        askforbackstory
    else:
        print("Thanks for playing!")
        time.sleep(1)
        exit()
        
#                   1                                                                                                                                2                                                                                                                   3                                                                                                              4                                                                                                            5                                                                         6                                                                                                                                                                                                                     7       8   9   10  11
regionalText = ["", "You are standing in your house. On your left is the door outside. In front of you is a television. Behind you is the kitchen.", "You are in a dark alleyway. There is a path, stretching right and left. You can also see the door to your house.", "You are in your kitchen. Behind you is the living room. There are a few knives on a rack above the counter.", "You are at a crossroads. There is an e-post on one corner. Opposite, on another corner, there is a clock.", "You reach a dead end. There is a man, asleep, on his balcony. <enter>", "You are outside the main doors of the Tokyo police station. You see a vent around the side of the building, but, then again, you could try walking through the front doors... (Enter your decision, vents or doors)", "You are outside one of many hospitals in Tokyo. The main doors are in front of you.", "", "", "", "The man's house is oddly quiet, even though it's the middle of the night. You can see a door that probably leads to the bedroom, a kitchen and another door that probably leads to a bathroom.","You don't need to wait long. Soon enough, a team of officers rush into the building, and whisk you off to a empty holding cell."]
def combat(difficulty):
    pygame.mixer.stop()
    pygame.mixer.music.load(os.path.join('audio', "battle.ogg"))
    pygame.mixer.music.play(loops=-1)
    battling = 1
    fight = []
    difficultymo = difficulty - 1
    fightChecker = ""
    for i in range(1, difficultymo):
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
    for i in range(1, difficultymo):
        print(fight[i - 1])
        fightchecker = input()
        time.sleep(0.5)
        if fightchecker == fight[i-1]:
            fightCorrect.extend("y")
            print(len(fightCorrect))
            print(difficultymo)
            if len(fightCorrect) > difficultymo:
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
            died()
            break

    
def commlist():
    print("Valid commands are:")
    print(WALK,LOOK,TAKE,CBAT,INVT,HALP[0],LEAV[0], "mute", "unmute")
    return 0

WALK = ["walk","go","move"]
LOOK = ["look","see","watch"]
TAKE = ["use","take","grab","pick up"]
CBAT = ["combat","fight","attack"]
INVT = ["inventory","me","self"]
HALP = ["help","?","huh","what","command","commands"]
LEAV = ["quit","die","exit"]

NRTH = ["north","forward"]
SUTH = ["south","back"]
EAST = ["east","right"]
WEST = ["west","left"]
UPUP = ["up","climb","jump"]
DOWN = ["down","crouch","duck"]
while True:
    if rtextdisplayed == False:
        print(regionalText[region])
        rtextdisplayed = True
    command = input()

    if command.lower() in HALP:
        commlist()
        
    if command.lower() in INVT:
        i = 0
        print(inventory)
    if command.lower() in CBAT:
        combat(5)
        print(fight)
    if command.lower() == "mute":
        pygame.mixer.music.set_volume(0.0)
    if command.lower() == "unmute":
        pygame.mixer.music.set_volume(1.0)
        '''while i <= len(inventory):
            print(inventory[i])
            i = i + 1'''
    if command.lower() in LEAV:
        yesquit = input("Are you sure you want to quit? y/n")
        if yesquit.lower()[0] == "y":
            exit()
        else:
            pass
        
    #print("region is:" + str(region))
    #print("command.lower() is:" + command.lower())
    #print("rtextdisplayed is:" + str(rtextdisplayed))
    #print("Checking region 1 loop")
    if region == 1 and rtextdisplayed:
        #print("Got inside region 1 loop")
        # what is the command?
        if command.lower().split(' ',1)[0] in WALK:
            # print("reg1 we are walking.")
            # but which way?
            if "outside" in command.lower() or "door" in command.lower() or command.lower().split(' ',1)[-1] in NRTH:
                print("Going north...")
                time.sleep(0.5)
                region = 2
                rtextdisplayed = False
            elif "kitchen" in command.lower() or command.lower().split(' ',1)[-1] in WEST:
                print("Going west...")
                time.sleep(0.5)
                region = 3
                rtextdisplayed = False
            else:
                print("You can't go that way")

        if command.lower().split(' ',1)[0] in TAKE:
            # ok, we are using something.
            # what are we using?
            if command.lower().split(' ',1)[-1] in ["television","tv"]:
                print("You turn on the television. There is a announcer, delivering the news.")
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

            
    #print("Checking region 2 loop")
    if region == 2 and rtextdisplayed:
        #print("Got inside region 2 loop")
        if command.lower().split(' ',1)[0] in WALK:
            #ok, we are walking. which way?
            if command.lower().split(' ',1)[-1] in SUTH or "door" in command.lower():
                print("Going south...")
                time.sleep(0.5)
                region = 1
                rtextdisplayed = False
            elif command.lower().split(' ',1)[-1] in WEST:
                print("Going west...")
                time.sleep(0.5)
                region = 4
                rtextdisplayed = False
            elif command.lower().split(' ',1)[-1] in EAST:
                print("Going east...")
                time.sleep(0.5)
                region = 5
                rtextdisplayed = False
            elif command.lower() in alwaysCommands:
                fdauhfkdsjhfksjhdf = 1
            else:
                pass
            
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
        if command.lower().split(' ',1)[0] in TAKE:
            if "knife" in command.lower() and "Knife" not in inventory:
                print("You pick up the sharpest seeming knife.")
                time.sleep(0.5)
                inventory.append("Knife")
            elif "Knife" in inventory:
                print("You already took a knife.")
            else:
                print("You can't pick that up.")

        elif command.lower().split(' ',1)[0] in WALK:
            if "living room" in command.lower() or command.lower().split(' ',1)[-1] in EAST:
                print("Going east...")
                time.sleep(0.5)
                region = 1
                rtextdisplayed = False
            else:
                print("You walk into a wall.")
        elif command.lower() in alwaysCommands:
                sfhdkjfhkjhdf = 1

    #print("Checking region 4 loop")
    if region == 4 and rtextdisplayed:
        #print("Got inside region 4 loop")
        if command.lower().split(' ',1)[0] in LOOK:
            # ok we are looking.
            # what are we looking at?
            if "post" in command.lower():
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
            elif "clock" in command.lower():
                print("The time is 1:37am.")
                time.sleep(0.5)

        if command.lower().split(' ',1)[0] in WALK:
            #where do we walk to
            if command.lower().split(' ',1)[-1] in NRTH:
                print("You have to be more specific than that.")
                print("Do you want to go to the library or to the university?")
                break
            
            if "kokugakuin" in command.lower() or "university" in command.lower():
                print("Going north...")
                region = 9
                time.sleep(0.5)
                rtextdisplayed = False
            elif "shibuya" in command.lower() or "library" in command.lower():
                    print("Going north...")
                    region = 10
                    time.sleep(0.5)
                    rtextdisplayed = False
            else:
                print("You can't go there!")

            if command.lower().split(' ',1)[-1] in EAST:
                print("Going east...")
                time.sleep(0.5)
                region = 2
                rtextdisplayed = False

            if command.lower().split(' ',1)[-1] in WEST:
                print("You have to be more specific than that.")
                print("Do you want to go to the police station, hospital, or high school?")
                

            if "police" in command.lower() or "station" in command.lower():
                print("Going west...")
                time.sleep(0.5)
                region = 6
                rtextdisplayed = False
            elif "hospital" in command.lower():
                print("Going west...")
                time.sleep(0.5)
                region = 7
                rtextdisplayed = False
            elif "daigaku" in command.lower() or "school" in command.lower():
                print("Going west...")
                time.sleep(0.5)
                region = 8
                rtextdisplayed = False
            else:
                print("You can't go there!")
        elif command.lower() in alwaysCommands:
                slfdijdifjsdlkfj = 1

    if region == 5 and rtextdisplayed:
        if "Knife" in inventory and not combat1done:
            print("You sneak up to the balcony. Just as you jimmy the lock, the man wakes up, and attacks you!")
            currentEnemy = "MAN ON BALCONY"
            combat(3)
            combat1done = True
            print("You slowly creep into the man's apartment.")
            time.sleep(1)
            region = 11
            rtextdisplayed = False
        else:
            print("Quickly, you run back to your apartment door.")
            print("Going west...")
            time.sleep(0.5)
            region = 2
            rtextdisplayed = False
    if region == 6 and rtextdisplayed:
        if command.lower() == "doors":
            decision1 = "doors"
            print("You chose to go in through the doors.")
            time.sleep(3)
            print("You try the handle. Unlocked!")
            time.sleep(2)
            print("As you step inside, a net falls onto you and an alarm goes off.")
            region = 13
            rtextdisplayed = False
        if command.lower() == "vents":
            decision1 = "vents"
            print("You chose to go in through the vent system.")
            region = 14
            rtextdisplayed = False
    if region == 7 and rtextdisplayed:
        if command.lower
        













































