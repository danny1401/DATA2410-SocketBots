import random


def alice(a, b=None):
    return "I think {} sounds great!".format(a + "ing")


def bob(a, b=None):
    if b is None:
        return "Not sure about {}. Don't I get a choice?".format(a + "ing")
    return "Sure, both {} and {} seems ok to me".format(a, b + "ing")


def dora(a, b=None):
    action = a + "ing"
    alternatives = ["coding", "singing", "sleeping", "fighting"]
    b = random.choice(alternatives)
    return "Yea, {} is an option. Or we could do some {}.".format(action, b)


def chuck(a, b=None):
    action = a + "ing"
    bad_things = ["fighting", "bickering", "yelling", "complaining"]
    good_things = ["singing", "cheating", "playing", "working"]
    if action in bad_things:
        return "YESS! Time for {}".format(action)
    elif action in good_things:
        return "What? {} sucks. Not doing that.".format(action)
    return "I don't mind!"
