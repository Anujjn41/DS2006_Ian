class Dog:

  def __init__ (self, name, age, breed, address):
    self.name = name
    self.age = age
    self.breed = breed
    self.address = address

  def bark(self):
    print(f"{self.name} looks at you and barks: Woof Woof!")

  def sleep(self):
    print(f"{self.name} is asleep, shhh!")

  def barkAt(self, target):
    print(f"{self.name} barked at {target}")

dog1 = Dog("Bidu", 1, "Mixed")
dog2 = Dog("Pipoca", 5, "German Sheperd")
dog3 = Dog("Luvinha", 18, "Puddle")

print(dog1.name)
print(dog2.name)
print(dog3.name)
dog1.bark()
print(dog1.bark())