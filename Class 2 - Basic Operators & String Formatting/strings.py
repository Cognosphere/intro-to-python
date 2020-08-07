"This is a string"
"My name is John"

print("My dog is Myles")
print("This is fun")
print("Use \n to print a new line")
print("It worked!")
print("\nEvery \n word \n is \n on \n a \n different \n line")

#The len keyword can check how many characters are in a string
print(len("Hello"))

#Remember variables?
print("\n")
my_name = "John"
print(my_name)

print(len(my_name))

#Strings and indexing: Indexing starts at 0
print(my_name[0])
print(my_name[3])
#print(my_name[4])
print(my_name[-1])

print(my_name[:])
print(my_name[:3])
print(my_name[::1])
print(my_name[::2])
print(my_name[::-1])

#Let's try to change the first letter of my_name
#my_name[0]="r"

#Join a string and a number
age = 15
name = "John"
#print(name+age) <-- This will give an error
print(name+str(age))

#What if we want to print John is 15 years old?
#String formatting - there are many different methods

print("{} is {} years old".format(name, age))
print(f"{name} is {age} years old")

name="Ernie"
print("His name is {}".format(name))
print(f"His name is {name}")



#PRACTICE PROBLEM
#Define a dog’s name, breed, color, and age. Then, add those variables into a sentence

#SOLUTION:
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
