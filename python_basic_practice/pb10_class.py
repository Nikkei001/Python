class Person:
    species = "human"
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def printAge(self):
        print(self.age)

class Athlete(Person):
	def printAge(self):
		print(str(self.age) + "athlete")
	def running(self):
		print("run")

p = Person("Alice", 25)
print(p.name)  # 输出: Alice
print(p.age)   # 输出: 25
p.printAge()   # 输出: 25
Person.printAge(p) # 输出: 25
print(Person.printAge) # 输出: <function Person.printAge at 0x00000224377989D0>
print(Person.species) # 输出: human
print(p.species) # 输出: human
a = Athlete("Bill", 25)
a.running()
a.printAge() # 多态