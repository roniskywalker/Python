story = "once upon a time there was a youtuber named Roni who uploaded python course with notes Roni"

# #String Slicing
print(story[1])
print(story[1:6])
print(story[ :4])
print(story[1: ])
print(story[1:4:2])   #slicing with skip value
print(story[0::3])
print(story[-14:-1])

print(len(story))
print(type(story))

# #String methods
print(story.endswith("notes"))
print(story.count("c"))
print(story.capitalize())
print(story.find("upon"))
print(story.find("Ron"))
print(story.replace("Roni", "CodeWithRoni"))
print(story.upper())
print(story.upper().islower())
print(story.lower())
print(story.index("a"))

# #Escape Sequences
A="Ma\"am, I am An\\\kan Hazra.\nI am\t good boy."
print(A)

# #Numbers
my_num = -5
print(abs(my_num))
print(pow(my_num, 2))
print(max(my_num, 15))
print(min(my_num, 5))
print(round(3.4))
from math import *
print(floor(7.8))
print(ceil(4.6))
print(sqrt(25))

name=input("Enter your name:\n")
date=input("Enter date:\n")

print(f'''Dear {name},
Your DOB is {date}''')

a_1 = 5
b_2 = 10.2
c_3 = "Ankan"
print(str(a_1) +" "+ str(b_2) + c_3) #Concatenation of String

# #strip
this = "     Roni is a good      "

print(this)
print(this.strip())