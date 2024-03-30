from displayDonuts import displayDonuts

def arrayAppend(donuts, donutInventory, number):
  #input in to consume
  consume = input(f"How many {donuts[number]} donuts would you like to eat?: ")
# This checks if consume is more than donutInventory of number which means if 
# the donutInventory[number] is 12 and if we enter 13 or more for consume it 
# will have us reenter
# This also check if consume is less than 0
  while not consume.isdigit() or int(consume) > donutInventory[number] and int(consume) < 0:

    try:
      print("Please enter a valid number")
      consume = input(f"How many {donuts[number]} donuts Would you like to eat: ")
    except:
       print("Invalid menu input. Please try again.")
      
  #This changes the donutInventory meaning that this minuses donutInventory[number] from consume
  #Meaning if donutInventory[number] is 12 and consume is 9 then donutInventory[number] will be 3
  donutInventory[number] -= int(consume)
  #This checks if donutInventory[number] is 0
  if donutInventory[number] == 0:
    #Shift the values to the left
    # Example: If the array is [4, 7, 0, 8] and number is at index 2 (0-based indexing)
    #                                 ^ this is the number index
    # After this loop, it becomes [4, 0, 8, 8], the last element is removed later
    for i in range(number, len(donutInventory) - 1):
      donutInventory[i] = donutInventory[i + 1]
      donuts[i] = donuts[i + 1]
     # Remove the last element from both lists
    donutInventory.pop()
    donuts.pop()

  # Display the updated donuts and donutInventory
  displayDonuts(donuts, donutInventory) 

  
  