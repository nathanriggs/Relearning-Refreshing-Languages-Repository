#!/usr/bin/env python3

#
#  -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
# [                                                       ]
# [ Program Header:                                       ]
# [                                                       ]
# [ Creator:  Nathan Riggs                                ]
# [ Date:                                                 ]
# [ Language: Python 3.8                                  ]
# [                                                       ]
# [ Description:                                          ]
# [                                                       ] 

# [                                                       ]
#  -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
#
## Variable Declariations
#



# add some space
print("\n\n\n\n")
#

#
## get floating-point value for an input
#
def get_float(prompt, low, high):
    answer = -1.0
    while answer < low or answer > high:
        answer = float(input(prompt))
        if answer < low or answer > high:
            print("ERROR: value must be between " + str(low) + " and " + str(high))
            print("Please re-enter an appropriate value.\n")
    return answer
#
## get integer value for an input
#
def get_int(prompt, low, high):
    return int(get_float(prompt,low,high))



#
## test to make sure the get_float() and get_int() routines work
#
def main():
    choice = "y"
    while choice.lower() == "y":

        print(get_float("float (0..200) = ",0,200))
        print(get_int("integer (0..200) = ",0,200))
        
        # see if the user wants to continue
        choice = input("Continue? (y/n): ")
        print()

    print("Bye!")
    
if __name__ == "__main__":
    main()
