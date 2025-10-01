print("*** Welcome to Basic Calculator ***")
print("Choose a mathematical operation: ")
userChoice = int(input("(1) Add two numbers\n(2) Subtract two numbers\n(3) Multiply two numbers\n(4) Divide two numbers\n(5) Remainder of the division of two numbers\n"))

firstNumber = int(input("Type in the first number: "))
secondNumber = int(input("Type in the second number: "))

def addition():
  return firstNumber + secondNumber
def subtraction():
  return firstNumber - secondNumber
def multiplication():
  return firstNumber * secondNumber
def division():
  return firstNumber / secondNumber 
def remainder():
  return firstNumber % secondNumber
 
match userChoice:
  case 1:
    total = addition()
    print(f"The addition of {firstNumber} + {secondNumber} is {total}")
  case 2:
    total = subtraction()
    print(f"The subtraction of {firstNumber} - {secondNumber} is {total}")
  case 3:
    total = multiplication()
    print(f"The multiplication of {firstNumber} * {secondNumber} is {total}")
  case 4:
    total = division()
    print(f"The division of {firstNumber} / {secondNumber} is {total}")
  case 5:
    total = remainder()
    print(f"The remainder of the division of {firstNumber} / {secondNumber} is {total}")
  case _:
    print("Invalid menu choice.")
    