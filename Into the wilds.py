import time
print("INTO THE WILDS: A TEXT ADVENTURE")
time.sleep(3)
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
#                   1                                                                                                                                2                                                                                                                  3
regionalText = ["", "You are standing in your house. On your left is the door outside. In front of you is a television. Behind you is the kitchen.", "You are in a dark alleyway. There is a path, stretching right and left. Behind you is the door you came out of.", "You are in your kitchen. Behind you is the living room. There are a few knives on a rack above the counter."]
while True:
    if rtextdisplayed == False:
        print(regionalText[region])
        rtextdisplayed = True
    command = input()
    if command == "inventory":
        print(inventory)
    if region == 1 & rtextdisplayed == True:
        if command == "walk to door":
            print("Going north...")
            time.sleep(0.5)
            region = 2
            rtextdisplayed = False
        if command == "walk to kitchen":
            print("Going west...")
            time.sleep(0.5)
            region = 3
            rtextdisplayed = False
        if command == "use television":
            print("You turn on the televsion. There is a announcer, delivering the news.")
            time.sleep(3)
            print("Always be on the lookout for the Mutants.")
            print("The Mutants, eh? Is that what they're calling us?")
            time.sleep(3)
            print("Already 6 of the nasty creatures are locked up in the main police station in Tokyo.")
            print("Aha! So that's where I should start.")
            time.sleep(3)
            print("The news stops, to be replaced by a cartoon about a boy trying to become a 'Pokeyman Mister?' Or something like that.")
    if region == 2 & rtextdisplayed == True:
        if command == "walk to door":
            print("Going south...")
            time.sleep(0.5)
            region = 1
            rtextdisplayed = False
        if command == "walk left":
            print("Going west...")
            time.sleep(0.5)
            region = 4
            rtextdisplayed = False
        if command == "walk right":
            print("Going east...")
            time.sleep(0.5)
            region = 5
            rtextdisplayed = False
        if command == "use television":
            print("You turn on the televsion. There is a announcer, delivering the news.")
            time.sleep(3)
            print("Always be on the lookout for the Mutants.")
            print("The Mutants, eh? Is that what they're calling us?")
            time.sleep(3)
            print("Already 6 of the nasty creatures are locked up in the main police station in Tokyo.")
            print("Aha! So that's where I should start.")
            time.sleep(3)
            print("The news stops, to be replaced by a cartoon about a boy trying to become a 'Pokeyman Mister?' Or something like that.")
    if region == 3 & rtextdisplayed == True:
        if command == "pick up knife":
            print("You pick up the sharpest seeming knife.")
            time.sleep(0.5)
            inventory.extend("Knife")
            rtextdisplayed = False
        if command == "walk to kitchen":
            print("Going west...")
            time.sleep(0.5)
            region = 3
            rtextdisplayed = False
        if command == "use television":
            print("You turn on the televsion. There is a announcer, delivering the news.")
            time.sleep(3)
            print("Always be on the lookout for the Mutants.")
            print("The Mutants, eh? Is that what they're calling us?")
            time.sleep(3)
            print("Already 6 of the nasty creatures are locked up in the main police station in Tokyo.")
            print("Aha! So that's where I should start.")
            time.sleep(3)
            print("The news stops, to be replaced by a cartoon about a boy trying to become a 'Pokeyman Mister?' Or something like that.")











































