import random

list = ["car", "zonk1", "zonk2"]
randlist = random.sample(list, 3)

door1 = randlist[0]
door2 = randlist[1]
door3 = randlist[2]

pick = input("Pick a door. (Type 1, 2, or 3)")
firstpick = int(pick)
firstpickindex = firstpick - 1

if randlist[firstpickindex] != "zonk1":
    print("Behind door ", randlist.index('zonk1') + 1, " is a zonk.")
    shown = 'zonk1'
else:
    print("Behind door", randlist.index('zonk2') + 1, "is a zonk.")
    shown = 'zonk2'

choice = input("Would you like to keep or change doors?")

if choice == 'change':
    if shown == 'zonk1':
        finalpick = [x for x in list if x not in [randlist[randlist.index('zonk1')], randlist[firstpickindex]]]
        finalpickitem = finalpick[0]
        finalpickindex = randlist.index(finalpickitem)
    elif shown == 'zonk2':
        finalpick = [x for x in list if x not in [randlist[randlist.index('zonk2')], randlist[firstpickindex]]]
        finalpickitem = finalpick[0]
        finalpickindex = randlist.index(finalpickitem)
elif choice == 'keep': #fix it so else repeats the input question
    finalpickindex = firstpickindex

if randlist[finalpickindex] != 'car':
    print("You do not get a car.")
elif randlist[finalpickindex] == 'car':
    print("You get the car!")


print(door1,door2,door3)