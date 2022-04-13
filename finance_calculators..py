# brings in extra functionality for math calculations
import math

# tells user what to input to proceed
intro = "Choose either 'investment' or 'bond' from the menu below to proceed: "

# prints line above
print(intro)

# gives user options
# multi-line string cleans up formatting
# indentation makes string more legible for user
options = """
investment      - to calculate the amount of interest you'll earn on interest
bond            - to calculate the amount you'll have to pay on a home loan 
"""

# the answers as strings
investment =    "investment"
bond =          "bond"

# saves user's choice as a variable
# formats options to eliminate differences in case, as well as spaces before and after
options_input = str(input(options).lower().strip())


# nested conditional statement
# handles what happens when user selects "investment"
if options_input ==    "investment":

    # asks the user how much they would like to deposit
    amount = int(input(
        "Please enter the amount you would like to deposit (enter the number only, in Rands): "
        ))
    
    # asks the user the interest rate on their investment
    rate = float(input(
        "Please enter the interest rate (enter the number only, as a percentage): "
        ))
    
    # asks the user how long they would like to invest their money for
    time = float(input(
        "Please enter the number of years you plan on investing for (please enter the number only): "
    ))
    
    # asks the user the type of interest they would like to earn
    interest_type = float(input(
        "Please type 1 for simple or 2 for compound interest: "
    ))

    # this is a placeholder
    # this will be the total amount, depending on whether the user selects simple or compound
    total = 0

    # conditional statement for simple or compound interest
    # if user selects "1", it will use the simple interest formula to calculate the total investment
    if interest_type == 1:

        # reassigns the "total" placeholder with this value
        total = amount * (1 + rate * time)

    # if the user selects "2", it will use the compound interest formula to calculate the total investment
    else:

        # reassigns the "total" placeholder with this value
        total = amount * math.pow((1 + rate), time)

    # prints the total value that the user would earn
    # rounds the total to two decimal places
    print("The amount you'll earn per annum is:", round(total, 2))

# handles what happens when the user selects (bond)
elif options_input ==   "bond":
    
    # asks the user the current value of the home
    value = float(input(
        "Please enter the current value of your house (enter the number only, in Rands) "
    ))

    # asks the user the interest rate of the bond
    rate = float(input(
        "Please enter the interest rate (enter the number only, as a percentage): "
        ))

    # asks the user the amount of time they would like to pay the bond over, in months
    time = float(input(
        "Please enter the number of months you plan to take to repay the bond (enter the number only) "
    ))

    # Formula as provided in assignment
    P = value
    i = (rate / 100) / 12 
    n = time

    total = (i * P)/(1 - (1+i) ** (-n))

    # prints amount to be paid each month
    # total rounded off to two decimal places
    print("The amount you'll pay per month is:", round(total, 2))