#Note: This code is not meant to be run altogether, as it is a teaching tool during our live classes. These are a series of programs taught invidually throughout a lesson. Feel free to still run the programs, though. Sign up for  classes at our website, www.cognosphere.tech

active = True
#must define above

while(active!=False):
  answer = input("Are you active? ")

  if (answer=="no"):
    active=False


''''
make sure to avoid infinite loops, like below
x=5
while(x%2==1):
  print(x)
  x+=2
'''

'''
Create a program that counts to a certain number starting from 1, and when you get to that number print out “Done Counting!”
'''
count = 1
end = 10
while(count<=end):
  print(count)
  count+=1


'''
PRACTICE
Use a while loop to print x times 2 until x reaches 1000.
'''
x = 1
while(x<1000):
  print(x)
  x=x*2


'''
Start with x=0
Use a while loop to add 2 to x every time it runs. Stop the while loop when x gets to 50. Every time the while loop runs, say “The number is now __”, with __ being the new number.
'''
x=0
while(x<=50):
  print(f"The number is now {x}")
  x+=2

'''
Define x as 0
Use a while loop to print x while x is less than or equal to 10. 
The increment is x+=1 
(add 1 to x every time the while loop runs)
Otherwise, when x is not less than 10, print (“All done!”)
'''
x=0
while(x<=10):
  print(x)
  x+=1
else:
  print("All done!")

#example of continue statement
x = 0

while x < 10:
    print('x is currently: ',x)
    print(' x is still less than 10, adding 1 to x')
    x+=1
    if x==3:
        print('x==3')
    else:
        print('continuing...')
        continue #restarts the loop

x = 0

#example of break & continue statement
while x < 10:
    print('x is currently: ',x)
    print(' x is still less than 10, adding 1 to x')
    x+=1
    if x==3:
        print('Breaking because x==3')
        break
    else:
        print('continuing...')
        continue

#example of pass statement. generally a placeholder
while x<10:
  pass