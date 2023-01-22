#While loop 

i = 0
while i<10:
    print("Yes " + str(i))
    i = i + 2

print("Done")

s=0                 
while s<10:
    s+=1          #print(s)
    print(s)      #s+=1           # Both are different
    

# #infinite loop
# b=0
# while b>=0:
#     print(str(b))
#     b+=1 # or without this 



fruits = ['Banana', 'Watermelon', 'Grapes', 'Mangoes']
a = 0
while a<len(fruits):
    print(fruits[a])
    a = a+1

#For loop

c = [2, "AH", 54, 7, 12, 9, 14]
for item in c:
    print(item)

#Range Function
for d in range (1, 15, 2):
    print("d",d)


for d1 in range(18,1,-1):
    print("d1", d1) 

ss="banana"
for i in ss:
   print(i)

for e in range(8):
    print(e)
else:
    print("This is inside else of for.")

# Break statement
for f in range(10):
    print(f)
    if f == 5:
        break
else:
    print("Done")

for q in range(4):
    break

# Continue statement 
for g in range(10):
    if g == 5:
        continue
    print(g)
else:
    print("Complete")

# Pass Statement

h = 4

if h>0:
    pass


# Multiplication Table
num = int(input("Enter the number:\n"))
limit = int(input("Enter the limit:\n"))
for j in range(1, limit+1):
    # print(str(num) + " X " + str(j) + "=" + str(j*num))
    print(f"{num} X {j} = {num*j}") #f string

# Reverse Multiplication Table  

num1 = int(input("Enter the number1:\n"))
limit1 = int(input("Enter the limit1:\n"))
for j in range(limit1, 0, -1):
    # print(str(num) + " X " + str(j) + "=" + str(j*num))
    print(f"{num1} X {j} = {num1*j}") #f string


num2 = int(input("Enter the number2: "))
j=0
while (j<=10):
    print(f"{num2} X {j} = {num2*j}")
    j+=1




l1 = ["Harry", "Sohan", "Sachin", "Rahul"]

for name in l1:
    if name.startswith("S"):
        print("Hello "+name)





num3 = int(input("Enter the number3: "))
prime = True

for w in range(2, num3):
    if(num3%w == 0):
        prime = False
        break
if prime:
    print("This number is Prime")
else:
    print("This number is not Prime")




#Factorial
num4 = int(input("Enter the number4: "))
factorial = 1
for i2 in range(1, num4+1):
    factorial = factorial * i2
print(f"The factorial of {num4} is {factorial}")

#Summation
num5 = int(input("Enter the number5:\n"))
Sum = 0
for i3 in range(1, num5+1):
    Sum = Sum + i3
print(f"The Sum of first {num5} numbers is {Sum}")

#Odd no. summation
 #for i3 in range(1, num5+1, 2):
#Even no. summation
 #for i3 in range(0, num5+1, 2):

#1/1+1/2+1/3....+1/k
#  for i3 in range(1, k+1):
#      sum=sum+1/i3

for num in range(10,14):
    for i in range(2, num):
        if num%i==1:
            print(num)
            break



# Find the digit sum of a number

num=int(input("Enter a value"))
sum=0
while(num!=0):
   r=num%10
   sum=sum+r
   num=int(num/10)
print(sum)


# try
try:
    answer=10/1  #/0
    num1= float(input("Enter the number:\n"))
    print(num1)
except ZeroDivisionError as err:
    print(err)
except ValueError:
    print("Invalid Input")