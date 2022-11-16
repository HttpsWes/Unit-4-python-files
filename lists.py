
# variable used to define my list
my_list = [ 'Ramen', 'Udon', 'Wonton' ]


# I changed the postion of Udon in my list from 1 to 0
my_list[0] = 'Udon'

my_list[1] = 'Ramen'

print(my_list)

# With del command i can delete items onmy list
del my_list[2]

# i added items to my list
my_list.append("tomato")

print(my_list)

# I created a tuple and added items to it
my_tuple = ("apple", "banana", "orange", "grape")

#   Since tuples are imutable they don't all for ou to make changes
# i tried to append and del my list but tuple would not allow me
my_tuple.append("peer")

print(my_tuple)

del my_tuple[2]

my_tuple[0]='peaches'

print(my_tuple)

# Len command allows me to see the number of items in m list
print(len(my_list))

print(my_list)

# sort allows me to sort my list items in order
my_list.sort()

print(my_list)
# reveerse allows me to reverse the order of the items on my list
my_list.reverse()

print(my_list)

second_list= ['blue', 'red', 'green', 'black', 'white']

# i used the + opperator to combine my list
print(my_list + second_list)

# Used "join" to add a character between my items
print(" | ".join(my_list + second_list))

# split allows me to spereate stringes
names = "anna, wesley, saint".split(" , ")

print(names)