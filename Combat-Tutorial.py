import time
print("WELCOME TO THE OFFICIAL INTO THE WILDS COMBAT TUTORIAL.")
time.sleep(3)
print("IN INTO THE WILDS, COMBAT IS WHEN LETTERS, W, A, S, AND D, APPEAR ON THE SCREEN.")
time.sleep(3)
print("YOU NEED TO TYPE THOSE LETTERS IN.")
time.sleep(3)
print("IN INTO THE WILDS, IT IS RECOMMENDED THAT YOU HAVE CAPS LOCK ON AT ALL TIMES.")
time.sleep(3)
def w():
    time.sleep(0.5)
    print("W")
    w = input()
    if w.lower() == "w":
        print("GREAT!")
    else:
        print("THAT'S NOT W! TRY AGAIN.")
        w()
w()
def a():
    time.sleep(0.5)
    print("A")
    a = input()
    if a.lower() == "a":
        print("GREAT!")
    else:
        print("THAT'S NOT A! TRY AGAIN.")
        a()
a()
def s():
    time.sleep(0.5)
    print("S")
    s = input()
    if s.lower() == "s":
        print("GREAT!")
    else:
        print("THAT'S NOT S! TRY AGAIN.")
        s()
s()
def d():
    time.sleep(0.5)
    print("D")
    d = input()
    if d.lower() == "d":
        print("GREAT!")
    else:
        print("THAT'S NOT D! TRY AGAIN.")
        d()
d()
print("CONGRATULATIONS, YOU HAVE COMPLETED THE INTO THE WILDS COMBAT TUTORIAL.")
time.sleep(3)
print("NOW YOU MAY PLAY THE REAL GAME.")
