#Functions

def mySum(num1, num2):
    return(num1 + num2)

print(mySum(6,32))


def greet(name="Stranger"):
    print("Good Day, "+ name)
 

greet("Harry") 
greet()



def factorial_iter(n):  # itretive factorial method
    product = 1
    for i in range(n):
        product = product * (i+1)
    return product
a= int(input("Enter the number:\n"))
b = factorial_iter(a)
print(b)


#Recursion

def factorial_recursive(n):
    if n == 1 or n == 0:
        return 1
    else:
        return n * factorial_recursive(n-1)  # sum(n) = sum(n-1) + n

f = factorial_recursive(3)
print(f)



def farh(cel):
    return (cel *(9/5)) + 32

c = 0
f = farh(c)
print("Fahreheit Temperature is " + str(f))




def remove_and_split(string, word):
    newStr = string.replace(word, "")
    return newStr.strip()

this = "     Harry is a good      "
n = remove_and_split(this, "Harry")
print(n)



def multab(number, limit):
    for i in range(1, limit+1):
        print(f"{number} x {limit} = {number*i}")
    return

n1= int(input("Enter the no.:\n"))
l1= int(input("Enter the limit:\n"))
print(multab(n1, l1))



def myfun(b, c=3, d="hello"):
    print (b + c)
    return
# myfun(5,3,"hello")
# myfun(5,3)
myfun(5)



def printinfo( name, age = 35 ): 
    print ("Name: ", name)
    print ("Age ", age)
    return
printinfo( age=50, name="miki" )
printinfo( name="miki" )


def foo(x=1,y=2,z=3): print(2*x,4*y,8*z)
foo()


def power(base_num, pow_num):
    result=1
    for index in range (pow_num):
        result = result * base_num
    return result
print(power(3, 2))



#lambda Expressions
x = lambda m: m*m
x(3)


def func1(n):
    return lambda x:x*n
r= func1(3)
print(r(4))