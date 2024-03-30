# Displays the two passed lists 

def displayDonuts(donuts, donutInventory):
  for i in range(len(donuts)):
    print(f'{i+1}:', '(', donutInventory[i], ')', donuts[i],)