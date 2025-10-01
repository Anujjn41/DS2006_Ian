class Cat:

  def __init__ (self, name, breed,):
    self.name = name
    self.breed = breed

  def piss(self):
    print(f"{self.name} pissed on the sofa :(")

  def pissAt(self, target):
    print(f"{self.name} pissed at {target}'s bed :(")

cat1 = Cat("Mittens", "Persian")
cat2 = Cat("Tom", "Siamese")
cat3 = Cat("Luna", "Maine Coon")
cat4 = Cat("Simba", "Bengal")
cat5 = Cat("Nala", "Sphynx")

cat1.piss()
cat2.pissAt("Bob")
cat3.piss()
cat4.pissAt("David")
cat5.pissAt("Emma")


