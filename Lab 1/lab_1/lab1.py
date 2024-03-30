#******************************************************************************
# Author:           Zain Ali
# Lab:              Lab 1
# Date:             Jan 13, 2023
# Description:      This program asks for the subtotal, the tax and shipping of an item and then gives us the output of how much we have to pay.
#Input              float taxRate, float shipping, float itemCost, char more.
# Output:           float subtotal, float tax, float shipping
# Sources:          none
#******************************************************************************



# Shopping program
# Inputs: float cost, float taxRate, float shipping
# Outputs: float totalPrice

def main():
    taxRate = 0.0
    shipping = 0.0
    totalCost = 0.0

    totalCost = getItemCosts()
    taxRate, shipping = getOtherCosts()
    printReceipt(totalCost, taxRate, shipping)

    print("Thank you!")

# getItemCosts() prompts a user for a list of item
# costs and returns the sum
def getItemCosts():
    itemCost = 0.0
    totalCost = 0.0
    more = 'y'

    while more == 'y':
        itemCost = float(input("Enter item cost $ ")) #itemcost should have the c capital like this itemCost
        #print(itemcost)
        totalCost = totalCost + itemCost
        #print(totalCost)
        more = input("Do you have more items (y/n): ")

    return totalCost
 
# getOtherCosts() prompts a user for the tax rate
# and shipping costs and returns both inputs
def getOtherCosts():
    taxRate = 0.0
    shipping = 0.0

    taxRate = float(input("\nEnter tax rate (i.e. .075 for 7.5%): "))
    shipping = float(input("Enter shipping costs $ "))
    #By Zain, returning shipping, taxRate rather than taxRate, shipping
    return taxRate, shipping

# printReceipt() accepts total cost, tax rate, and 
# shipping costs and calculates and prints the tax 
# amount, and total cost
def printReceipt(totalCost, taxRate, shipping):
    subtotal = totalCost
    tax = subtotal * taxRate  # Calculate tax based on subtotal
    #print(tax)
    print("\nSubtotal: $", format(subtotal, ".2f"))
    print("Tax: $", format(tax, ".2f"))
    print("Shipping: $", format(shipping, ".2f"))
    print("------------------------")
    print("Please pay: $", format(subtotal + tax + shipping, ".2f"))


main()