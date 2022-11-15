
# variable used to define my list
my_list = [ 'Ramen', 'Udon', 'Wonton' ]


# I changed the postion of Udon in my list from 1 to 0
my_list[0] = 'Udon'

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

