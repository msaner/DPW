'''
DPW Project 1 - Madlib
Developer: Michael Saner
Date: June 5 2014
'''

#establish prompts for users to enter information we will use later to create our story

name = raw_input("Enter a persons name and hit enter.")
dob = raw_input("Enter the year you were born and hit enter.")
number = raw_input("Enter an even number and hit enter.")
adjective1 = raw_input("Enter an adjective and hit enter.")
verb1 = raw_input("Enter a verb and hit enter.")
verb2 = raw_input("Enter another verb and hit enter.")
pets = raw_input("Enter how many pets you have and hit enter.")
color = raw_input("Enter your favorite color of the rainbow; (red orange yellow green blue or purple) and hit enter.")

#setting up a dictionary to house values based on the different colors a user might enter
animal = dict()
animal = {"red":"unicorn", "orange":"beaver", "yellow":"squirrel", "green":"duck", "blue":"eagle", "purple":"t-rex"}

# we're going to add the users year of birth to a number to get a year in the future by adding the two numbers
# dob is a string so we need to convert that to an integer so we can add it.  do this by adding int()
future_date = int(dob) + 1256
print future_date

if color in animal:
    new_animal = (animal[color])

#getting rid of the indenting ends the if statement

'''
now we will figure out how many animals there will be in our story by making an equation
dont forget that the variable is a sting so we have to convert it to an integer with int()
'''

def pack_size(number):
    size = int(number) * 9 - 1
    return size

pack = pack_size(number);
print pack

#lets analyze the pack_size and figure out how we are going to describe it in terms of size
if pack > 10:
    pack_desc = "massive herd"
else:
    pack_desc = "gang"

print pack_desc

print "In the year " + str(future_date) + " " + name + " was " + verb1 + " the small town of Kokomo. " + " Suddenly, a " + pack_desc + " of " + adjective1 + " " + new_animal + " was " + verb2 + " the town!" + " " + name + " was not in a fighting mood so he grabbed " + pets + " Dr. Peppers a hot dog and found a nice bean bag to have lunch in."