import time
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
print("DO YOU WANT BACKSTORY? y/n")
bsyn = input()
if bsyn == "y":
    backstory()
print("YOUR MISSION BEGINS...")
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
region = 1
rtextdisplayed = False
alwaysCommands = ["reset", "inventory", "goals"]
inventory = []
#                   1                                                                                                                                2                                                                                                                  3                                                                                                                                    4
regionalText = ["", "You are standing in your house. On your left is the door outside. In front of you is a television. Behind you is the kitchen.", "You are in a dark alleyway. There is a path, stretching right and left. You can also see the door to your house.", "You are in your kitchen. Behind you is the living room. There are a few knives on a rack above the counter.", "You are at a crossroads. There is an e-post on one corner. Opposite, on another corner, there is a clock."]
while True:
    if rtextdisplayed == False:
        print(regionalText[region])
        rtextdisplayed = True
    command = input()
    #print("region is:" + str(region))
    #print("command is:" + command)
    #print("rtextdisplayed is:" + str(rtextdisplayed))
    #print("Checking region 1 loop")
    if region == 1 and rtextdisplayed == True:
        #print("Got inside region 1 loop")
        if command == "walk to door":
            print("Going north...")
            time.sleep(0.5)
            region = 2
            rtextdisplayed = False
        elif command == "walk to kitchen":
            print("Going west...")
            time.sleep(0.5)
            region = 3
            rtextdisplayed = False
        elif command == "use television":
            print("You turn on the televsion. There is a announcer, delivering the news.")
            time.sleep(3)
            print("Always be on the lookout for the Mutants.")
            print("The Mutants, eh? Is that what they're calling us?")
            time.sleep(3)
            print("Already 6 of the nasty creatures are locked up in the main police station in Tokyo.")
            print("Aha! So that's where I should start.")
            time.sleep(3)
            print("The news stops, to be replaced by a cartoon about a boy trying to become a 'Pokeyman Mister?' Or something like that.")
        else:
            print("I didn't recognise that command!")
    #print("Checking region 2 loop")
    if region == 2 and rtextdisplayed == True:
        #print("Got inside region 2 loop")
        if command == "walk to door":
            print("Going south...")
            time.sleep(0.5)
            region = 1
            rtextdisplayed = False
        elif command == "walk left":
            print("Going west...")
            time.sleep(0.5)
            region = 4
            rtextdisplayed = False
        elif command == "walk right":
            print("Going east...")
            time.sleep(0.5)
            region = 5
            rtextdisplayed = False
        else:
            print("I didn't recognise that command!")
    #print("Checking region 3 loop")
    #print("region is:" + str(region))
    #print("command is:" + command)
    #print("rtextdisplayed is:" + str(rtextdisplayed))
    if region == 3 and rtextdisplayed == True:
        #print("Got inside region 3 loop")
        if command == "pick up knife":
            print("You pick up the sharpest seeming knife.")
            time.sleep(0.5)
            inventory.extend("Knife")
        elif command == "walk to living room":
            print("Going east...")
            time.sleep(0.5)
            region = 1
            rtextdisplayed = False
        else:
            print("I didn't recognise that command!")
    #print("Checking region 4 loop")
    if region == 4 and rtextdisplayed == True:
        #print("Got inside region 4 loop")
        if command == "look at e-post":
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
        elif command == "look at clock":
            print("The time is 1:37am.")
            time.sleep(0.5)
        elif command == "walk north":
            print("Going north...")
            time.sleep(0.5)
            region = 6
            rtextdisplayed = False
        elif command == "walk west":
            print("Going west...")
            time.sleep(0.5)
            region = 7
            rtextdisplayed = False
        elif command == "walk east":
            print("Going east...")
            time.sleep(0.5)
            region = 2
            rtextdisplayed = False
        else:
            print("I didn't recognise that command!")
        if region == 5 and rtextdisplayed == True:
            if command == "look at e-post":
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
            elif command == "look at clock":
                print("The time is 1:37am.")
                time.sleep(0.5)
            elif command == "walk north":
                print("Going north...")
                time.sleep(0.5)
                region = 6
                rtextdisplayed = False
            elif command == "walk west":
                print("Going west...")
                time.sleep(0.5)
                region = 7
                rtextdisplayed = False
            elif command == "walk east":
                print("Going east...")
                time.sleep(0.5)
                region = 2
                rtextdisplayed = False
            else:
                print("I didn't recognise that command!")













































