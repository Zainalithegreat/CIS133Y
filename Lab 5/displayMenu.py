
# Display the contents of a list and index number+1 when passed as an argument
def displayMenu(menu):
  for i in range(len(menu)):
    print(f'{i+1}:', menu[i])

