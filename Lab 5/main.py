#******************************************************************************
# Author:           Ben du Chalard
# Lab:              Lab 6, Name.py
# Date:             2/26/2024
# Description:      This program is for learning how object oriented 
#                    programming works
#
# Input:            Maybe a database
# Output:           Formated data
# Source:           PCC CIS133 Lab 6 Instructions
#                   Requirments
#                     (x) At least one list or dictionary
#                     (x) Contain at least three files, driver and two modules
#                     (x) Validate user input
#                     (x) Use at least one loop to accesss the list data
#                     (x) Use at least two "if" decison structures to access the list data
#                     (x) Must make changes to the list or dictionary
#                     (x) Orangize code into separate functions, input, output, calac, 
#                     (x) Use parameter and arguments to pass vlaues into functions (no global)
#
#******************************************************************************

from getMenuNo import getMenuNo
from displayMenu import displayMenu
from displayDonuts import displayDonuts
from arrayAppend import arrayAppend

print("Welcome to your donut tracker!")



#def donutEater():
#  eat = int(input("How many donuts do you want to eat?: "))

def main():
  eatMore = "y"
  donuts = ["Maple Bars", "Bismarks", "Bear Claws", "Jelly Filled"]
  donutInventory = [12, 12, 12, 12]
  menu = ["Dispaly Donut Inventory", "Eat Donuts", "Quit"]
  while eatMore == "y":
    print()
    displayMenu(menu)
    print()
    menuNo = getMenuNo(menu)
    if menuNo == 1:
      print()
      print('These are the donuts you have left')
      displayDonuts(donuts, donutInventory)
      print()
    elif menuNo == 2:
      print()
      if not donutInventory and not donuts:
        print("List is empty")
        break
      print('What donut do you want to eat?: ')
      displayDonuts(donuts, donutInventory)
      print()
      number = getMenuNo(donuts)
      print("you selected", number)
      arrayAppend(donuts, donutInventory, number - 1)
    elif menuNo == 3:
      print()
      print("Can't eat anymore, Bye!")
      break
      


if __name__ == "__main__":
  main()
