#!/usr/bin/env python3

"""
 -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
[                                                       ]
[ Program Header: Exercise 3.3                          ]
[                                                       ]
[ Creator:  Nathan Riggs                                ]
[ Date:     14-JUL-2020                                 ]
[ Language: Python 3.8                                  ]
[                                                       ]
[ Description:                                          ]
[                                                       ]

[                                                       ]
 -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
"""
#
## Variable Declariations
#

choice = "y"                # choice to continue entering values
monthly_investment = 0      # monthly investment in dollars
yearly_interest_rate = 0    # interest rate percentage, between 0 and 16
years = 0                   # number of years of savings
months = 0                  # number of year * 12
future_value = 0            # Future value in savings account
i = 0                       # for loop counter


# add some space
print("\n\n\n\n")
###
##
#


# display a welcome message
print("Welcome to the Future Value Calculator")
print()

while choice.lower() == "y":

    # get input from the user
    monthly_investment = float(input("Enter monthly investment:\t"))
    yearly_interest_rate = float(input("Enter yearly interest rate:\t"))
    years = int(input("Enter number of years:\t\t"))

    # convert yearly values to monthly values
    monthly_interest_rate = yearly_interest_rate / 12 / 100
    months = years * 12

    # calculate the future value
    future_value = 0
    for i in range(months):
        future_value += monthly_investment
        monthly_interest_amount = future_value * monthly_interest_rate
        future_value += monthly_interest_amount

    # display the result
    print("Future value:\t\t\t" + str(round(future_value, 2)))
    print()

    # see if the user wants to continue
    choice = input("Continue (y/n)? ")
    print()

print("Bye!")
