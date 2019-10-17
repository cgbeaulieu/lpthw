import random

print("""You enter a dark room with two doors.
Do you go through door #1 or door #2?""")

door = input("> ")

if door == "1":
    print("There's a giant bear here eating a cheese cake.")
    print("Roll for initiative.")

    input("> Press ENTER to roll.")

    bear = random.randint(1, 20)
    
    if bear == 1:
        print(f"CRITICAL FAILURE! You rolled a {bear}!  ")
        print("The bear eats your face off.  You are dead.  Good job!")
    elif bear in range (2, 10):
        print(f"You rolled a {bear}!")
        print("The bear eats your legs off.  You are dead.  Good job!")
    elif bear in range (11, 19):
        print(f"You rolled a {bear}!")
        print("The bear swipes at you but you're able to dodge it and run out the door.  Good job!")
    else:
        print(f"CRITICAL HIT!  You rolled a {bear}!")
        print("Bear runs away.")

elif door == "2":
    print("You stare into the endless abyss of Cthulu's retina.")
    print("1. Blueberries.")
    print("2. Yellow jacket clothespins.")
    print("3. Understanding revolvers yelling melodies.")

    insanity = input("> ")

    if insanity == "1" or insanity == "2":
        print("Your body survives powered by a mind of jello puddin'.")
        print("Good job!")
    else:
        print("The insanity rots your eyes into a pool of muck.")
        print("Good job!")

else:
    print("You stumble around and fall on a knife and die.")
    print("Good job!")