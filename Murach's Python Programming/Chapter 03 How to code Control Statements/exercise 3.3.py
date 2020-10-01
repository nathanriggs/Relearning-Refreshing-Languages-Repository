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
[ This exercise calculates the value of savings each    ]
[ year after compound interest is added. It also checks ]
[ for invalid values, as the exercise requires.         ]
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
months = 12                 # number of year * 12
future_value = 0            # Future value in savings account
i = 0                       # for loop counter


# add some space
print("\n\n\n\n")
####
###
##
#


# display a welcome message
print("Welcome to the Future Value Calculator")
print("======================================")
print()

while choice.lower() == "y":

    monthly_investment = 0        # reset variables
    yearly_interest_rate = 0
    years = 0
    future_value = 0

    # get input from the user
    while monthly_investment <= 0:
        monthly_investment = float(input("Enter monthly investment:\t"))
        if monthly_investment <= 0:
            print("Error: investment needs to be greater than zero.")
            print()
            

    while yearly_interest_rate <= 0 or yearly_interest_rate >= 16:       
        yearly_interest_rate = float(input("Enter yearly interest rate:\t"))
        if yearly_interest_rate <= 0 or yearly_interest_rate >= 16:
            print("Error: Interest rate must be between 1 and 15.")
            print()

    while years <= 0 or years > 50:              
        years = int(input("Enter number of years:\t\t"))
        if years <= 0 or years > 50:
            print("Error: years must be between 1 and 50 years.")
            print()

    print()
    # convert yearly values to monthly values
    monthly_interest_rate = yearly_interest_rate / 12 / 100
    months = years * 12

    # calculate the future value
    future_value = 0
    for i in range(months):
        future_value += monthly_investment
        monthly_interest_amount = future_value * monthly_interest_rate
        future_value += monthly_interest_amount

        # print each year's value after calculating compound interest
        if i % 12 == 0:
           print("Year " + str(int((i/12)+1)) + " future value = \t\t" + str(round(future_value,2)))

    # see if the user wants to continue
    print()
    choice = input("Continue (y/n)? ")
    print()

print("Bye!")
