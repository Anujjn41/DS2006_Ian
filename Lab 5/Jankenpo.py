import random
print("Welcome to the randomized jankenpo machine, choose your option:")
playerOption = int(input("(1) rock\n(2) paper\n(3) scissors\n"))

machineOption = random.randint(1, 3)

if playerOption == 1: 
  print("Player played rock")
elif playerOption == 2: 
  print("Player played paper")
elif playerOption == 3: 
  print("Player played scissors")

if machineOption == 1: 
  print("Machine played rock")
elif machineOption == 2: 
  print("Machine played paper")
elif machineOption == 3: 
  print("Machine played scissors")

#Machine winning
if playerOption == 1 and machineOption == 2:
  print("The machine won the game.")
elif playerOption == 2 and machineOption == 3:
  print("The machine won the game.")
elif playerOption == 3 and machineOption == 1:
  print("The machine won the game.")

#Player winning
elif machineOption == 1 and playerOption == 2:
  print("The Player won the game.")
elif machineOption == 2 and playerOption == 3:
  print("The Player won the game.")
elif machineOption == 3 and playerOption == 1:
  print("The Player won the game.")

#Draw
else:
  print("The game was a draw")





