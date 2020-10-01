#!/usr/bin/env python3

#######################################################
##                                                   ##
## Program Header: Exercise 2.1                      ##
##                                                   ##
## Creator:  Nathan Riggs                            ##
## Date:     12-JUL-2020                             ##
## Language: Python 3.8                              ##
##                                                   ##
## Description:                                      ##
##                                                   ##
##  Modify the mpg.py program from the book to do    ##
##  two more calculations.                           ##
##                                                   ##
#######################################################
##
#

# display a welcome message
print("\n\n\n")
print("The Miles Per Gallon program")
print("-=-=-=-=-=-=-=-=-=-=-=-=-=-=")
print("")

# get input from the user
miles_driven = float(input("Enter miles driven:\t\t\t"))
gallons_used = float(input("Enter gallons of gas used:\t\t"))
gallon_cost = float(input("Enter cost of gasoline per gallon:\t"))
                     
# calculate miles per gallon
mpg = round(miles_driven / gallons_used, 1)
total_cost = round(gallons_used * gallon_cost,2)
cost_per_mile = round(total_cost / miles_driven, 2)
            
# format and display the result
print("")
print("Miles Per Gallon:\t\t\t" + str(mpg))
print("Total Cost:\t\t\t\t" + str(total_cost))
print("ncost_per_mile:\t\t\t\t" +str(cost_per_mile))
print("")
print("Bye")


