import numpy as np
def add(a,b):
    return a+b

def sub(a,b):
    return a-b

def mul(a,b):
    return a*b

def div(a,b):
    if b!=0:
        return a/b
    else:
        return ("Denominator cannot be zero!")
    
print("Select operation: ")
print("1. Addition: ")
print("2. Subtraction: ")
print("3. Multiplication: ")
print("4. Division: ")

choice=int(input("Enter a number between 1-4: "))

a=float(input("Enter first number: "))
b=float(input("Enter second number: "))

if choice==1:
    result=add(a,b)
    operation="+"
elif choice==2:
    result=sub(a,b)
    operation="-"
elif choice==3:
    result=mul(a,b)
    operation="*"
elif choice ==4:
    result=div(a,b)
    operation="/"
else:
    print("Invalid input!")
    
print(f"{a}{operation}{b}={result}")




a1=np.range(1,10).reshape(3,3)
a2=np.range(1,10).reshape(3,3)
print(a1)
print(a2)

# (lambda x:x*x)(5)

