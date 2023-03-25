#loop
#for i in range(1,10):
   # print(i)
#    print(i, end=" ")

"""str="asdfjasfkjdsf"
for i in str:
    print(i)"""


#format string
"""string="Sailesh"
age=23
print(f"My name is { string} and i am {age} years old")"""
# num= input("enter a number")
# print(f"the number you entered is {num}")

#calculate the sum of all numbers from 1 to given number
number= int(input("enter a number"))
sum=0
for i in range (1,number):
    sum=sum+i

print(f"the sum of all numbers from 1 to {number} is {sum}")

for i in range(1, number):
    print(f"{number} * {i} = {number*i}")
   
