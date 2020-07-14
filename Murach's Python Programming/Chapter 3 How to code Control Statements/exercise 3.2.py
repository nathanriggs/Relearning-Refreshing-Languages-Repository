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
[ Alter the test score program to 1) allow for entering ]
[ multiple sets of test scores via another while loop,  ]
[ and 2) allows the user to quit entering scores by     ]
[ typing "end" instead of 999.                          ]
[                                                       ]
 -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
##
#
## Variable Declariations
#
"""

counter = 0
score_total = 0
test_score = "0"
keyword = "end"
choice = "y"



# add some space
print("\n\n\n\n")
#
#
#

# display a welcome message
print("The Test Scores application")
print("===========================")

while choice.lower() == "y":
    score_total = 0
    counter = 0
    
    print()
    print("Enter test scores. Type \"end\" to finish.")
    print()

    while test_score.lower() != keyword.lower():
        test_score = input("Enter test score: ")
        if test_score.lower() != keyword.lower():
            if int(test_score) >= 0 and int(test_score) <= 100:
                score_total += int(test_score)
                counter += 1
            else:
                print("Test score must be from 0 through 100. Score discarded. Try again.")

    # calculate average score
    average_score = round(score_total / counter)
                
    # format and display the result
    print("======================")
    print("Total Score:", score_total,
      "\nAverage Score:", average_score)
    print()

    choice = input("Enter another set of test scores? (y/n) ")


print()
print("Bye")


