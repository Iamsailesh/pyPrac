'''String Slicing
abc="Hello World"
print(abc[0]) #- indexing is possible....-1= last letter
print(abc[0]+abc[-1])
#to take input
userInput = input("Enter a number")
print("you enter"+userInput)
print(input("enter another number"))
userInput2=input("Enter a string : ")
print("your last and first letter is :" +userInput2[0]+userInput2[1]+userInput2[-2]+userInput2[-1])
text="sdkjflksdjfsdljfdslks"
print(text[0:5])
'''
# print(userInput[-1]+userInput[1:-1]+userInput[0])
# userInput=input("Enter a string :")
# str="asdfd"
# print(str.upper())
# print(str.capitalize())
# userInput= input("Enter a word: ")
# print("In upper case: "+userInput.upper()+" In lower Case: "+userInput.lower())
"""char="a"
word= input("enter a word ")
bol=(word[0]==char)
print(bol)
if(word[0]==char):
  print("ture")
else: 
    print("false")"""

#write a program to reverse a string
word="aklsdfjdls"
print(word[-1:0:-1]+word[0])
print(word[-1::-1])
print(word[::-1])