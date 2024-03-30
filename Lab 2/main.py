
#******************************************************************************
# Author:           Zain Ali & Ben du Chalard
# Lab:              Lab 2 Rev 2
# Date:             1/23/2024
# Description:      This program will calculate the total cost of college/university
#
# Input:            name, years in school, interest rate, borrowed per term
# Output:           Total cost of loan college
# Sources:          
#
#
#******************************************************************************
import datetime

# added import locale and decimal for Rev 2  ~ Ben du
import locale as lc
from decimal import Decimal
from decimal import ROUND_HALF_UP

# function to get inputs from user
def get_inputs():
  print(f"Welcome to this program, we will be calculating interest for a college student'\n")
  userName = input("What is your name: ")
  yearsInSchool = int(input("How many years until you graduate?: "))
  numberOfTerms = yearsInSchool * 3
  borrowedPerTerm = Decimal(input("How much money will you need to borrow per term?: "))
  borrowedPerTerm = borrowedPerTerm.quantize(Decimal("1.00"), ROUND_HALF_UP)
  interestRate = Decimal(input(f"What is the interest rate?: "))
  

  return userName, yearsInSchool, numberOfTerms, borrowedPerTerm, interestRate

# function to calculate the total cost of the loan
def calc_interest(borrowedPerTerm, interestRate, numberOfTerms):
  interest = interestRate / 12 / 100
  months = numberOfTerms * 4 
  futureValue = Decimal("0.00")
  currentDate = datetime.date.today()
  for i in range(months):
    if i % 4 == 0:
      futureValue += borrowedPerTerm
    monthlyInterest = futureValue * interest
    futureValue += monthlyInterest
    print(f"After {currentDate} date the total intereset is ", format(futureValue, ".2f"))
  futureValue = futureValue.quantize(Decimal("1.00"))
  return futureValue
  


# main function to call other functions
def main():
  userName, yearsInSchool, numberOfTerms, borrowedPerTerm, interestRate = get_inputs()
  totalMoney = calc_interest(borrowedPerTerm, interestRate, numberOfTerms)
  print()
  print(userName + ", you will have to pay back", format(totalMoney, ".2f"), "when you graduate")



  #s1 = 10
  #s2 = '>20'
  #print(f"{'Invoice total:'} {'whatever'} {totalMoney:{s2}}")

# used to call main function when file is main
if __name__ == '__main__':
 main()

