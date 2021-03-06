from sys import exit


def gold_room():
    print "This room is full of gold. How much do you take?"

    gold = raw_input("> ")
    try:
        how_much = int(gold)
    except Exception:
        dead("Man, learn to type a number.")

    if how_much < 50:
        print "Nice, you're not greedy, you win!"
        exit(0)
    else:
        dead("You greedy bastard!")


def bear_room():
    print "There is a bear here."
    print "The bear has a bunch of honey."
    print "The fat bear is in front of another door."
    print "How are you going to move the bear?"
    bear_moved = False

    while True:
        x = raw_input("> ")

        if x == "take honey":
            dead("The bear looks at you then slaps your face off.")
        elif x == "taunt bear" and not bear_moved:
            print "The bear has moved from the door. " \
                  "You can go through it now."
            bear_moved = True
        elif x == "taunt bear" and bear_moved:
            dead("The bear gets pissed off and chews your leg off.")
        elif x == "open door" and bear_moved:
            gold_room()
        else:
            print "I got no idea what that means."


def cthulhu_room():
    print "Here you see the great evil Cthulhu."
    print "He, it, whatever stares at you and you go insane."
    print "Do you flee for your life or eat your head?"

    x = raw_input("> ")

    if "flee" in x:
        start()
    elif "head" in x:
        dead("Well that was tasty!")
    else:
        cthulhu_room()


def dead(why):
    print why, "Good job!"
    exit(0)


def start():
    print "You are in a dark room."
    print "There is a door to your right and left."
    print "Which one do you take?"

    x = raw_input("> ")

    if x == "left":
        bear_room()
    elif x == "right":
        cthulhu_room()
    else:
        dead("You stumble around the room until you starve.")


start()
