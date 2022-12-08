class person:
    species = 'Homosapien'



    def __init__(self, name, age):
            self.name  = name
            self.age =  age
            print("Hello World")



    def hi(self):
     print("My name is" + self.name)
        


Wesley = person("Wesley",17)

print(Wesley.species)
print(Wesley.age)
print(Wesley.name)
Wesley.hi()

Bryant = person("Bryant",17)

print(Bryant.age)
print(Bryant.name)

