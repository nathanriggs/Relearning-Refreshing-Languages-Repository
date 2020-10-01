#!/usr/bin/env python3

#######################################################
##                                                   ##
## Program Header: Exercise 2.                      ##
##                                                   ##
## Creator:  Nathan Riggs                            ##
## Date:     12-JUL-2020                             ##
## Language: Python 3.8                              ##
##                                                   ##
## Description:                                      ##
##                                                   ##
##  Modify the test score program in the book to     ##
##  display the three scores entered by the user     ##
##  with a single line.                              ##
##                                                   ##
#######################################################
##
#
## Variable Declariations
#

total_score = 0                        # initialize total as int

# add some space

print("\n\n\n\n")

# display a welcome message
print("The Test Scores application")
print()
print("Enter 3 test scores")
print("======================")

# get scores from the user

score1 = int(input("Enter test score: "))
score2 = int(input("Enter test score: "))
score3 = int(input("Enter test score: "))
total_score = score1 + score2 + score3

# calculate average score
average_score = total_score / 3
average_score = round(average_score)
                
# format and display the result

print("======================")
print("Your Scores:  ", score1, score2, score3, sep=" ", end="\n")
print("Total Score:  ", total_score,
      "\nAverage Score:", average_score)
print()
print("Bye")


