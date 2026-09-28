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
# Append to a list
name = input ("What is your name: ")
siblings.append("Jayshree") # <= adds the item to the end of the list
siblings.insert(3, "Vienna")
print(siblings)
#Remove from a list 
siblings.pop(3) # <= if no number given pop removes the last item
print(siblings)

#print each item in a list
for sibling in siblings:
    print(sibling)

# For Loops
for num in range(1,25):
    if num % 15 == 0:
       print("FizzBuzz")
    elif num % 3 == 0:
       print("Fizz") 
    elif num % 5 == 0:
       print("Buzz")
    else:
       print(num)

for num in range(2,20):
    print(num)