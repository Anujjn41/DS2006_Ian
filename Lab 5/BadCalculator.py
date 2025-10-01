print("*** Welcome to Basic Calculator ***")
print("Choose a mathematical operation: ")
userChoice = input("(1) Add two numbers\n(2) Subtract two numbers\n(3) Multiply two numbers\n(4) Divide two numbers\n") #Returns a string

firstNumber = input("Type in the first number: ") #Returns a string
secondNumber = input("Type in the second number: ") #Returns a string

match str(userChoice): #Uses str() when the cases an integers
  case 1:
    total = firsNumber + secondNumber
    print(f"The addition of {firsNumber} + {secondNumber} is {total}")
  case 2:
    total = firsNumber - secondNumber
    print(f"The subtraction of {firsNumber} - {secondNumber} is {total}")
  case 3:
    total = firsNumber * secondNumber
    print(f"The multiplication of {firsNumber} * {secondNumber} is {total}")
  case 4:
    total = firsNumber / secondNumber
    print(f"The division of {firstNumber} / {secondNumber} is {total}")
  case _:
    print("Invalid menu choice.")
    