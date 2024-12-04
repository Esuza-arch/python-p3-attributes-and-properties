#!/usr/bin/env python3

APPROVED_BREEDS = [
    "Mastiff",
    "Chihuahua",
    "Corgi",
    "Shar Pei",
    "Beagle",
    "French Bulldog",
    "Pug",
    "Pointer"
]

class Dog:
    APPROVED_BREEDS = ["Labrador", "Pug", "Bulldog", "Beagle", "Chihuahua"]

    def __init__(self, name=None, breed=None):
        if name is not None:
            if not isinstance(name, str) or not (1 <= len(name) <= 25):
                print("Name must be string between 1 and 25 characters.")
                return
            self.name = name
        else:
            self.name = None

        if breed is not None:
            if breed not in self.APPROVED_BREEDS:
                print("Breed must be in list of approved breeds.")
                return
            self.breed = breed
        else:
            self.breed = None


