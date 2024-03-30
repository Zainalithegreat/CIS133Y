#******************************************************************************
# Author:           Zain Ali & Ben du Chalard
# Lab:              Lab 4
# Date:             2/17/2024
# Description:      This programs let your picks the toppings for a Sandwich
#
# Input:            Toppings
# Output:           Built Sandwich
# Source:           Lab 4 Instructions
#
#
#******************************************************************************
# Used functions import

from getYorN import yOrN 
from menuSelector import menuSelector

# Welcome message
print("Welcome to the Sandwich Builder!")

print()

def main():
  # Contents of different menus
  meat = ["Chicken", "Roast Beef", "Turkey", "Ham", "Pastrami"]

  bread = ["Wheat Bread", "White Bread", \
           "5 Grain Bread", "Italian Herb Bread"]
  cheese = ["American Cheese", "Swiss Cheese", \
    "Cheddar Cheese", "Provolone Cheese"]
  
 # start while loop and runs until user enters n
  keepGoing = yOrN()
  while keepGoing == 'y':
    # If user enter y, starts menu selection
    if keepGoing == "y":
      breadChoice = menuSelector(bread)
      meatChoice = menuSelector(meat)
      cheeseChoice = menuSelector(cheese)
      # prints the sandwich with the toppings selected
      print(meat[meatChoice], "sandwich with",      cheese[cheeseChoice], "on",
      bread[breadChoice])
      print()
      keepGoing = yOrN()
    if keepGoing == "n":
      print()
      print("Bye")
      break
  
# Calls main function if named as is main
if __name__ == '__main__':
  main()


