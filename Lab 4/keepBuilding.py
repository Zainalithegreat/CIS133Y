# Function to get a y or n from a user, if anything else 
# is input it will keep requesting user to enter valid input


def yOrN():
  keepGoing = 'y'
  while keepGoing == 'y':
    keepGoing = input(
      "Would you like to build a sandwich? (y/n): ")
    return keepGoing
  if keepGoing =="n":
    return keepGoing
  while keepGoing != 'n' and keepGoing != 'y':
      print("Invalid please try again")
      keepGoing = input("Would you like to build your sandwich? (y/n): ")
      return keepGoing
