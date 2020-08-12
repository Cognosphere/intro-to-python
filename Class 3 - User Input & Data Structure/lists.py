#Let's make our first list
my_list = [1,2,3]
print(len(my_list))

my_list= ["Hello", 15, 1.5, "This is a sentence."]
print(len(my_list))
print('\n')

#Indexing & Slicing
my_list = [1,2,3,4]
#Remember indexing from strings?
print(my_list[0])
print(my_list[1:])
print(my_list[:3])

#Error if index doesn't exist
print(my_list[100])

#You can add values to a list
print(my_list + [5])
#This won't change the original list
print(my_list)
#But, you can change the original list like this:
my_list = my_list + [5]
print(my_list)
print("\n\n")

'''
PRACTICE PROBLEM: Make a list with different food. Print the second food on the list. 
Challenge: Create a sentence with one of the foods... Hint: You’ll need string formatting and indexing
'''
food = ["pizza", "sandwiches", "burritos", "chicken"]
print(food[1])
print(f"My favorite food is {food[0]}")