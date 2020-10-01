#!/usr/bin/env python3

"""
 -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
[                                                       ]
[ Program Header: Exercise 3.1                          ]
[                                                       ]
[ Creator:  Nathan Riggs                                ]
[ Date:     13-JUL-2020                                 ]
[ Language: Python 3.8                                  ]
[                                                       ]
[ Description:                                          ]
[                                                       ]
[  Add a loop to let the user enter repeated            ]
[  entries for the whole trip in terms of mileage       ]
[  with a while loop. Then, modify it to get the        ]
[  cost of gallon of gas as another entry, and then     ]
[  validate this entry before using it in the code      ]
[  calculations. If all thre entries are valid,         ]
[  then total gas cost and cost per mile, and           ]
[  display to user.                                     ]
[                                                       ]
 -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
##
#
## Variable Declariations
#
"""
choice = "n"
entry = 0
miles_driven = 0.0
gallons_used = 0.0
cost_per_gal = 0.0
mpg = 0.0
total_cost = 0.0

# add some space
print("\n\n\n\n")
#
#
#


# display a welcome message
print("The Miles Per Gallon application")
print()

while choice != "y" or choice != "Y":
    # get input from the user
    print("Enter round " + str(entry) + " of miles driven and gallons used.")
    print("\n");
    miles_driven += float(input("Enter miles driven this round: "))
    gallons_used += float(input("Enter gallons of gas used this round: "))
    entry += 1
    print()
    if miles_driven <= 0:
        print("Miles driven must be greater than zero. Please try again.")
        continue
    elif gallons_used <= 0:
        print("Gallons used must be greater than zero. Please try again.")
        continue
    else:
        choice = input("Continue entering trip? (y/n)")
        if choice == "y" or choice == "Y":
            continue
        else:
            break

mpg = round(miles_driven / gallons_used, 2)
choice = "n"
#
# note that the book exercise instructions aren't clear on
# whether the entire program should be in a loop, or just adding up
# a number of trips. I've assumed the second option, because the first
# option is prett damned simple, even at this stage in the book
#
while choice == "n" or choice == "N":
    # calculate the miles per gallon
    cost_per_gal = round(float(input("What's the cost of a gallon of gas? ")),2)
    choice = input("\n\nJust to verify, the cost of gasoline is " + str(cost_per_gal) + " per mile? (Y/N)")
    continue


print("\n\nTotal Miles Per Gallon:          ", mpg)
total_cost = round(cost_per_gal * mpg,2)

print("Total Cost: ", total_cost)
print("\n\n\n")




print("Bye")



