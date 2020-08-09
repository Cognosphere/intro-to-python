#Make a tuple
t = (1,2,3,4,5)
print(t)
print(len(t))

#Can mix object types
t = (1,2,"three")
print(t)

#indexing and slicing
t = (1,2,"three", "four", "five")
print(t[0])
print(t[3:])

#tuple methods
t = (1,2,"three", "four", "five")
print(t.index("four"))

#immutability
t = (1,2,"three", "four", "five")
#t[0]="not 1"
#print(t)
#t.append("six")
