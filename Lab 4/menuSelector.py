#******************************************************************************
# Author:           Zain Ali & Ben du Chalard
# Lab:              Lab 4
# Date:             2/15/2024
# Description:      This programs let your picks the toppings for a Sandwich
#
# Input:            Toppings
# Output:           Built Sandwich
# Source:
#
#
#*****************************************************************************

# Provides user with prompt for entering a number from len of the menu list
def menuSelector(option):
  choice = 0
  for i in range(len(option)):
      print(f"{i + 1}:", option[i])   
  choice = input("Choose an index: ")
  while not choice.isdigit() or int(choice) < 1 or int(choice) > len(option):
      print("Invalid input. Please enter a valid index.")
      choice = input("Choose an index: ")
  return int(choice) - 1



