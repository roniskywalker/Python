v_122 = '''Ankan" ' '''
# v = 'Ankan'
n = 345
m = 45.32
h = 2+4j
o = True#/False
o = None

# #Printing the variables
print(v_122)
print(n)
print(m)
print(h)
print("bool",o)

k=3
l=7
p=9
print('k={1}, l={2} and p={0}'. format(k,l,p))
print("k=",k, "," ,"l=", l, ",", "p=",p)
print("k=%d"%k, "l=%d"%l, "p=%d"%p )

name = 'cyborg' 
number = 31 
print ('%s %d' % (name, number))    #%f for float

# #Printing the type of variables
# print(type(v))
print(type(n))
print(type(m))
print(type(h))
print(type(o))

a = 3
b = 4

# #Arithmetic Operators
print("The value of 3+4 is ", 3+4)
print("The value of 3-4 is ", 3-4)
print("The value of 3*4 is ", 3*4)
print("The value of 3/4 is ", 3/4)
print("The reminder is", a%b)

# #Assignment Operators
p = 34
p -= 12
p *= 12
p /= 12
print("p",p)

# #Comparison Operators
q1 = (14<=7)
print("Q1",q1)
q2 = (14>=7)
print("Q2",q2)
q3 = (14<7)
print("Q3",q3)
q4 = (14>7)
print("Q4",q4)
q5 = (14==7)   #true if values are equal
print("Q5",q5)
q6 = (14!=7)   #true if values are not equal
print("Q6",q6)

# #Logical Operators
bool1 = True
bool2 = False
print("The value of bool1 and bool2 is", (bool1 and bool2))
print("The value of bool1 or bool2 is", (bool1 or bool2))
print("The value of not bool2 is", (not bool2))

# #To Integer Typecasting
U = "34"
U = int(U)
print(type(U))
print('U+5',U + 5)

j = input("Enter a number: ")   #Taking input from user
j = int(j)   #Convert j to Integer(if possible)
print(type(j))

# #Square Value
r=float(input("Enter The number:\n"))
Sqr= r**2
print("The Square is ", Sqr)
