my_todo = open("toodoo.txt","a")

# print(my_todo.read())

while True:

    x = input("What to add to list?")

    my_todo = open("toodoo.txt","a")

    my_todo.write(x + "\n")

    my_todo.close()

    

    my_todo = open("toodoo.txt",)

    
    for line in my_todo.readlines():

        print(line, end="")

# my_todo.close()

# my_todo = open("todo.txt")


# while True:
#     print("Your todo list is")
#     print(todos)

#     x = input("What to add to list?")

#     todos.append(x)



