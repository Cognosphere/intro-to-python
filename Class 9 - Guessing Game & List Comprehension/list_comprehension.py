lst = [x for x in 'word']
print(lst)

''' 
Square numbers in a range and turn in into a list
'''
lst = [x**2 for x in range(0,11)]
print(lst)


'''
Use your knowledge of list comprehension to find all even numbers in a range of 11.
'''
lst = [x for x in range(0,11) if x%2==0]
print(lst)