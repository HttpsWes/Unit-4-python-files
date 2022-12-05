my_file = open("Wesley.txt", "r+")

# print(my_file.readlines())

# print("hello")

# print("world")

for line in my_file.readlines():
    print(line, end="")
my_file.writelines(['Im writing from python Boo'])