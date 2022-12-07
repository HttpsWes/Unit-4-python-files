# price = 3.99

# print("you price total is", price, "wan to pay now?")

try:
    age = int(input('Enter your age: '))

    faveNum = int(input('What is your favorite number: '))

    if age <= 21:
     print('You are not allowed to enter, you are too young.')

    else:
        print('Welcome, you are old enough.')

    print("Fun Fact! Your age divided by your favorite number is: " , age / faveNum)

except ValueError:
    print("Use a string")

except ZeroDivisionError:
    print("please do not  enter Zero!")

finally:
    print("You are not a PICNIC :D")






    