# X is my vairble that i used to store the nmber 100
x = 100

# input statment. I  included a int type so my code can by enter as a interger
x=int(input("What is your GPA?"))


# This is my if conditional statement the prints; If x is greater then or equal to 90 you will recive an A.
if x >= 90:
    print("Good Job you get an A")

# This is my else conditional statement that decides if my if statment above is not true then the following will happening
elif x >= 80 and x <=89:
    print("You scored Well. You get an B")

elif x >= 70 and x <=79:
    print("You did a decent job. You get an C")

elif x >= 60 and x <=69:
    print("try harder next time. You get an D")
#  --------------------------------------------------------------------------------------------------------------------------

# When my other if and elif conditional statements are not met then this will print. 
else:
   
    print("You failed. You get an F")
