#ERROR HANDLING 
try:
    a= int(input("enter a number"))
    print(10/a)
except ZeroDivisionError:
    print("cant be divided by 0")
finally:
    print("finally vet vayo kta ho...finallay finally")

