homework_done = True
#homework_done = False


if (homework_done) == True:
  print("You can play video games!")
else:
  print("Go finish your homework.")


#if statement and allows the user to guess a number
num = 5
guess = int(input("Guess a number between 1 and 10: "))
if guess==num:
  print("Congratulations! You win!")
else:
  print("Nope, that's wrong")

'''
PRACTICE
Define a name.
Make a program that asks the user for their name. 
Then, if the name the user gave is equal to your actual name, the program prints “That’s me!”. 
Otherwise, if the inputted name is not your actual name, it prints “That is not me!”
'''
name = "John"
user_name = input("Please enter your name: ")
if name==user_name.capitalize():
  print("That's me!")
else:
  print("That is not me :(")

'''
PRACTICE: Grade Calculator
Have a user enter a grade percentage	
ex. 50, 60, 70, 80, or 90
Calculate if the user has an A, B, C, D, or F in the class
'''
grade = int(input("Please enter your grade percentage: "))
if grade>=90:
  print("You have an A. Great job!")
elif grade>=80 and grade<90:
  print("You have a B. Nice!")
elif grade>=70 and grade<80:
  print("You have a C.")
elif grade>=60 and grade<70:
  print("You have a D. Study harder!")
else:
  print("You have an F. Oh no!")

#multiple if statements
a=20
if a>20:
  print("Greater than 20")
if a>15:
  print("Greater than 15")
if a>10:
  print("Greater than 10")
else:
  print("Less than 10")

#if inside of an if statement. Let's go back to our homework_done example for this
#Original:
homework_done = True
if (homework_done) == True:
  print("You can play video games!")
else:
  print("Go finish your homework.")

#Revised:
homework_done = True
dishes_done = True
#dishes_done = False
if (homework_done) == True:
  if dishes_done == True:
    print("You can play video games!")
else:
  print("Go finish your homework.")