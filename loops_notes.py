# TG, Loops Notes
import random

count = 1 # 1: start point

while count <= 10: # 2: stop point, boolean statement
    print(count)
    count += 1 # 3: increase iterater

ducks = 1 # start loop
goose = random.randint(1,11)

while True:
    if ducks == goose:
        break # ends the loop
    print("Duck. . . .")
    ducks += 1 #ducks = ducks + 1
print("GOOSE!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")

# Complex Data Type = holds other data in it
siblings = ["Alex", "Katie", "Andrew", "Tia", "Treyson", "Xavier", "Jake"] # -> surround by brackets -> every item separated by commas-> must be valid data type
print(siblings[2])
