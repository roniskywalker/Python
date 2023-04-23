# #Lists
l = [3,56, 67.56, 0, {2,3}] # Set is allowed in list
print(l)
lucky_numbers= [3,7,9,5,8]
l1 = [1.09, 8, 7, 2, 21.045, "Ankan", 15, False]

# #List Slicing
print(l1[3])
print(l1[1:5:2])
# #List modification
l1[2] = 67
print(l1)

# #List methods
l1.reverse() # reverses the list
print(l1)
l1.append(45) # adds 45 at the end of the list 
l1.append(85)
print(l1)
l1.insert(2, 544) # inserts 544 at index 2
print(l1)
l1.pop(2) # removes element at index 2
print(l1)
l1.remove(2) # removes 21 from the list
print(l1)
l1.extend(lucky_numbers)
print("Lucky numbers", l1)
lucky_numbers.sort()
print(lucky_numbers)
lucky_numbers2 = lucky_numbers.copy()
print(lucky_numbers2)
l1.clear()
print(l1)

l2 = [2,67,1, 0, 3.22, 43]
print(l2) 
print(l2.sort())#It doesnot allowed in Lists
l2.sort()#sorts the list
print(l2)

l3 = []
print(l3)


# #2d Lists
Grid= [
    [2,4,5],
    [7,6,89],
    [56,87,0]
]
print(Grid[1][2])
for row in Grid:
     for col in row:
         print(col)

# #Tuples
t = (1, 2, 4, 5, 4, 1, 2,1 ,1)
print(t[1:4])
# #Tuples Methods 
print(t.count(1))
print(t.index(5))

# #Empty Tuple
t1 = ()
print(t1)
t2 = (1) # doesnot allowed
print(t2)

# #Single elements tuples
t3 = (1,)
print(t3)

a = [2, 4, 56, 7]

print(a[0] + a[1] + a[2] + a[3])
print(sum(a))
