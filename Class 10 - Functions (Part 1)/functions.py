#function that greets people with their name:
def greeting(name):
    print(f'Hello {name}')

greeting("Myles")


#function with return:
def add_num(num1,num2):
    return num1+num2

print(add_num(4,5))
answer = add_num(4,5) #can also save as variable (return)
print(answer) 
print(add_num("Hello ", "John")) #strings work too!


#difference between print and return:
def print_answer(a,b):
    print(a+b)
def return_answer(a,b):
    return a+b
print_answer(10,5)
print(return_answer(10,5)) #we need to say print because it is saved as a variable

#what if we want to save it for a later use?
my_result = print_answer(20,30)
print(my_result) #will return a None type
#print(my_result*2)

my_result = return_answer(30,20)
print(my_result)
print(my_result*2)

#check if any number in a list is even
def check_even_list(num_list):
    # Go through each number
    for number in num_list:
        # Once we get an even number, we return True
        if number % 2 == 0:
            return True
        # Otherwise we don't do anything
        else:
            pass #DO NOT SAY return False here because it        will not check other numbers
    return False #we have gone through the entire for loop               and it has not returned True, so we can                now safely return False

print(check_even_list([1,2,3]))
print(check_even_list([1,3,5]))

#return all even numbers in a list  
def check_even_list(num_list):  
    even_numbers = []  
    # Go through each number
    for number in num_list:
        # Once we get an even number, we append the even number
        if number % 2 == 0:
            even_numbers.append(number)
        # Don't do anything if its not even
        else:
            pass
    # Notice the indentation! This ensures we run through the entire for loop    
    return even_numbers
print(check_even_list([1,2,3,4,5,6]))
print(check_even_list([1,3,5]))

#function to check whether a number is in a given range
def test_range(n): 
  if n in range(3,9): 
    print(f"{n} is in the range") 
  else : 
    print("The number is outside the given range.") 
    test_range(5)

test_range(12)

'''
Write a function that returns the lesser of two given numbers if both numbers are even, but returns the greater if one or both numbers are odd. use min(a,b) and max(a,b)
'''
def lesser_of_two_evens(a,b):
    if a%2 == 0 and b%2 == 0:
        return min(a,b)
    else:
        return max(a,b)
print(lesser_of_two_evens(2,4))
print(lesser_of_two_evens(2,5))

"Write a function takes a two-word string and returns True if both words begin with the same letter"
def animal_crackers(text):
    wordlist = text.split()
    return wordlist[0][0] == wordlist[1][0]
animal_crackers('Levelheaded Llama')
animal_crackers('Crazy Kangaroo')

'''
Given two integers, return True if the sum of the integers is 20 or if one of the integers is 20. If not, return False
'''
def makes_twenty(n1,n2):
    return (n1+n2)==20 or n1==20 or n2==20
makes_twenty(20,10)
makes_twenty(11,9)
makes_twenty(2,4)