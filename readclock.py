import time
readtime = 0.0
def startreadtime(readtime):
    time.sleep(0.01)
    readtime = readtime + 0.01
print("Press enter/return when you have finished reading the text.")
print("3")
time.sleep(1)
print("2")
time.sleep(1)
print("1")
time.sleep(1)
print("You are left in the holding cell for a few minutes, but soon a burly man with a patch saying CHIEF OF POLICE walks in.")
startreadtime(0)
stop = input()
if stop == "":
    print(readtime)
    readtime = 0
