#!/usr/bin/env python3

"""
 -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
[                                                       ]
[ Program Header: Exercise 3.2                          ]
[                                                       ]
[ Creator:  Nathan Riggs                                ]
[ Date:     14-JUL-2020                                 ]
[ Language: Python 3.8                                  ]
[                                                       ]
[ Description:                                          ]
[                                                       ]

[                                                       ]
 -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
##
#
## Variable Declariations
#
"""






# add some space
print("\n\n\n\n")
#
#
#

# display a welcome message
print("The Test Scores application")
print()
print("Enter test scores")
print("===========================\n\n")

# initialize variables
counter = 0
score_total = 0
test_score = 0

while test_score != 999:
    test_score = int(input("Enter test score (999 to end): "))
    if test_score >= 0 and test_score <= 100:
        score_total += test_score
        counter += 1
    elif test_score == 999:
        break
    else:
        print("Test score must be from 0 through 100. Score discarded. Try again.")

# calculate average score
average_score = round(score_total / counter)
                
# format and display the result
print("======================")
print("Total Score:", score_total,
      "\nAverage Score:", average_score)
print()
print("Bye")


