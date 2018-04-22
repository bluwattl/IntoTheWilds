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
invisisuit = False
seennewsstory = False
battling = 0
i = 1
currentEnemy = ""
print("INTO THE WILDS: A TEXT ADVENTURE")
def backstory():
    print("YOU LIVE IN 36TH CENTURY TOKYO, WHERE THE WORLD IS IN PANIC.")
    time.sleep(3)
    print("THERE ARE HUMAN-PANDA HYBRIDS, WHO THE NORMAL HUMANS HATE.")
    time.sleep(3)
    print("AS THE CITY BEGAN TO DISLIKE THESE CREATURES, THE OLDER ONES RETREATED TO THE BAMBOO GROVES.")
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
        askforbackstory()
        combat1done = False

    else:
        print("Thanks for playing!")
        time.sleep(1)
        exit()

#                                                                                      1                                                                                                                                2                                                                                                                   3                                                                                                              4                                                                                                                                                                                               5                                                                         6                                                                                                                                                                                                                     7                                                                                                                                                                                                       8                                                                                                                                                                               9                                                                                                                                                                10  11
regionalText = ["Technically, region 0 isn't supposed to exist. But congratulations!", "You are standing in your house. On your left is the door outside. In front of you is a television. Behind you is the kitchen.", "You are in a dark alleyway. There is a path, stretching right and left. You can also see the door to your house.", "You are in your kitchen. Behind you is the living room. There are a few knives on a rack above the counter.", "You are at a crossroads. There is an e-post on one corner. Opposite, on another corner, there is a clock. There is a small newsstand next to the e-post, with a big headline barely visible.", "You reach a dead end. There is a man, asleep, on his balcony. <enter>", "You are outside the main doors of the Tokyo police station. You see a vent around the side of the building, but, then again, you could try walking through the front doors... (Enter your decision, vents or doors)", "You are outside one of many hospitals in Tokyo. The main doors are in front of you. You sneak in. The lobby is surprisingly decorative. There is a direction sign up ahead, and behind it is a lift.", "Daigaku High School is quite a small school, considering it's in the centre of Tokyo. There are two blocks, conveniently labelled Block A and Block B. Which will you go to?", "This branch of Kokugakuin University is only a three-storey building, but you're sure you could find something here. Which floor will you check? (1, 2, or 3)", "The library is filled with ancient document about Tokyo's and Japan's history.", "The man's house is oddly quiet, even though it's the middle of the night. You can see a door that probably leads to the bedroom, a kitchen and another door that probably leads to a bathroom.","You don't need to wait long. Soon enough, a team of officers rush into the building, and whisk you off to a empty holding cell."]
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
        i = i + 1
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
            print(currentEnemy + " dealt a lethal blow!")
            pygame.mixer.fadeout(1)
            time.sleep(1)
            died()
            break


def commlist():
    print("Valid commands are:")
    print("walk to, look at, pick up, use, inventory, quit, mute, unmute.")
    return 0

WALK = ["walk","go","move"]
LOOK = ["look","see","watch"]
TAKE = ["use","take","grab","pick up"]
CBAT = ["combat","fight","attack"]
INVT = ["inventory","me","self"]
HELP = ["help","?","huh","what","command","commands"]
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

    if command.lower() in HELP:
        commlist()

    if command.lower() in INVT:
        i = 0
        if len(inventory) < 1:
            print("You aren't carrying anything!")
        else:
            print("You are carrying:")
            i=0
            while i < len(inventory):
                print(inventory[i])
                i = i + 1
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
            if "living room" in command.lower():
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
                print("The time is 1:38am.")
                time.sleep(0.5)
            elif "headline" in command.lower():
                print("You can't see it from here. Maybe if you went a bit closer?")

        if command.lower().split(' ',1)[0] in WALK:
            #where do we walk to
            if "newsstand" in command.lower() or "headline" in command.lower():
                print("You walk over to the newsstand, to get a closer look at the headline.")
                time.sleep(1)
                print("Hmm...")
                time.sleep(1.2)
                print("Maybe...")
                time.sleep(0.97)
                print("Yes!")
                time.sleep(1.5)
                print("You've made out most of it, it reads:")
                time.sleep(1)
                print("INV-B-ITY SU- DISC-ERED")
                time.sleep(0.6)
                if combat1done:
                    print("Underneath is a photo who looks strangely familiar...")
                seennewsstory = True

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
            region = 12
            rtextdisplayed = False
        if command.lower() == "vents":
            decision1 = "vents"
            print("You chose to go in through the vent system.")
            region = 13
            rtextdisplayed = False
    if region == 7 and rtextdisplayed:
        if "look" in command.lower() and "post" in command.lower():
            hospitalpostlooked = True
            print("HOSPITAL PLAN")
            time.sleep(0.3)
            print("L: LOBBY")
            time.sleep(0.3)
            print("F1: DELIVERY UNIT & ACCIDENT AND EMERGENCY")
            time.sleep(0.3)
            print("F2: INTENSIVE CARE UNIT")
            time.sleep(0.3)
            print("F3: CHILDREN'S HOSPITAL")
            time.sleep(0.3)
            print("F4: THEATERS & ORTHOPAEDICS")
            time.sleep(0.3)
            print("F5: CARDIOLOGY & RADIOLOGY")
            time.sleep(0.3)
        if "walk" in command.lower() and "lift" in commmand.lower():
            if hospitalpostlooked:
                  print("Which floor would you like to go to?")
                  if "1" in command.lower():
                      region = 14
                      rtextdisplayed = False
                  if "2" in command.lower():
                      region = 15
                      rtextdisplayed = False
                  if "3" in command.lower():
                      region = 16
                      rtextdisplayed = False
                  if "4" in command.lower():
                      region = 17
                      rtextdisplayed = False
                  if "5" in command.lower():
                      region = 18
                      rtextdisplayed = False
            else:
                  print("How do you know where you're going?")
    if region == 8 and rtextdisplayed:
        if "a" in command.lower():
            region = 19
            rtextdisplayed = False
        if "b" in command.lower():
            region = 20
            rtextdisplayed = False
    if region == 9 and rtextdisplayed:
        if "walk" in command.lower() and "crossroads" in command.lower():
            region = 4
            rtextdisplayed = False
        if "1" in command.lower():
            i = 1
            while i < 4:
                print("BRB, looking for stuff")
                time.sleep(1)
                i=i+1
            print("You found a Philips screwdriver!")
            inventory.append("Philips screwdriver")
        if "2" in command.lower():
            i = 1
            if invisisuit:
                print("You put on the INVISISUIT, sneak past the guards and start searching.")
                while i < 4:
                    print("BRB, looking for stuff")
                    time.sleep(1)
                    i=i+1
                print("You found a shotgun!")
                inventory.append("Shotgun")
            if not invisisuit:
                print("The nightly patrol is here, and you are spotted and shot.")
                time.sleep(1)
                died()
        if "3" in command.lower():
            i = 1
            while i < 4:
                print("BRB, looking for stuff")
                time.sleep(1)
                i=i+1
            print("You found an... icecream cone?!")
            inventory.append("Icecream cone")

    if region == 10 and rtextdisplayed:
        time.sleep(0.7)
        print("There sure is some interesting stuff here. Above the desk is a portrait of a dark-skinned woman, the founder.")
        time.sleep(0.8)
        print("... Better get going!")
        region = 4
        rtextdisplayed = False
