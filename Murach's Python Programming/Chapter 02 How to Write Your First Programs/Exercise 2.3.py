#!/usr/bin/env python3

#######################################################
##                                                   ##
## Program Header: Exercise 2.3                      ##
##                                                   ##
## Creator:  Nathan Riggs                            ##
## Date:     12-JUL-2020                             ##
## Language: Python 3.8                              ##
##                                                   ##
## Description:                                      ##
##                                                   ##
##  Modify the Miles Per Gallon program to create a  ##
##  program that gets the area and perimeter of a    ##
##  rectangle.                                       ##
##                                                   ##
#######################################################
##
#
## Variable Declariations
#

length = 0.0                           # initialize total as float
width = 0.0                            # initialize total as float
area = 0.0                             # initialize total as int
perimeter = 0.0                        # initialize total as int

# add some space

print("\n\n\n\n")
#


# display a welcome message
print("The Area and Perimeter Program")
print("-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=")
print()

# get input from the user
length = float(input("Enter the length:\t"))
width = float(input("Enter width:\t\t"))

# calculate area and permieter
area = length * width
perimeter = (length *2) + (width *2)
            
# format and display the result
print()
print("Area:\t\t\t" + str(area))
print("Perimeter:\t\t" + str(perimeter))
print()
print("Bye")


