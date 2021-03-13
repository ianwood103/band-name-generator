import inflect
import csv
import json
import random

engine = inflect.engine();
animals = json.load(open("animals.txt"))
adjectives = json.load(open("adjectives.txt"))

print("The " + adjectives[random.randint(0,len(adjectives))].split(" ")[1].capitalize() + " " + engine.plural(animals[random.randint(0,len(animals))]).split(" ")[-1])
