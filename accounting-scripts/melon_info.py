"""Print out all the melons in our inventory."""

from melons import *


def print_melons(melon_data = melon_data):
    for melon in melon_data:
        print(melon.upper())
        for attribute, value in melon_data[melon].items():
            if type(value) == float:
                print(f"{attribute}: {value:.2f}")
            else: print(f"{attribute}: {value}")
        print()

print_melons()