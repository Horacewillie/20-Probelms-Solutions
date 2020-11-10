# -*- coding: utf-8 -*-
"""
Created on Mon Nov  9 09:50:04 2020

@author: Admin
"""

# Name Concatenation


first_name = input("Please enter your first name :")
last_name = input("Please enter your last name: ")
age = int(input("We are almost done, I'll need your age also: "))

current_year = 2020
year_of_birth = current_year - age

gender = input("Gender: ").lower()
if gender == "male":
    print("\nWelcome {}, son of {}. \nBorn in the year {}".format(first_name, last_name, year_of_birth))
else:
    print("\nWelcome {}, daughter of {}. \nBorn in the year {}".format(first_name, last_name, year_of_birth))



