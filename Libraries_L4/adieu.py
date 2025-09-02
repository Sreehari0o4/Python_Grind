# In this problem, you are asked to write a program that prompts the user for names, one per line, until the user signals EOF. 
# After all names have been input, the program should bid adieu to those names using proper English grammar (with commas and "and" where appropriate).

import sys
import inflect

p = inflect.engine()

names = []
while True:
    try:
        names.append(input("Name: "))
    except EOFError:
        print("Adieu, adieu, to " + p.join(names))
        sys.exit()