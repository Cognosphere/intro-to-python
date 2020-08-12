#Example 1
my_list = [1,2,3,4,5,6,7,8,9,10]
for num in my_list:
  print(num)

#Example 2: With an if statement!
my_list = [1,2,3,4,5,6,7,8,9,10]
for num in my_list:
  if num%2==0:
    print(num)

#Example 3: Add an else statement too!
my_list = [1,2,3,4,5,6,7,8,9,10]
for num in my_list:
  if num%2==0:
    print(num)
  else:
    print("ODD NUMBER")

#Example 4: Sum of list
my_list = [1,2,3,4,5,6,7,8,9,10]
list_sum = 0 

for num in my_list:
    list_sum+=num

print(list_sum)

#Example 5: Strings too!
for letter in 'This is a string.':
    print(letter)

#Example 6: Don't forget tuples
tup = (1,2,3,4,5)

for t in tup:
    print(t)

#Example 7: Tuple unpacking
list2 = [(2,4),(6,8),(10,12)]
for tup in list2:
    print(tup) #guess what will be prined...

for (t1,t2) in list2: #Tuple unpacking
    print(t1)

#Example 8: Dictionaries!
d = {'k1':1,'k2':2,'k3':3}
for k,v in d.items():
    print(k)
    print(v)