# Gets a number for menu from the user, passed a list to give number of indexs
# Error checking for menu number not in range
# Error checking for if not a number is entered

def getMenuNo(menu):
  # sets upper and lower numbers of menu
  low = 1
  high = len(menu)
  
  while True:
    try:
      menuNo = int(input("Enter a menu number.: "))
    except ValueError:
      print("Invalid menu input. Please try again.")
      continue
    if menuNo >= low and menuNo <= high:
      return menuNo
    else:
      print("Invalid menu number. Please try again.")