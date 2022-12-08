class person:
    species = 'Homosapien'



    def __init__(self, name, age):
            self.name  = name
            self.age =  age
            print("Hello World")



    def hi(self):
     print("My name is" + self.name)
        



class Teacher(person): 
    role = 'teacher'

    def hi(self):
        print("Hi  my name is Mr" + self.name)
forlenza = Teacher("forlenza",95)
print(forlenza.role)
forlenza.hi()


class student(person):
    role = 'student'

Wesley = student("Wesley",17)

print(Wesley.role)

print(Wesley.species)
print(Wesley.age)
print(Wesley.name)
Wesley.hi()
Bryant = person("Bryant",17)

print(Bryant.age)
print(Bryant.name)