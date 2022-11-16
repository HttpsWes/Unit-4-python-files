#Empty list 
x = []

grades = int(input("What is your grade?".split(" , ")))

print(grades)

sum = 0

for grade in x:
    sum =  sum  + grade

print(sum/len(grades))

