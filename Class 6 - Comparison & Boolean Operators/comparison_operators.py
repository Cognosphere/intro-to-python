#Comparison Operators: ==,!=, >, <, >=, <=

print("== Operator")
print(2==2) #This will return True
print(1==2) #This will return False
print("----------")

print("!= Operator")
print(2!=2) #This will return False
print(1!=2) #This will return True
print("----------")

print("> Operator")
print(3>2) #This will return True
print(1>2) #This will return False
print("----------")

print("< Operator")
print(3<2) #This will return False
print(1<2) #This will return True
print("----------")

print(">= Operator")
print(3>=2) #This will return True
print(2>=2) #This will return True
print(1>=2) #This will return False
print("----------")

print("<= Operator")
print(3<=2) #This will return False
print(2<=2) #This will return True
print(1<=2) #This will return True
print("----------")


#Chained Comparison Operators
print(1<2<3) #will return True
print(1<2>3) #will return False

#different method- "and" keyword checks if both conditions are true
print(1<2 and 2<3) #will return True
print(1<2 and 2>3) #will return False

print(2==2 and 3==3) #will return True

#use different comparison operators at once
print(2==2 and 3!=2) #will return True

#or keyword checks if one of the conditions are true
print(2==2 or 1<2) #will return True
print(1<2 or 2<3 or 5<100 or 5<=100 or 2!=2 or 5==5) #will return True

'''
PRACTICE
Define a variable as an integer (you can choose any number)
ex. number = 5
Take user input to get another number
Print the boolean (True or False) of the number you defined and the number the user gave with the == comparison operator.
'''

my_num = 5
user_num = int(input("Please enter a number: "))
print(my_num==user_num)

'''
Note: 
If you don't put int(input()) instead of input, then it will always return False because one type is an integer and one type is a string
'''


