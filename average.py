#Empty list 
grades = []
#Total amount 
total = 0


# Infinte While statement is uses to repeated ask user whathtuer grade is
while True:
    # Simple input statement that asks  for grades in the from  of a interger 
    x = int(input('What is your grade?'))
    #Once those grades are in we use append to add them to our list
    grades.append(x)

    z=input("Enter stop to finshing  entering  grades")
    # I used an if statment that states if its conditions arent meet the infinte loop will broke
    if z=="stop":
        break
    # If the else statments are not met then the code will just print thec grades 
    else:
        print(grades)

# I used a for  loop find the average of my grades
for grade in grades:
    total =  total + grade

print('your total is...')
#Total of my  grades is didved by  the amount of grades entered
print (total/len(grades))

