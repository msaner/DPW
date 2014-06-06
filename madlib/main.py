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
future_date = int(dob) + 1256
print future_date

if color in animal:
    print(animal[color])