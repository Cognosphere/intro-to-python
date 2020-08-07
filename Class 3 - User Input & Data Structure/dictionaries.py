#How to make a dictionary
my_dict = {'key1':'value1','key2':'value2'}
print(my_dict["key2"])

#Dictionaries are flexible. They can hold different data types.
my_dict = {'key1':123,'key2':[12,23,33],'key3':['item0','item1','item2']}
print(my_dict["key3"])

#Go even more in depth with indexing
print(my_dict["key3"][0])

#Change values
print(my_dict["key1"])
my_dict["key1"] = my_dict["key1"]-100
print(my_dict["key1"])

#Add to Dictionaries
my_dict["key4"] = "value4"
my_dict["key5"] = "value5"
my_dict["key6"] = "value6"
print(my_dict)
print("\n")

#What can we use dictionaries for?
price_lookup = {"apple":2.99, "banana":3.99, "mango":4.50, "blueberries":5.49, "cherries":4.75, "peach": 2.99, "watermelon":6.99, "strawberries":6.99}
print(price_lookup)
print(price_lookup["banana"])
print(price_lookup["cherries"])
print(price_lookup["strawberries"])

#Nested dictionaries
nested = {'key1':{'nestkey':{'subnestkey':'value'}}}
print(nested["key1"]["nestkey"]["subnestkey"])

#Special dictionary methods
d = {'key1':1,'key2':2,'key3':3}
print(d.keys())
print(d.values())

