my_list=[1,2,3]
#Append method adds an object to a list
my_list.append("add me!")
print(my_list)

my_list=[1,2,3]
#Pop method removes an object from a list. Based off index
my_list.pop(2)
print(my_list)

my_list=["dog", "cat", "mouse"]
  #my_list.pop("mouse")
my_list.pop(2)
print(my_list)

#Assign variables to popped off object
my_list=["dog", "cat", "mouse"]
x = my_list.pop(2)
print(x)
print(my_list)

#Extra methods
my_list=[3,1,6,7,5,9,2,4,8]
my_list.sort() #sort in alphabetical or numerical order
print(my_list)
my_list.reverse() #reverse list (PERMANENT)
print(my_list)

#Nesting lists
list1=[1,2,3]
list2=[4,5,6]
list3=[7,8,9]
all_lists=[list1,list2,list3]
print(all_lists)
  #print all 3 lists
print(all_lists[1])
  #print one list
print(all_lists[1][0])
  #print one value

#PRACTICE

'''
Make a list with the numbers 1-10
Print the entire list
Print the number ‘5’
Print the numbers 5-10
Print the entire list backwards
Add 11 to the list
Remove the number ‘1’
Find the length of the list
'''
#SOLUTION
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