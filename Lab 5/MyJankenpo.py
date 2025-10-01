import random
print("Welcome to the randomized jankenpo machine, choose your option:")
playerOption = int(input("(1) rock\n(2) paper\n(3) scissors\n(4) smartphone\n"))

#The smarphone wins against paper and scissors but loses against stone

machineOption = random.randint(1, 4)

if playerOption == 1: 
  print("Player played rock")
elif playerOption == 2: 
  print("Player played paper")
elif playerOption == 3: 
  print("Player played scissors")
elif playerOption == 4: 
  print("Player played smartphone")

if machineOption == 1: 
  print("Machine played rock")
elif machineOption == 2: 
  print("Machine played paper")
elif machineOption == 3: 
  print("Machine played scissors")
elif playerOption == 4: 
  print("Machine played smartphone")

#Machine winning
if playerOption == 1 and machineOption == 2:
  print("The machine won the game.")
elif playerOption == 2 and machineOption == 3:
  print("The machine won the game.")
elif playerOption == 3 and machineOption == 1:
  print("The machine won the game.")
elif playerOption == 4 and machineOption == 1:
  print("The Player won the game.")
elif playerOption == 2 and machineOption == 4:
  print("The Player won the game.")
elif playerOption == 3 and machineOption == 4:
  print("The Player won the game.")


#Player winning
elif machineOption == 1 and playerOption == 2:
  print("The Player won the game.")
elif machineOption == 2 and playerOption == 3:
  print("The Player won the game.")
elif machineOption == 3 and playerOption == 1:
  print("The Player won the game.")
elif machineOption == 4 and playerOption == 1:
  print("The Player won the game.")
elif machineOption == 2 and playerOption == 4:
  print("The Player won the game.")
elif machineOption == 3 and playerOption == 4:
  print("The Player won the game.")

#Draw
else:
  print("The game was a draw")





