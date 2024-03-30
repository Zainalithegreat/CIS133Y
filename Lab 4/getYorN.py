# Function to get a y or n from a user, if anything else 
# is input it will keep requesting user to enter valid input


def yOrN():
  YorN = input(
    "Would you like to build a sandwich? (y/n): ")
  YorN = YorN.lower()
  while True:
    if YorN  == 'y' or YorN == "n":
      return YorN
    else: 
      print(f'You entered {YorN} which is an invalid choice.')        
      print(f'Please try again.')
      print()
      YorN = input(
        "Would you like to build a sandwich? (y/n): ")
      YorN = YorN.lower()
