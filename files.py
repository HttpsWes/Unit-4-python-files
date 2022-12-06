my_file = open("Wesley.txt", "a")

# print(my_file.readlines())

# print("hello")

# print("world")

my_file.write('Im writing from python Boo \n')

my_file.close()

my_file = open("Wesley.txt")

for line in my_file.readlines():
    print(line, end="")

