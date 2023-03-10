l1 = ["r", "p", "s"]
import random
def funchion1():
    print("input r for rock p for papper and s for sizzors")
    x = input ("")
    if ((x) in l1):#seing if x is r,p or s 
        a = ("true")
    else:
        a = 3
    while a == 3:
        print ("error")
        funchion1 ()
    y = (random.randint(1,3))
    if x == ("r"):#player
        x = ("rock")
    if x == ("p"):
        x = ("papper")
    if x == ("s"):
        x = ("sizzors")


    if y == 1:#computer
        y = ("rock")
    if y == 2:
        y = ("papper")
    if y == 3:
        y = ("sizzors")
    #display awnsers
    print ("you-"+(x))
    print ("computer-"+(y))
    # x = player and y = computer
    if x == y:
        print ("tie")#win deteshion
    if y == ("rock") and x == ("papper"):
        print ("you win!")
    if y == ("rock") and x == ("sizzors"):
        print ("computer wins!")
    if y == ("papper") and x == ("rock"):
        print ("computer wins!")
    if y == ("papper") and x == ("sizzors"):
        print ("you win!")
    if y == ("sizzors") and x == ("rock"):
        print ("you win!")
    if y == ("sizzors") and x == ("papper"):
        print ("computer wins!")
    x = input ("do you want tp retry y/n?")
    if x == ("y"):
        funchion1 ()
    else:
        print ("ok.")
funchion1 ()
#make a score counter
