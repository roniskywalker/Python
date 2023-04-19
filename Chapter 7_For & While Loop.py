# #While loop 
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

# #For loop

c = [2, "AH", 54, 7, 12, 9, 14]
for item in c:
    print(item)

# #Range Function
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

# #Break statement
for f in range(10):
    print(f)
    if f == 5:
        break
else:
    print("Done")

for q in range(4):
    break

# #Continue statement 
for g in range(10):
    if g == 5:
        continue
    print(g)
else:
    print("Complete")

# #Pass Statement
h = 4

if h>0:
    pass

# #try
try:
    answer=10/1  #/0
    num1= float(input("Enter the number:\n"))
    print(num1)
except ZeroDivisionError as err:
    print(err)
except ValueError:
    print("Invalid Input")