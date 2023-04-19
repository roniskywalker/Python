# #Functions
def mySum(num1, num2):
    return(num1 + num2)

print(mySum(6,32))

def greet(name="Stranger"):
    print("Good Day, "+ name)

greet("Roni") 
greet()

def factorial_iter(n):  # itretive factorial method
    product = 1
    for i in range(n):
        product = product * (i+1)
    return product
a= int(input("Enter the number:\n"))
b = factorial_iter(a)
print(b)

# #Recursion
def factorial_recursive(n):
    if n == 1 or n == 0:
        return 1
    else:
        return n * factorial_recursive(n-1)  # sum(n) = sum(n-1) + n

f = factorial_recursive(3)
print(f)

def printinfo( name, age = 35 ): 
    print ("Name: ", name)
    print ("Age ", age)
    return
printinfo( age=50, name="miki" )
printinfo( name="miki" )

# #lambda Expressions
x = lambda m: m*m
x(3)

def func1(n):
    return lambda x:x*n
r= func1(3)
print(r(4))