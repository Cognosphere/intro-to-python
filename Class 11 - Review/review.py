'''
Class 2 Review Problem
Define a dog’s name, breed, color, and age. Then, add those variables into a sentence
'''
dog_name = "Max"
dog_breed = "poodle"
dog_color = "white"
dog_age = 5

#Method 1:
print("My {}-year old dog {} is a {} {}".format(dog_age, dog_name, dog_color, dog_breed))

#Method 2:
print("My {3}-year old dog {0} is a {2} {1}".format(dog_name, dog_breed, dog_color, dog_age))

#Method 3:
print(f"My {dog_age}-year old dog {dog_name} is a {dog_color} {dog_breed}")


'''
Class 3 Review Problem
Make a list with different food. Print the second food on the list. 
Create a sentence with one of the foods... 
Hint: You’ll need string formatting and indexing
'''
food = ["pizza", "sandwiches", "burritos", "chicken"]
print(food[1])
print(f"My favorite food is {food[0]}")



'''
Class 4 Review Problem
Make a list with the numbers 1-10
Print the entire list
Print the number ‘5’
Print the numbers 5-10
Print the entire list backwards
Add 11 to the list
Remove the number ‘1’
Find the length of the list
'''
nums = [1,2,3,4,5,6,7,8,9,10]
print(nums)
print(nums[4])
print(nums[4:])
print(nums[::-1])
nums.append(11)
print(nums)
nums.pop(0)
print(nums)
print(len(nums))


'''
Class 5 - No Review (Was a unit test)
'''


'''
Class 6 Review Problem
Define a variable as an integer (you can choose any number)
ex. number = 5
Take user input to get another number
Print the boolean (True or False) of the number you defined and the number the user gave with the == comparison operator.
'''
my_num = 5
user_num = int(input("Please enter a number: "))
print(my_num==user_num)



'''
Class 7 Review Problem
Grade Calculator
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



'''
Class 8 Review Problem
Use a while loop to print numbers 0-20.
'''
x=0
while x<=20:
  print(x)
  x+=1

'''
Class 8 Review Problem
Use a for loop to find those numbers which are divisible by 7 and divisible by 5, between 1400 and 2800
'''
for num in range(1400,2801):
  if num%7==0 and num%5==0:
    print(num)

'''
Class 8 Review Problem
Use while loops to generate the shape 
*
**
***
****
'''
x=0
while (x<5):
  print("*"*x)
  x+=1



'''
Class 9 Review Problem
Use list comprehension to find how many letters are in a word
'''
lst = [x for x in 'character']
print(len(lst))



'''
Class 10 Review Problem
Write a Python function to find the Max of three numbers.
'''
def max_of_two( x, y ):
    if x > y:
        return x
    return y
def max_of_three( x, y, z ):
    return max_of_two( x, max_of_two( y, z ) )
print(max_of_three(3, 6, -5))

