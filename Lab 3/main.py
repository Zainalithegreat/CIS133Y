#******************************************************************************
# Author:           Zain Ali 
# Lab:              Lab 3
# Date:             1/30/2024
# Description:      This programs calculates a students GPA when given a grade for different classes 
#
# Input:            userName, num
# Output:           userName, grade, total
# Sources:          
#
#
#******************************************************************************

from decimal import Decimal
from decimal import ROUND_HALF_UP
#This function welcomes the user and lets them know what the program is about
def Welcome():
  print(f"Welcome to this program, this program will ask for your name and your grades for each class(0/4) 0 being 'F' and 4 being 'A', then it will output your GPA.\n")
#This function asks for users name and their grade [1/4] for a given class this function also returns users name the sum of each class and count
def UserInput():
  userName = input("What is your name: ")
  print()
  print("Entering -1 means the program ends")
  num = 0
  sum = 0
  count = 0
  while num != -1:
      try:
          num = float(input(f"Please enter your grade for class #{count + 1}: "))
          print()
          if num < -1 or num > 4:
              print("Grade must be between 0 and 4")
          if num > -1 and num < 5:
              sum += num
              count += 1
      except:
          print(f"Invalid input for class #{count + 1}. Please enter a valid grade between 0 and 4.")
          print()
  return userName, sum, count


#This function calculates grades based on total, total being sum / count. This function also returns grade and total
def CalculateGrade(sum, count):
  if(sum > 0):
    total = sum / count
    grade = ' '
    if total > 3.3 and total <= 4.0:
       grade = 'A';
    
    elif total > 2.7 and total <= 3.3:
       grade = 'B'
    
    elif total > 1.9  and total <= 2.7:
       grade = 'C'
    
    elif total > 1.1 and total <= 1.9:
       grade = 'D'
    
    elif total > 0.0 and total <= 1.1:
       grade = 'F'
  else:
    total = 0
    grade = 'F'
  return grade, total

#This is the main function where we call all the other functions
def main():
  q = "yes"
  Welcome()
  while (q == "yes" or q == "y"):
    userName, sum, count = UserInput()
    grade, total= CalculateGrade(sum, count)
    print(f"{userName} your grade is '{grade}' and your GPA is ", format(total, ".2f"))
    q = input("Would you like to continue with new inputs: ")
    while q != "yes" and q != "no" and q != "n" and q != "y":
      q = input("Please enter [y/n] or [yes/no]: ")
    
#This is where we call the main fuction 
if __name__ == '__main__':
 main()