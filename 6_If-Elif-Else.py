# #if-elif-else ladder in Python 
a = 14

if(a>3): 
    print("The value of a is greater than 3") #Indentation(Tab or 4 Spaces)
if(a<13):
    print("The value of a is lesser than 13")
elif(a>7):                                    #Elif= Else If
    print("The value of a is greater than 7")
elif(a>17):
    print("The value of a is greater than 17")
else:
    print("Nothing")

# #Multiple if statements
b=8
if(b<3):                                      #Not in ladder
    print("The value of b is greater than 3")

if(b>13):                                     #Not in ladder
    print("The value of b is greater than 13")
    
if(b>7):                                      #Not in ladder
    print("The value of b is greater than 7")

if(b>17):                                     #In if- else ladder
    print("The value of b is greater than 17")
else:
    print("Nothing")

print("Done")


# #in & is
c = None

if (c==6):
    pass       # Pass to don't get an error
if (c is None):   # also "is not" 
    print("Yes")
else:
    print("No")

d = [45, 56, 6]
print(435 in d)

text = input("Enter the text:\n")
if("Make a lot of money" in text or "Buy now" in text or "Subscribe this" in text or "Click it" in text):
    print("This text is spam")
else:
    print("This text is not spam")

un = input("Enter the username: ")
if len(un)<10:
    print("allowed")
else:
    print("not allowed")

# #Nested Structure to find greatesst number
p=int(input("Enter the 1st no.:\n"))
q=int(input("Enter the 2nd no.:\n"))
r=int(input("Enter the 3rd no.:\n"))
if (p>q and p>r):
    print("p is greatest", p)
else:
    if (q>p and q>r):
        print("q is greatest", q)
    else:
        print("r is greatest", r)

str1 = "hello"
v=0 
for x in str1:
    if(x!="1"):
        v=v+1
    else:
        pass
print(v)

a,b = 12,5
if a+b:
    print("True", a+b)
else:
    print("False")

x=0
while(x<=100):
    x+=2
    print(x)
