'''
Questions:

Conditional Statements:

Write a Python program that prompts the user for their age and
checks if they are eligible to vote. Voting age is 18 or above.
The program should print either "You are eligible to vote" or
"You are not eligible to vote".
'''
age = int(input("Please Enter your age "))
if age >=18:
    print("You are eligibile to vote")
elif(age<18):
    print("You are not eligible to vote")
else:
    print("Invalid age.")
'''
While Loops:

Write a Python program that prompts the user to enter a number.
The program should keep prompting the user until a positive number
is entered. Once a positive number is received, print "Thank you
for entering a positive number".
'''

end = False
while(end == False):
    num = float(input("Please Enter a positive number "))
    if num>=0:
        print("Thank you for entering a positive number")
        end= True
'''
For Loops with Range:

Write a Python program that prompts the user for a number, n, 
and then prints the first n squares. For example, if the user 
enters 5, the program should print:

1
4
9
16
25
'''
numb = int(input("Please enter a number "))
if numb < 1:
    print("Please enter a positive integer.")
else:
    for i in range(1, numb + 1):
        print(i ** 2)
       
'''
Comparison Operators:

Write a Python program that asks the user for three numbers, a, b,
and c. The program should check and print the largest number among
the three. If two or more numbers are the largest (i.e., equal),
print "There's a tie" followed by the largest number.
'''

a = int(input("Enter the first number (a): "))
b = int(input("Enter the second number (b): "))
c = int(input("Enter the third number (c): "))

if a == b == c:
    print(f"There's a tie.")
else:
    lar_num = max(a, b, c)
    print(f"The largest number is {lar_num}")

'''
Proper Python Syntax:

Write a Python program that calculates the area of a rectangle.
Prompt the user for the length and width of the rectangle, 
compute the area, and display the result. Make sure to use
appropriate variable names, formatting, and comments within the code.
'''
len = float(input("Enter the Length of rectangle  ")) #Obtaining Length of the rectangle
wid = float(input("Enter the width of rectangle  ")) #Obtaining Width of the rectangle

print("Area of the rectangle", len*wid) #Printing area of the rectangle
'''
Getting User Input:

Write a Python program that prompts the user for their favorite color. 
Once the color is received, the program should print: "Your favorite color is [color]", 
where [color] is replaced with the user's input.

hint
'''
color= input("Enter your favorite Color ")
print("Your Favorite color is",color)
'''

color = "blue"


print("the color is",color," and i like it ")


'''